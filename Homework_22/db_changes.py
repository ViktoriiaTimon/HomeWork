
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from HomeWork.Homework_22.tables_configuration import Base, F_Student, F_Courses
from faker import Faker
import random

DATABASE_URL = "postgresql://vik:vik@localhost:5432/vika_db"
engine = create_engine(DATABASE_URL)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Filter Students of foreign_students table

one_student = session.query(F_Student).filter_by(id=20).first()
if one_student:
    print(f'ID: {one_student.id}, Name: {one_student.name}, Course: {one_student.course_name}')
else:
    print(f'Student with this ID was not found')
session.commit()

# Group of the students

group_user = session.query(F_Student).filter(F_Student.id<=20).all()
session.commit()
for user in group_user:
    print(f'ID: {user.id}, Name: {user.name}, Course: {user.course_name}')


# Add new student

eng_course = session.query(F_Courses).filter_by(course='Ukrainian').all()[0]
new_student = F_Student(name='Bob Moss', course_name=eng_course.course)
session.add(new_student)
session.commit()
print(f'The new student is added to the table: ID: {new_student.id}, Name: {new_student.name}, Course: {new_student.course_name}')


# Update student data

student_for_update = session.query(F_Student).filter_by(name='Tom Mile').first()
student_for_update.course_name = 'Ukrainian'
session.commit()
print(f'The student data is updated: ID: {student_for_update.id}, Name: {student_for_update.name}, Course: {student_for_update.course_name}')


#Delete student

student_to_delete = session.query(F_Student).filter_by(id=21).first()
if student_to_delete:
    session.delete(student_to_delete)
    session.commit()
    print(f'The student ID is deleted')
else:
    print(f'The student ID is not found. Perhaps, it was deleted from the table')
session.close()