from db.models.models import Loan
from ..utils import DBSessionContext

class LoanCRUD(DBSessionContext):

    def get_loan(self, id):
        return self.db.query(Loan).filter(Loan.id == id).first()

    def get_all(self):
        customer = self.db.query(Loan).all()
        return customer
    
    def create(self, cust_id, loan):
        new_loan = Loan(amount = loan.amount, customer_id = cust_id)
        self.db.add(new_loan)
        self.db.commit()
        self.db.refresh(new_loan)
        return new_loan
    
    def update(self, db_loan, loan):
        db_loan.amount = loan.amount
        self.db.commit()
        return db_loan

    def delete(self, loan):
        self.db.delete(loan)
        self.db.commit()
        return loan
    
    def get_costumer_loans(self, costumer_id):
        return self.db.query(Loan.amount, Loan.customer_id, Loan.id, Loan.created, Loan.modified).filter(Loan.customer_id == costumer_id).all()