from unittest.mock import mock_open, patch

from api.items_api import ItemsResource


class TestItemsResource:
    url = "/v1/item"
    model = ItemsResource

    def test_generate_random_alphabet_strings(self):
        generated_random_string = self.model._generate_random_alphabet_strings()
        assert generated_random_string.isalpha() is True

    def test_generate_random_real_numbers(self):
        generated_random_real_number = self.model._generate_random_real_numbers()
        assert float(generated_random_real_number)

    def test_generate_random_integers(self):
        generated_random_integer = self.model._generate_random_integers()
        assert generated_random_integer.isdigit() is True

    def test_generate_random_alphanumerics(self):
        generated_alnum = self.model._generate_random_alphanumerics()
        assert generated_alnum.isalnum()

    @patch("os.stat")
    @patch("builtins.open", new_callable=mock_open, read_data="data")
    def test_generate_item_endpoint(self, mock_file, os_stat, client):
        os_stat.return_value.st_size = 5000000
        response = client.post("/v1/item")
        assert response.status_code == 201
        assert response.json == {"file_name": "output.txt"}

    @patch("os.path.exists")
    @patch(
        "builtins.open", new_callable=mock_open, read_data="1234, abcd, abc123, 1.7, "
    )
    def test_retrieve_details_endpoint(self, mock_file, os_path, client):
        response = client.get("/v1/item")
        assert response.status_code == 200
        assert "alphabet" in response.json
        assert "integers" in response.json
        assert "alphanumeric" in response.json
        assert "real_numbers" in response.json


def test_download_output_file_not_existing(client):
    response = client.get("/v1/item/download")
    assert response.status_code == 404
    assert response.json == {"detail": "File not found"}


def test_api_docs(client):
    response = client.get("/api-docs/")
    assert response.status_code == 200
