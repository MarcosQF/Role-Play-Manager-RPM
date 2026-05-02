from http import HTTPStatus

def test_delete_game_success(db_with_one_game, api_path):
    game_id = 1
    response = db_with_one_game.delete(f"{api_path}/{game_id}")

    assert response.status_code == HTTPStatus.NO_CONTENT


def test_get_game_not_found_after_delete(db_with_one_game, api_path):
    game_id = 1
    db_with_one_game.delete(f"{api_path}/{game_id}")
    response = db_with_one_game.get(f"{api_path}/{game_id}")

    assert response.status_code == HTTPStatus.NOT_FOUND

def test_delete_game_not_found(client, api_path):
    response = client.delete(f"{api_path}/999")
    assert response.status_code == HTTPStatus.NOT_FOUND
