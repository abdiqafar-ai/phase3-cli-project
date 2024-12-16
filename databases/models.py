from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()
engine = create_engine("sqlite:///school.db")
Session = sessionmaker(bind=engine)
session = Session()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)

class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))
    teacher = relationship("Teacher")

class Assignment(Base):
    __tablename__ = 'assignments'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    course_id = Column(Integer, ForeignKey('courses.id'))
    course = relationship("Course")
