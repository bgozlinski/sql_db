import random
from faker import Faker
from connect import PostgresDB

fake = Faker('pl_PL')


def create_groups(db, cursor):
    group_names = ["SM01", "SM02", "SM03"]
    for group_name in group_names:
        cursor.execute("INSERT INTO groups (group_name) VALUES (%s)", (group_name,))
    db.conn.commit()


def create_students(db, cursor, num_students=50):
    for _ in range(num_students):
        name = fake.first_name()
        surname = fake.last_name()
        group_id = random.randint(1, 3)
        cursor.execute("INSERT INTO students (name, surname, group_id) VALUES (%s, %s, %s)", (name, surname, group_id))
    db.conn.commit()


def create_lecturers(db, cursor, num_lecturers=5):
    for _ in range(num_lecturers):
        name = fake.first_name()
        surname = fake.last_name()
        cursor.execute("INSERT INTO lecturers (name, surname) VALUES (%s, %s)", (name, surname))
    db.conn.commit()

def create_subjects(db, cursor):
    subjects = ["Analiza Matematyczna", "Algebra", "Geometria Wykreślna", "Informatyka", "Wychowanie Fizyczne",
                "Filozofia", "Ekonomia"]
    for name in subjects:
        lecturer_id = random.randint(1, 5)
        cursor.execute("INSERT INTO subjects (name, lecturer_id) VALUES (%s, %s)", (name, lecturer_id))
    db.conn.commit()


def create_grades(db, cursor, num_students=50, num_subjects=7, num_grades_per_student=20):
    grades = [2, 2.5, 3, 3.5, 4, 4.5, 5]
    for student_id in range(1, num_students + 1):
        for _ in range(num_grades_per_student):
            subject_id = random.randint(1, num_subjects)
            grade = random.choice(grades)
            date = fake.date()
            cursor.execute("INSERT INTO grades (student_id, subject_id, grade, date) VALUES (%s, %s, %s, %s)",
                           (student_id, subject_id, grade, date))
    db.conn.commit()


if __name__ == '__main__':
    db = PostgresDB()
    db.connect()

    cursor = db.conn.cursor()

    create_groups(db, cursor)
    create_students(db, cursor)
    create_lecturers(db, cursor)
    create_subjects(db, cursor)
    create_grades(db, cursor)

    cursor.close()
    db.close()
