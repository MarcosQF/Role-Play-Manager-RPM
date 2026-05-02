import pytest

@pytest.fixture(scope="module")
def api_path():
    return "/api/games"

@pytest.fixture
def sample_game():
    return {
        "title": "Hades",
        "status": "Backlog",
        "platform": "Steam",
        "hours_played": 100
    }

@pytest.fixture
def other_game():
    return {
        "title": "Besiege",
        "status": "Completed",
        "platform": "Steam",
        "hours_played": 50
    }

@pytest.fixture
def db_with_one_game(client, api_path, sample_game):
    client.post(api_path, json=sample_game)
    return client

@pytest.fixture
def db_with_multiple_games(client, api_path, sample_game, other_game):
    client.post(api_path, json=sample_game)
    client.post(api_path, json=other_game)
    return client
