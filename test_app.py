import requests

BASE_URL = "http://127.0.0.1:5000/format" 

def test_uppercase():
    response = requests.post(BASE_URL, json={"text": "hello", "mode": "upper"})
    assert response.status_code == 200
    assert response.json() == {"formatted_text": "HELLO"}

def test_lowercase():
    response = requests.post(BASE_URL, json={"text": "HELLO", "mode": "lower"})
    assert response.status_code == 200
    assert response.json() == {"formatted_text": "hello"}

def test_capitalize():
    response = requests.post(BASE_URL, json={"text": "hello world", "mode": "capitalize"})
    assert response.status_code == 200
    assert response.json() == {"formatted_text": "Hello world"}

def test_invalid_mode():
    response = requests.post(BASE_URL, json={"text": "hello", "mode": "unknown"})
    assert response.status_code == 400
    assert "error" in response.json()

def test_missing_text():
    response = requests.post(BASE_URL, json={"mode": "upper"})
    assert response.status_code == 400
    assert "error" in response.json()

if __name__ == "__main__":
    test_uppercase()
    test_lowercase()
    test_capitalize()
    test_invalid_mode()
    test_missing_text()
    print("усе тесты пройдены успешно!")
