import pytest
import requests

BASE_URL = "https://petstore.swagger.io/v2/pet"


class TestPetStoreAPI:

    @pytest.fixture
    def pet_data(self):
        return {
            "id": 123456789,
            "name": "Sirko",
            "photoUrls": ["https://example.com/sirko.jpg"],
            "status": "available"
        }

    @pytest.mark.api
    def test_create_pet(self, pet_data):
        response = requests.post(BASE_URL, json=pet_data)
        assert response.status_code == 200
        assert response.json()["name"] == pet_data["name"]

    @pytest.mark.api
    def test_get_pet(self, pet_data):
        requests.post(BASE_URL, json=pet_data)
        response = requests.get(f"{BASE_URL}/{pet_data['id']}")
        assert response.status_code == 200
        assert response.json()["id"] == pet_data["id"]

    @pytest.mark.api
    def test_update_pet(self, pet_data):
        requests.post(BASE_URL, json=pet_data)
        pet_data["name"] = "Bulat"
        pet_data["status"] = "sold"
        response = requests.put(BASE_URL, json=pet_data)
        assert response.status_code == 200
        assert response.json()["name"] == "Bulat"
        assert response.json()["status"] == "sold"

    @pytest.mark.api
    def test_delete_pet(self, pet_data):
        requests.post(BASE_URL, json=pet_data)
        response = requests.delete(f"{BASE_URL}/{pet_data['id']}")
        assert response.status_code == 200

    @pytest.mark.api
    @pytest.mark.negative
    def test_get_deleted_pet_returns_404(self, pet_data):
        requests.post(BASE_URL, json=pet_data)
        requests.delete(f"{BASE_URL}/{pet_data['id']}")
        response = requests.get(f"{BASE_URL}/{pet_data['id']}")
        assert response.status_code == 404

    @pytest.mark.api
    @pytest.mark.negative
    def test_create_pet_with_invalid_body(self):
        response = requests.post(BASE_URL, data="not a json")
        assert response.status_code in [400, 415, 500]

    @pytest.mark.api
    @pytest.mark.negative
    def test_get_pet_with_invalid_id(self):
        response = requests.get(f"{BASE_URL}/invalid_id")
        assert response.status_code == 404

    @pytest.mark.api
    @pytest.mark.negative
    def test_delete_pet_with_nonexistent_id(self):
        response = requests.delete(f"{BASE_URL}/9999999999999")
        assert response.status_code in [404, 200]
