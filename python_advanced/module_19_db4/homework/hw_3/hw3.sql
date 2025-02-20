SELECT DISTINCT s.full_name
FROM students s
JOIN students_groups sg ON sg.group_id = s.group_id
WHERE sg.teacher_id = (
    SELECT t.teacher_id
    FROM teachers t
    JOIN assignments a ON t.teacher_id = a.teacher_id
    JOIN assignments_grades ag ON ag.assisgnment_id = a.assisgnment_id
    GROUP BY t.teacher_id
    ORDER BY round(avg(ag.grade), 3) DESC
    LIMIT 1
)
