from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base
from faker import Faker
import random

DATABASE_URL = "postgresql://vik:vik@localhost:5432/vika_db"
engine = create_engine(DATABASE_URL)

Base = declarative_base()


class F_Courses(Base):
    __tablename__ = 'foreign_courses'

    id = Column(Integer, primary_key=True)
    course_name = Column(String, unique=True)
    hours = Column(Integer)


class F_Student(Base):
    __tablename__ = 'foreign_students'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    course_name = Column(String)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

courses = [
    F_Courses(course_name='English', hours=40),
    F_Courses(course_name='French', hours=50),
    F_Courses(course_name='Spanish', hours=30),
    F_Courses(course_name='Polish', hours=20),
    F_Courses(course_name='Ukrainian', hours=55)
]

session.add_all(courses)
session.commit()

fake = Faker()
students = []
for _ in range(20):
    student_name = fake.unique.name()
    assigned_courses = random.sample(courses, k=random.randint(1, 3))
    course_names = [course.course_name for course in assigned_courses]
    student = F_Student(name=student_name, course_name=', '.join(course_names))
    students.append(student)

session.add_all(students)
session.commit()

session.close()

