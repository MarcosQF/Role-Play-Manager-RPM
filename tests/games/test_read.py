from http import HTTPStatus

def test_read_empty_games(client, api_path):
    response = client.get(api_path)

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"games": []}

def test_read_one_game(db_with_one_game, api_path):
    response = db_with_one_game.get(api_path)
    data = response.json()

    assert response.status_code == HTTPStatus.OK
    assert len(data["games"]) == 1

def test_read_multiple_games(db_with_multiple_games, api_path):
    response = db_with_multiple_games.get(api_path)
    data = response.json()

    assert response.status_code == HTTPStatus.OK
    assert len(data["games"]) == 2

def test_read_game_by_id(db_with_one_game, api_path, sample_game):
    game_id = 1
    response = db_with_one_game.get(f"{api_path}/{game_id}")
    data = response.json()

    assert response.status_code == HTTPStatus.OK
    assert data["title"] == sample_game["title"]
    assert data["id"] == game_id

def test_read_game_not_found(client, api_path):
    response = client.get(f"{api_path}/999")
    assert response.status_code == HTTPStatus.NOT_FOUND
