from sqlalchemy import Column, Integer, String, ForeignKey
from databases.setup import Base

class Grade(Base):
  __tablename__ = "grades"
  id = Column(Integer, primary_key=True)
  student_id = Column(Integer, ForeignKey("students.id"))
  course_id = Column(Integer, ForeignKey("courses.id"))
  grade = Column(String)
 
  def __repr__(self):
        return f"<Grade(id={self.id}, student_id={self.student_id}, course_id={self.course_id}, grade_value={self.grade_value})>"
