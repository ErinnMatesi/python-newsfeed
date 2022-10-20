from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

# connect to database using env variable
# engine manages the overall connection to the database
engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)
#Session generates temporary connections for CRUD operations
Session = sessionmaker(bind=engine)
#Base maps the models to the MySQL tables
Base = declarative_base()