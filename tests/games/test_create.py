from http import HTTPStatus
import pytest

def test_create_game_success(client, sample_game, api_path):
    response = client.post(api_path, json=sample_game)
    data = response.json()

    assert response.status_code == HTTPStatus.CREATED
    assert sample_game.items() <= data.items()
    assert isinstance(data.get("id"), int)

@pytest.mark.parametrize("payload, expected_status", [
    (
        {"title": "", "platform": "PC"}, 
        HTTPStatus.UNPROCESSABLE_ENTITY
    ),
    (
        {"title": "Hades"},
        HTTPStatus.UNPROCESSABLE_ENTITY
    ),
])
def test_create_game_invalid_data(client, api_path, payload, expected_status):
    response = client.post(api_path, json=payload)
    assert response.status_code == expected_status
