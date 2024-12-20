#db_connection
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

student_courses = Table('student_courses', Base.metadata,
    Column('foreign_students_id', Integer, ForeignKey('foreign_students.id'), primary_key=True),
    Column('foreign_courses_id', Integer, ForeignKey('foreign_courses.id'), primary_key=True))

class F_Student(Base):
    __tablename__ = 'foreign_students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True)
    course_name = Column(String)
    courses = relationship('F_Courses', secondary=student_courses, back_populates='students')


class F_Courses(Base):
    __tablename__ = 'foreign_courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    course = Column(String, unique=True)
    hours = Column(Integer)
    students = relationship('F_Student', secondary=student_courses, back_populates='courses')