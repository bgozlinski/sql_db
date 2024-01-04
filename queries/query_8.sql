--Średnia ocen wystawionych przez wykładowcę z danego przedmiotu.
SELECT l.lecturer_id, l.name, l.surname, sub.name as subject_name, ROUND(AVG(g.grade), 2) as average_grade
FROM lecturers l
JOIN subjects sub ON l.lecturer_id = sub.lecturer_id
JOIN grades g ON sub.subject_id = g.subject_id
WHERE l.lecturer_id = 1
GROUP BY l.lecturer_id, l.name, l.surname, sub.name
ORDER BY sub.name, average_grade DESC;
