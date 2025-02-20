SELECT min(expired), ROUND(AVG(expired)), max(expired) FROM
(
SELECT sg.group_id, count(ag.assisgnment_id) as expired
FROM students_groups sg
JOIN assignments a ON sg.group_id = a.group_id
JOIN assignments_grades ag ON a.assisgnment_id = ag.assisgnment_id
WHERE ag.date > a.due_date
GROUP BY sg.group_id
)