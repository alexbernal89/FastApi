from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# SQLAlchemy database URl en render
#SQLALCHEMY_DATABASE_URL = 'postgresql://database_c7cy_user:sAdHev0baTEDmOa0gVGmRKLb8jqBeSUh@dpg-d1bet40dl3ps73eknjvg-a/database_c7cy'
#local
SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:postgres!@localhost:5432/TodoApplicationDatabase'

# MySQL database URL (uncomment if using MySQL)
#SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:AlexBM1@127.0.0.1:3306/todoapplicationdatabase'


engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
