--5 uczniów z najwyższą średnią ocen ze wszystkich przedmiotów.
SELECT s.student_id, s.name, s.surname, ROUND(AVG(g.grade), 2) as average_grade
FROM students s
JOIN grades g ON s.student_id = g.student_id
GROUP BY s.student_id, s.name, s.surname
ORDER BY average_grade DESC
LIMIT 5;