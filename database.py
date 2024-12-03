from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE = "postgresql://greenhaven_user:kokf1ht3QVLf3UNihKqISjwzjki00I2I@dpg-ct7ked3qf0us73dp8140-a.oregon-postgres.render.com/greenhaven"

engine = create_engine(URL_DATABASE)

SessionLocate = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
