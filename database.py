from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE = "postgresql://greenhaven_wvym_user:DBMRGKCTHctAsqECEwyxi2t6O5VGLZgZ@dpg-cuabmh1u0jms73fn6pp0-a.oregon-postgres.render.com/greenhaven_wvym"


engine = create_engine(URL_DATABASE)

SessionLocate = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
