###################################################
#Purpose: Contains unit tests for the book-related API endpoints and CRUD operations (similar to test_users.py).
#How it works:
#   Similar structure as test_users.py, but focused on the books routes.
###################################################


def test_create_book(client, token):
    response = client.post(
        "/books",
        json={"title": "Test Book", "author": "Author", "description": "Description"},
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
