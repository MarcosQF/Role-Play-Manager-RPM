from sqlmodel import SQLModel, Field

from rpm.games.enums import GamePlatform, GameStatus


class GameCreate(SQLModel):
    title: str
    status: GameStatus = Field(default=GameStatus.BACKLOG)
    platform: GamePlatform = Field(default=GamePlatform.OTHER)
    hours_played: int = Field(default=0)
    summary: str | None = None


class GameUpdate(SQLModel):
    title: str | None = None
    status: GameStatus | None = None
    platform: GamePlatform | None = None
    hours_played: int | None = None
    summary: str | None = None


class GameResponse(GameCreate):
    id: int


class GameResponseList(SQLModel):
    games: list[GameResponse]
