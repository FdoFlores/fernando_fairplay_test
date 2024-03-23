from fastapi.testclient import TestClient
from api.v1.costumers.schemas import CostumerSchema
from main import app

client = TestClient(app)

def test_create_customer():
    # Sample customer data
    customer_data = {
        "full_name": "feeeeeeer",
        "email": "fllllll2"
}
    
    response = client.post("/v1/customers/create", json=customer_data)
    
    #assert response.status_code == 200
    print(response.json())
    created_customer = response.json()
    #assert created_customer == created_customer
    # Add assertions for other fields as needed