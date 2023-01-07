from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from database import SessionLocal, engine


import crud
import models
import schemas
import auth
import os
import secrets

if not os.path.exists('.\sqlitedb'):
    os.makedirs('.\sqlitedb')

#"sqlite:///./sqlitedb/sqlitedata.db"
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

security = HTTPBasic()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    player = auth.authenticate_player(db, form_data.username, form_data.password)
    if not player:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = auth.create_access_token(
        data={"sub": player.name}
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/player/{player_id}", response_model=schemas.Player)
def read_player(player_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    db_player = crud.get_player(db, player_id=player_id)
    if db_player is None:
        raise HTTPException(status_code=404, detail="Player not found")
    return db_player


@app.get("/players/", response_model=list[schemas.Player])
def read_players(skip: int = 0, limit: int = 5, db: Session = Depends(get_db)):
    players = crud.get_players(db, skip=skip, limit=limit)
    return players


@app.post("/player/", response_model=schemas.Player)
def create_player(player: schemas.PlayerCreate, db: Session = Depends(get_db)):
    db_player = crud.get_player_by_name(db, name=player.name)
    if db_player:
        raise HTTPException(status_code=400, detail="Player already exists")
    return crud.create_player(db=db, player=player)



@app.get("/opener/{opener_id}", response_model=schemas.Opener)
def read_opener(opener_id: int, db: Session = Depends(get_db)):
    db_opener = crud.get_opener(db, opener_id=opener_id)
    if db_opener is None:
        raise HTTPException(status_code=404, detail="Opener not found")
    return db_opener

@app.put("/opener/", response_model=schemas.Opener)
def create_opener(opener: schemas.OpenerCreate, db: Session = Depends(get_db)):
    db_opener = crud.get_opener_by_name(db, name=opener.name)
    if db_opener:
        raise HTTPException(status_code=400, detail="Opener already exists")
    return crud.create_opener(db=db, opener=opener)


@app.delete("/opener/{opener_id}", response_model=schemas.Opener)
def delete_opener(opener_id: int, db: Session = Depends(get_db)):
    db_opener = crud.get_opener(db, opener_id=opener_id)
    if db_opener is None:
        raise HTTPException(status_code=404, detail="Opener not found")
    db.delete(db_opener)
    db.commit()
    db.refresh(db_opener)
    return {"ok": True}


@app.get("/stat/", response_model=schemas.Stat)
def read_stat(stat_id: int, db: Session = Depends(get_db)):
    db_stat = crud.get_stat(db, stat_id=stat_id)
    if db_stat is None:
        raise HTTPException(status_code=404, detail="Stat not found")
    return db_stat


@app.post("/stat/", response_model=schemas.Stat)
def create_stat(stat: schemas.StatCreate, db: Session = Depends(get_db)):
    return crud.create_player_stat(db=db, stat=stat)