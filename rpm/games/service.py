from typing import Annotated

from fastapi import Depends
from sqlmodel import Session, select

from rpm.core.database import get_session
from rpm.core.errors import NotFoundException
from rpm.games.model import Game
from rpm.games.schemas import GameCreate, GameUpdate


class GamesService:
    def __init__(self, session: Session):
        self.session = session

    def create_game(self, game_data: GameCreate) -> Game:
        db_game = Game.model_validate(game_data)
        self.session.add(db_game)
        self.session.commit()
        self.session.refresh(db_game)
        return db_game

    def get_games(self, offset: int = 0, limit: int = 100):
        games = self.session.scalars(
            select(Game).offset(offset).limit(limit)
        ).all()
        return games

    def get_game_by_id(self, game_id: int) -> Game:
        statement = select(Game).where(Game.id == game_id)
        game = self.session.scalar(statement)

        if not game:
            raise NotFoundException(entity=Game, entity_id=game_id)
        return game

    def update_game(self, game_id: int, game_data: GameUpdate) -> Game:
        db_game = self.get_game_by_id(game_id)
        update_data = game_data.model_dump(exclude_unset=True)
        db_game.sqlmodel_update(update_data)

        self.session.add(db_game)
        self.session.commit()
        self.session.refresh(db_game)
        return db_game

    def delete_game(self, game_id: int) -> None:
        db_game = self.get_game_by_id(game_id)
        self.session.delete(db_game)
        self.session.commit()


def get_game_service(session: Session = Depends(get_session)):
    return GamesService(session)


T_GameService = Annotated[GamesService, Depends(get_game_service)]
