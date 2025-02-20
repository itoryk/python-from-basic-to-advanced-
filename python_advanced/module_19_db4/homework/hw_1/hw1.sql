SELECT t.full_name,
   round(avg(ag.grade), 3) as avg_grade
FROM teachers t
        JOIN assignments a ON t.teacher_id = a.teacher_id
        JOIN assignments_grades ag  ON ag.assisgnment_id = a.assisgnment_id
GROUP BY t.teacher_id
ORDER BY avg_grade
limit 1

