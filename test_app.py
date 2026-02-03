
from app import app

def test_home():
    client=app.text_client()
    response=client.get("/")
    assert response.status_code==200
