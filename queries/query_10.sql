--Lista kursów prowadzonych przez wybranego wykładowcę dla określonego ucznia.
SELECT DISTINCT sub.subject_id, sub.name
FROM subjects sub
JOIN grades g ON sub.subject_id = g.subject_id
WHERE g.student_id = 1 AND sub.lecturer_id = 1;
