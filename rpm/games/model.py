from sqlmodel import Field, SQLModel

from .enums import GamePlatform, GameStatus


class Game(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    status: GameStatus = Field(default=GameStatus.BACKLOG)
    platform: GamePlatform = Field(default=GamePlatform.OTHER)
    hours_played: int = Field(default=0)
    summary: str | None = None
