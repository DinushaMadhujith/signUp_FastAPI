from sqlalchemy import Column, Integer, String
from database import Base

class Signup(Base):
    __tablename__ = 'signup'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone_number = Column(String, nullable=False)
    type = Column(String, nullable=False)  # customer, labor, admin, deliver, farmer
    password = Column(String, nullable=False)  # Store hashed passwords in production
