from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///.blog.db"

engine = create_engine(DATABASE_URL,connect_args ={"check_same_thread":False})

Sessionlocal=sessionmaker(autocommit = False, autoflush= False,bind = engine)

Base = declarative_base()

def get_db():
    db = Sessionlocal()
    try:
        yield db
    except:
        print("error")
    finally:
        db.close()