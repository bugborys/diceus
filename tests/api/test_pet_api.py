import pytest
import requests

BASE_URL = "https://petstore.swagger.io/v2/pet"


class TestPetStoreAPI:

    @pytest.fixture
    def pet_data(self):
        return {
            "id": 123456789,
            "name": "MySuperPEt",
            "photoUrls": ["https://example.com/mysuperpet.jpg"],
            "status": "available"
        }

    # C
    def test_create_pet(self, pet_data):
        response = requests.post(BASE_URL, json=pet_data)
        assert response.status_code == 200
        assert response.json()["name"] == pet_data["name"]

    # R
    def test_get_pet(self, pet_data):
        requests.post(BASE_URL, json=pet_data)
        response = requests.get(f"{BASE_URL}/{pet_data['id']}")
        assert response.status_code == 200
        assert response.json()["id"] == pet_data["id"]

    # U
    def test_update_pet(self, pet_data):
        requests.post(BASE_URL, json=pet_data)
        pet_data["name"] = "Santa"
        pet_data["status"] = "unavailable"
        response = requests.put(BASE_URL, json=pet_data)
        assert response.status_code == 200
        assert response.json()["name"] == "Santa"
        assert response.json()["status"] == "unavailable"

    #D
    def test_delete_pet(self, pet_data):
        requests.post(BASE_URL, json=pet_data)
        response = requests.delete(f"{BASE_URL}/{pet_data['id']}")
        assert response.status_code == 200

    def test_get_deleted_pet_returns_404(self, pet_data):
        requests.post(BASE_URL, json=pet_data)
        requests.delete(f"{BASE_URL}/{pet_data['id']}")
        response = requests.get(f"{BASE_URL}/{pet_data['id']}")
        assert response.status_code == 404

    def test_create_pet_with_invalid_body(self):
        response = requests.post(BASE_URL, data="some incorrect data")
        assert response.status_code in [415, 500]

    def test_get_pet_with_invalid_id(self):
        response = requests.get(f"{BASE_URL}/some_invalid_id")
        assert response.status_code == 404

    def test_delete_pet_with_nonexistent_id(self):
        response = requests.delete(f"{BASE_URL}/9999999999999")
        assert response.status_code in [404, 200]
