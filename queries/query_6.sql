--Lista uczniów w wybranej grupie.
SELECT s.student_id, s.name, s.surname
FROM students s
WHERE s.group_id = 1;