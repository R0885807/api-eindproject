from database import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    nationality = Column(String, index=True)
    stat_id = Column(Integer, ForeignKey("stats.id"))
    opening_id = Column(Integer, ForeignKey("openers.id"))
    password = Column(String)


    stat = relationship("Stat", back_populates="player_stat")
    opener = relationship("Opener", back_populates="player_opener")
class Stat(Base):
    __tablename__ = "stats"

    id = Column(Integer, primary_key=True, index=True)
    rank = Column(Integer,index=True)
    games = Column(Integer, index=True)
    wins = Column(Integer, index=True)
    losses = Column(Integer, index=True)
    draws = Column(Integer, index=True)


    player_stat = relationship("Player", back_populates="stat")

class Opener(Base):
    __tablename__ = "openers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    player_opener = relationship("Player", back_populates="opener")
