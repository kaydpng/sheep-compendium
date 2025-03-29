from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_sheep():
    response = client.get("/sheep/1")

    assert response.status_code == 200

    assert response.json() == {
        "id": 1,
        "name": "Spice",
        "breed": "Gotland",
        "sex": "ewe"
    }


def test_add_sheep():
    sheep_data = {
        "id": 8,
        "name": "Steve",
        "breed": "sheep",
        "sex": "ram"
    }

    sheep_upload = client.post("/sheep", json=sheep_data)

    assert sheep_upload.status_code == 201

    assert sheep_upload.json() == {
        "id": 8,
        "name": "Steve",
        "breed": "sheep",
        "sex": "ram"
    }

    new_sheep = client.get("/sheep/8")

    assert new_sheep.status_code == 200


def test_delete_sheep():
    response = client.delete("/sheep/6")

    assert response.status_code == 204
    assert client.get("/sheep/6").status_code == 404


def test_update_sheep():
    new_sheep_data = {
        "id": 5,
        "name": "Kayd",
        "breed": "sheep",
        "sex": "ewe"
    }

    response = client.put("/sheep/5", json=new_sheep_data)

    new_sheep = client.get("/sheep/5")

    assert new_sheep.json() == new_sheep_data
    assert response.status_code == 200


def test_read_all():
    all_sheep = client.get("/sheep").json()

    data = [
        {
            "breed": "Gotland",
            "id": 1,
            "name": "Spice",
            "sex": "ewe"
        },
        {
            "breed": "Polypay",
            "id": 2,
            "name": "Blondie",
            "sex": "ram"
        },
        {
            "breed": "Jacobs Four Horns",
            "id": 3,
            "name": "Deedee",
            "sex": "ram"
        },
        {
            "breed": "Romney",
            "id": 4,
            "name": "Rommy",
            "sex": "ewe"
        },
        {
            "breed": "sheep",
            "id": 5,
            "name": "Kayd",
            "sex": "ewe"
        },
        {
            "breed": "sheep",
            "id": 8,
            "name": "Steve",
            "sex": "ram"}

    ]

    assert data == all_sheep

    response = client.get("/sheep")
    assert response.status_code == 200
