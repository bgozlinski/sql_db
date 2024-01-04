--Średnia ocen w grupach dla wybranego przedmiotu.
SELECT gr.group_name, ROUND(AVG(g.grade), 2) as average_grade
FROM groups gr
JOIN students s ON gr.group_id = s.group_id
JOIN grades g ON s.student_id = g.student_id
WHERE g.subject_id = 1
GROUP BY gr.group_name;