from pydantic import BaseModel


class StatBase(BaseModel):
    rank: int
    games: int
    wins: int
    losses: int
    draws: int


class StatCreate(StatBase):
    pass


class Stat(StatBase):
    id: int

    class Config:
        orm_mode = True

class OpenerBase(BaseModel):
    name: str


class OpenerCreate(OpenerBase):
    pass


class Opener(OpenerBase):
    id: int

    class Config:
        orm_mode = True


class PlayerBase(BaseModel):
    name: str
    nationality: str
    stat_id: int
    opening_id: int
    password: str

class PlayerCreate(PlayerBase):
    pass


class Player(PlayerBase):
    id: int


    class Config:
        orm_mode = True
