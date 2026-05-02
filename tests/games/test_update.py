from http import HTTPStatus
import pytest

def test_update_game_success(db_with_one_game, api_path):
    game_id = 1
    update_payload = {"title": "Hades II", "hours_played": 150}

    response = db_with_one_game.patch(f"{api_path}/{game_id}", json=update_payload)
    data = response.json()

    assert response.status_code == HTTPStatus.OK
    assert data["title"] == "Hades II"
    assert data["hours_played"] == 150
    assert data["id"] == game_id

@pytest.mark.parametrize("payload, expected_status", [
    (
        {"title": ""},
        HTTPStatus.UNPROCESSABLE_ENTITY
    ),
    (
        {"hours_played": -10},
        HTTPStatus.UNPROCESSABLE_ENTITY
    ),
    (
        {"title": "   "},
        HTTPStatus.UNPROCESSABLE_ENTITY
    ),
])
def test_update_game_invalid_data(db_with_one_game, api_path, payload, expected_status):
    game_id = 1
    response = db_with_one_game.patch(f"{api_path}/{game_id}", json=payload)

    assert response.status_code == expected_status

def test_update_game_not_found(client, api_path):
    payload = {"title": "Novo Nome"}
    response = client.patch(f"{api_path}/999", json=payload)

    assert response.status_code == HTTPStatus.NOT_FOUND

