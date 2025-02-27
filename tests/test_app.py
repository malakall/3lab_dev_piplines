import pytest
from src.app import app  # Импортируем Flask-приложение из основного файла


@pytest.fixture
def client():
    """Создаем тестовый клиент Flask."""
    with app.test_client() as client:
        yield client


def test_uppercase(client):
    response = client.post("/format", json={"text": "hello", "mode": "upper"})
    assert response.status_code == 200
    assert response.json == {"formatted_text": "HELLO"}


def test_lowercase(client):
    response = client.post("/format", json={"text": "HELLO", "mode": "lower"})
    assert response.status_code == 200
    assert response.json == {"formatted_text": "hello"}


def test_capitalize(client):
    response = client.post(
        "/format",
        json={
            "text": "hello world",
            "mode": "capitalize"})
    assert response.status_code == 200
    assert response.json == {"formatted_text": "Hello world"}


def test_invalid_mode(client):
    response = client.post(
        "/format",
        json={
            "text": "hello",
            "mode": "unknown"})
    assert response.status_code == 400
    assert "error" in response.json


def test_missing_text(client):
    response = client.post("/format", json={"mode": "upper"})
    assert response.status_code == 400
    assert "error" in response.json


if __name__ == "__main__":
    pytest.main()
