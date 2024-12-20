from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from HomeWork.Homework_22.tables_configuration import Base, F_Student, F_Courses
from faker import Faker
import random

DATABASE_URL = "postgresql://vik:vik@localhost:5432/vika_db"
engine = create_engine(DATABASE_URL)

if __name__ == '__main__':

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    course_1 = F_Courses(course='English', hours=40)
    course_2 = F_Courses(course='French', hours=50)
    course_3 = F_Courses(course='Spanish', hours=30)
    course_4 = F_Courses(course='Polish', hours=20)
    course_5 = F_Courses(course='Ukrainian', hours=55)

    all_courses = [course_1, course_2, course_3, course_4, course_5]
    session.add_all(all_courses)
    session.commit()

    fake = Faker()
    students = []
    for k in range(20):
        student_name = fake.unique.name()
        assigned_courses = random.sample(all_courses, k=random.randint(1, 3))
        student = F_Student(name=student_name, courses=assigned_courses)
        session.add(student)

    session.add_all(students)

    for student in session.query(F_Student).all():
        if student.courses:
            student.course_name = ", ".join(course.course for course in student.courses)
#
    session.commit()

    print("Data added successfully!")

# student_name = fake.unique.name()
# available_courses = session.query(F_Courses).all()
# if not available_courses:
#     raise ValueError("No courses found in the database")
# assigned_courses = random.sample(available_courses, k=random.randint(1, 3))
# new_user = F_Student(name=student_name, courses=assigned_courses)
# session.add(new_user)
# session.commit()
# print(new_user.name, [course.course_name for course in new_user.courses])
# session.close()