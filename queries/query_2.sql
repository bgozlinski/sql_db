--Uczeń z najwyższą średnią ocen z wybranego przedmiotu.
SELECT s.student_id, s.name, s.surname, ROUND(AVG(g.grade), 2) as average_grade
FROM students s
JOIN grades g ON s.student_id = g.student_id
WHERE g.subject_id = 2
GROUP BY s.student_id, s.name, s.surname
ORDER BY average_grade DESC
LIMIT 1;