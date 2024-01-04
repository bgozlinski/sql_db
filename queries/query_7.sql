--Oceny uczniów w wybranej grupie z określonego przedmiotu.
SELECT s.student_id, s.name, s.surname, g.grade
FROM students s
JOIN grades g ON s.student_id = g.student_id
WHERE s.group_id = 1 AND g.subject_id = 1;
