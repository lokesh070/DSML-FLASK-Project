from predictions import app
import pytest
import json

@pytest.fixture
def client():
    return app.test_client()

#client make sure that it acts as a server
def test_pinger(client):
    response = client.get('/ping')
    assert response.status_code == 200
    assert response.json == {'Message': 'This is a Hello Message'}

def test_predict(client):
    test_data = {
    "Gender":"Male",
    "Married":"Yes",
    "ApplicantIncome":500000,
    "LoanAmount":5000,
    "Credit_History":0.0
    }
    response = client.post('/predict', json=test_data)
    assert response.status_code == 200

    assert response.json == {'Loan Approval Status': 'Rejected'}
