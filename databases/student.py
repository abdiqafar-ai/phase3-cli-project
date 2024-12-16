from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
from databases.setup import Base

class Student(Base):
  __tablename__ = "Students"

  id = Column(Integer, primary_key=True)
  first_name = Column(String)
  last_name = Column(String)
  email = Column(String, unique=True)

  def __repr__(self):
    return  f"<Student(id={self.id}, first_name={self.first_name}, last_name={self.last_name}, email={self.email})>"