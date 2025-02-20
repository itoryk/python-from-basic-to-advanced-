SELECT ag.assisgnment_id, ROUND(AVG(ag.grade), 2) as "average score"
FROM  assignments_grades ag WHERE ag.assisgnment_id IN
(
SELECT a.assisgnment_id FROM assignments a
WHERE a.assignment_text LIKE '%прочитать%' OR a.assignment_text LIKE '%выучить%'
)
GROUP BY ag.assisgnment_id