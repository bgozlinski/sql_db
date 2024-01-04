--Lista kursów, na które uczęszcza uczeń.
SELECT DISTINCT sub.subject_id, sub.name
FROM subjects sub
JOIN grades g ON sub.subject_id = g.subject_id
WHERE g.student_id = 2;

