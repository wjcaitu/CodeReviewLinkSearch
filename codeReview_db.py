from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
  
import settings

DeclarativeBase = declarative_base()
  
def db_connect():
	return create_engine(URL(**settings.DATABASE))
  
def create_code_review_link_table(engine):
    DeclarativeBase.metadata.create_all(engine)
  
class CodeReviewDb(DeclarativeBase):
    __tablename__ = "cr"
  
    id = Column(Integer, primary_key=True)
    title = Column('link', String(200))
    link = Column('desc', String(200))