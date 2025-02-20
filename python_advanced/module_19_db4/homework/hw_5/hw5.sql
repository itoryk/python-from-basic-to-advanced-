SELECT s.group_id, count(s.group_id) FROM students s GROUP BY s.group_id;
SELECT s.group_id, ROUND(AVG(ag.grade), 2) FROM students s JOIN assignments_grades ag ON s.student_id = ag.student_id GROUP BY s.group_id;
SELECT count(distinct s.student_id) AS not_pass FROM students s LEFT JOIN assignments_grades ag ON s.student_id = ag.student_id WHERE ag.grade_id is NULL;
SELECT COUNT(ag.student_id) AS "missed deadline" FROM students_groups sg JOIN assignments a ON sg.group_id = a.group_id JOIN assignments_grades ag on a.assisgnment_id = ag.assisgnment_id WHERE ag."date" > a.due_date;
SELECT COUNT(student_id) AS "repeat_attempts" from (select student_id, count(1) FROM assignments_grades ag GROUP BY student_id HAVING count(1) > 1 );


WITH group_stats AS (
    SELECT
        s.group_id,
        COUNT(s.student_id) AS total_students
    FROM students s
    GROUP BY s.group_id
),
avg_grades AS (
    SELECT
        s.group_id,
        ROUND(AVG(ag.grade), 2) AS avg_grade
    FROM students s
    JOIN assignments_grades ag ON s.student_id = ag.student_id
    GROUP BY s.group_id
),
not_pass AS (
    SELECT
        s.group_id,
        COUNT(DISTINCT s.student_id) AS not_pass
    FROM students s
    LEFT JOIN assignments_grades ag ON s.student_id = ag.student_id
    WHERE ag.grade_id IS NULL
    GROUP BY s.group_id
),
missed_deadline AS (
    SELECT
        sg.group_id,
        COUNT(ag.student_id) AS missed_deadline
    FROM students_groups sg
    JOIN assignments a ON sg.group_id = a.group_id
    JOIN assignments_grades ag ON a.assisgnment_id = ag.assisgnment_id
    WHERE ag.date > a.due_date
    GROUP BY sg.group_id
),
repeat_attempts AS (
    SELECT
        s.group_id,
        COUNT(DISTINCT ag.student_id) AS repeat_attempts
    FROM students s
    JOIN assignments_grades ag ON s.student_id = ag.student_id
    WHERE ag.student_id IN (
        SELECT student_id
        FROM assignments_grades
        GROUP BY student_id
        HAVING COUNT(1) > 1
    )
    GROUP BY s.group_id
)
SELECT
    gs.group_id,
    gs.total_students,
    COALESCE(ag.avg_grade, 0) AS avg_grade,
    COALESCE(np.not_pass, 0) AS not_pass,
    COALESCE(md.missed_deadline, 0) AS missed_deadline,
    COALESCE(ra.repeat_attempts, 0) AS repeat_attempts
FROM group_stats gs
LEFT JOIN avg_grades ag ON gs.group_id = ag.group_id
LEFT JOIN not_pass np ON gs.group_id = np.group_id
LEFT JOIN missed_deadline md ON gs.group_id = md.group_id
LEFT JOIN repeat_attempts ra ON gs.group_id = ra.group_id
ORDER BY gs.group_id;