import requests
import pytest

TOKEN = "y0__wgBEKrJvMIDGPC4QSDroOStFyQTRdLE3lS8hql7KgSjvK599prK"
BASE_URL = "https://cloud-api.yandex.net/v1/disk/resources"
HEADERS = {
    "Authorization": f"OAuth {TOKEN}",
    "Content-Type": "application/json"
}


class TestYandexDiskAPI:

    created_folders = []

    def teardown_method(self):
        for folder in self.created_folders:
            requests.delete(f"{BASE_URL}?path={folder}", headers=HEADERS)
        self.created_folders.clear()

    def test_create_folder_success(self):
        folder_name = "TestFolder"

        response = requests.put(f"{BASE_URL}?path={folder_name}", headers=HEADERS)
        assert response.status_code == 201
        self.created_folders.append(folder_name)

        check_response = requests.get(f"{BASE_URL}?path=/", headers=HEADERS)
        items = check_response.json().get("_embedded", {}).get("items", [])
        folder_names = [item["name"] for item in items if item["type"] == "dir"]

        assert folder_name in folder_names

    @pytest.mark.parametrize("folder_name, expected_status", (
        ("TestFolder", 409),
    ))
    def test_create_folder_duplicate(self, folder_name, expected_status):

        requests.put(f"{BASE_URL}?path={folder_name}", headers=HEADERS)
        self.created_folders.append(folder_name)

        response = requests.put(f"{BASE_URL}?path={folder_name}", headers=HEADERS)
        assert response.status_code == expected_status

    def test_create_folder_unauthorized(self):

        bad_headers = {"Authorization": "OAuth BAD_TOKEN"}
        response = requests.put(f"{BASE_URL}?path=SecretFolder", headers=bad_headers)

        assert response.status_code == 401

    @pytest.mark.parametrize("invalid_path", ["", "   ", "???"])
    def test_create_folder_invalid_name(self, invalid_path):
        response = requests.put(f"{BASE_URL}?path={invalid_path}", headers=HEADERS)
        assert response.status_code in [400, 404, 409]