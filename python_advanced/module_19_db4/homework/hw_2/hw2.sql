SELECT full_name, sum_grades FROM (
SELECT s.full_name, AVG(ag.grade) as sum_grades
FROM assignments_grades ag
INNER JOIN students s ON s.student_id = ag.student_id
GROUP BY ag.student_id
)
ORDER BY sum_grades DESC
LIMIT 10