###################################################
#Purpose: Contains unit tests for the user-related API endpoints and CRUD operations.
#How it works:
#   Tests routes such as POST /users, GET /users/{id}, etc.
#   Uses FastAPI's TestClient for simulating requests to the API and asserting expected results.
###################################################


def test_register_user(client):
    response = client.post("/users/register", json={"username": "testuser", "password": "password123"})
    assert response.status_code == 200

def test_login_user(client):
    response = client.post("/users/login", data={"username": "testuser", "password": "password123"})
    assert response.status_code == 200
