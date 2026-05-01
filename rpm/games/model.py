from sqlmodel import SQLModel, Field
from .enums import GameStatus, GamePlatform


class Game(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    status: GameStatus = Field(default=GameStatus.BACKLOG)
    platform: GamePlatform = Field(default=GamePlatform.OTHER)
    hours_played: int = Field(default=0)
    summary: str | None = None
