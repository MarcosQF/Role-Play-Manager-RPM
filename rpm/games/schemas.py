from pydantic import field_validator
from sqlmodel import Field, SQLModel

from rpm.games.enums import GamePlatform, GameStatus


class GameCreate(SQLModel):
    title: str = Field(min_length=1, max_length=100)
    status: GameStatus
    platform: GamePlatform
    hours_played: int = Field(default=0, ge=0)
    summary: str | None = Field(default=None, max_length=500)

    @field_validator('title', mode='before')
    @classmethod
    def str_strip_whitespace(cls, v: str) -> str:
        return v.strip()


class GameUpdate(SQLModel):
    title: str | None = Field(default=None, min_length=1, max_length=100)
    status: GameStatus | None = None
    platform: GamePlatform | None = None
    hours_played: int | None = Field(default=None, ge=0)
    summary: str | None = Field(default=None, max_length=500)

    @field_validator('title', mode='before')
    @classmethod
    def str_strip_whitespace(cls, v: str | None) -> str | None:
        if isinstance(v, str):
            return v.strip()
        return v


class GameResponse(GameCreate):
    id: int


class GameResponseList(SQLModel):
    games: list[GameResponse]
