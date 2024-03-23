from db.models.models import Customer
from ..utils import DBSessionContext

class CostumerCRUD(DBSessionContext):

    def get_all(self):
        customer = self.db.query(Customer).all()
        return customer

    def get_costumer(self, id : str):
        customer = self.db.query(Customer).filter(Customer.id == id).first()
        return customer

    def get_costumer_by_fullname(self, fullname : str):
        customer = self.db.query(Customer.email).filter(Customer.full_name == fullname).first()._asdict()
        return customer
    
    def create(self, costumer):
        new_costumer = Customer(full_name = costumer.full_name, email = costumer.email)
        self.db.add(new_costumer)
        self.db.commit()
        self.db.refresh(new_costumer)
        return new_costumer
    
    def update(self, costumer, updated):
        
        costumer.email = updated.email
        costumer.full_name = updated.full_name

        self.db.commit()
        return costumer
    
    def delete(self, costumer):
        self.db.delete(costumer)
        self.db.commit()
        return costumer