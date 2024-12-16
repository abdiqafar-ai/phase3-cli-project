from sqlalchemy import Column, Integer,String,ForeignKey
from sqlalchemy.orm import relationship, Session
from databases.setup import Base

class Course(Base):
  __tablename__ = "courses"

  id = Column(Integer, primary_key=True)
  course_name = Column(String)
  description = Column(String)
  teacher_id = Column(Integer, ForeignKey("teachers.id"))

  teacher = relationship("Teacher", back_populates="courses")

  def __repr__(self):
    return f"< Course(id={self.id}, course_name={self.course_name}, description={self.description}, teacher_id={self.teacher_id})>"