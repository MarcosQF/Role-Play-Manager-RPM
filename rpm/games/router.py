from http import HTTPStatus

from fastapi import APIRouter

from rpm.games.schemas import (
    GameCreate,
    GameResponse,
    GameResponseList,
    GameUpdate,
)
from rpm.games.service import T_GameService

router = APIRouter(prefix='/games', tags=['Games'])


@router.post('/', response_model=GameResponse, status_code=HTTPStatus.CREATED)
def create_game(game_data: GameCreate, service: T_GameService):
    """Cria um novo jogo no catálogo."""
    return service.create_game(game_data)


@router.get('/', response_model=GameResponseList, status_code=HTTPStatus.OK)
def list_games(service: T_GameService, offset: int = 0, limit: int = 100):
    """Lista os jogos com suporte a paginação."""
    games = service.get_games(offset, limit)
    return {'games': games}


@router.get(
    '/{game_id}', response_model=GameResponse, status_code=HTTPStatus.OK
)
def read_game(game_id: int, service: T_GameService):
    """Busca os detalhes de um jogo específico."""
    return service.get_game_by_id(game_id)


@router.patch(
    '/{game_id}', response_model=GameResponse, status_code=HTTPStatus.OK
)
def update_game(game_id: int, game_data: GameUpdate, service: T_GameService):
    """Atualiza campos específicos de um jogo."""
    return service.update_game(game_id, game_data)


@router.delete('/{game_id}', status_code=HTTPStatus.NO_CONTENT)
def delete_game(game_id: int, service: T_GameService):
    """Remove um jogo permanentemente."""
    service.delete_game(game_id)
