from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, sessionmaker, declarative_base


Base = declarative_base()

engine = create_engine("sqlite:///school.db")
Session = sessionmaker(bind=engine)
session = Session()


student_courses = Table(
    'student_courses',
    Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
    Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
)

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)


    courses = relationship('Course', secondary=student_courses, back_populates='students')

class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    courses = relationship('Course', back_populates='teacher')


class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))

    teacher = relationship("Teacher", back_populates="courses")


    students = relationship('Student', secondary=student_courses, back_populates='courses')


class Assignment(Base):
    __tablename__ = 'assignments'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    course_id = Column(Integer, ForeignKey('courses.id'))


    course = relationship("Course")


Base.metadata.create_all(engine)




