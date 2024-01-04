--Przedmioty, które prowadzi wybrany wykładowca.
SELECT sub.subject_id, sub.name
FROM subjects sub
WHERE sub.lecturer_id = 1;