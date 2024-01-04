--Średnia ocen dla wszystkich grup, uwzględniając wszystkie oceny.
SELECT gr.group_name, ROUND(AVG(g.grade), 2) as average_grade
FROM groups gr
JOIN students s ON gr.group_id = s.group_id
JOIN grades g ON s.student_id = g.student_id
GROUP BY gr.group_name;