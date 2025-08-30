import requests

def test_api_country_prediction():
    response = requests.get("http://localhost:5000/predict?country=India")
    assert response.status_code == 200
    assert "prediction" in response.json()

def test_api_all_countries():
    response = requests.get("http://localhost:5000/predict?country=all")
    assert response.status_code == 200
