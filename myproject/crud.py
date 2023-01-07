from sqlalchemy.orm import Session

import models
import schemas
import auth


def get_player(db: Session, player_id: int):
    return db.query(models.Player).filter(models.Player.id == player_id).first()


def get_player_by_name(db: Session, name: str):
    db_player = db.query(models.Player).filter(models.Player.name == name).first()
    return db_player


def get_players(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Player).offset(skip).limit(limit).all()


def create_player(db: Session, player: schemas.PlayerCreate):
    hashed_password = auth.get_password_hash(player.password)
    db_player = models.Player(name=player.name, nationality=player.nationality, stat_id=player.stat_id, opening_id=player.opening_id, password=hashed_password)
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player


def get_stat(db: Session, stat_id: int):
    return db.query(models.Stat).filter(models.Stat.id == stat_id).first()

#def update_stat_wins(db: Session, stat_id: int, new_wins):
#    db_stat = db.query(models.Stat).filter(models.Stat.id == stat_id).first()

def create_player_stat(db: Session, stat: schemas.StatCreate):
    db_stat = models.Stat(rank=stat.rank, games=stat.games, wins=stat.wins, losses=stat.losses, draws=stat.draws)
    db.add(db_stat)
    db.commit()
    db.refresh(db_stat)
    return db_stat

def get_opener(db: Session, opener_id: int):
    return db.query(models.Opener).filter(models.Opener.id == opener_id).first()

def get_opener_by_name(db: Session, name: str):
    return db.query(models.Opener).filter(models.Opener.name == name).first()

def create_opener(db: Session, opener: schemas.OpenerCreate):
    db_opener = models.Opener(name=opener.name)
    db.add(db_opener)
    db.commit()
    db.refresh(db_opener)
    return db_opener

def delete_opener(db: Session, opener_id: int):
    db_opener = db.query(models.Opener).filter(models.Opener.id == opener_id).first()
    db.delete(db_opener)
    db.commit()
    db.refresh(db_opener)
    return db_opener

