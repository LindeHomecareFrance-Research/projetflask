from dataclasses import dataclass
from app import db
from sqlalchemy import  Integer,String

@dataclass
class User(db.Model):
    id: int
    name: str
    
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(255))