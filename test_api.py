import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


# ✅ Test 1: GET users (status code)
def test_get_users_status():
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 200


# ✅ Test 2: Check response is not empty
def test_get_users_not_empty():
    response = requests.get(f"{BASE_URL}/users")
    data = response.json()
    assert len(data) > 0


# ✅ Test 3: Validate user structure
def test_user_structure():
    response = requests.get(f"{BASE_URL}/users/1")
    user = response.json()

    assert "id" in user
    assert "name" in user
    assert "email" in user


# ✅ Test 4: POST request (create user)
def test_create_user():
    payload = {
        "name": "Maksym",
        "email": "maksym@test.com"
    }

    response = requests.post(f"{BASE_URL}/users", json=payload)

    assert response.status_code == 201
    data = response.json()

    assert data["name"] == "Maksym"


# ❌ Test 5: Negative test (wrong endpoint)
def test_invalid_endpoint():
    response = requests.get(f"{BASE_URL}/invalid-endpoint")
    assert response.status_code == 404