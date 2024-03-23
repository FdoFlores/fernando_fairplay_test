from fastapi import HTTPException
# from comun.models.user import UsersDB
from .dao import LoanCRUD
from ..utils import DBSessionContext
from ..costumers.services import CostumerCRUD

class LoanService(DBSessionContext):
    def get_loan(self, id):
        loan = LoanCRUD(self.db).get_loan(id)

        if not loan:
            raise HTTPException(status_code=404, detail="Loan not found.")

        return loan

    def get_all(self):
        loans = LoanCRUD(self.db).get_all()
        if not loans:
            raise HTTPException(status_code=404, detail="Loans not found.")
        return loans
    
    def create(self, costumer_id, loan):
        costumer = CostumerCRUD(self.db).get_costumer(costumer_id)
        if not costumer:
            raise HTTPException(status_code=404, detail="Costumer not found.")
        return LoanCRUD(self.db).create(costumer_id, loan)
    
    def update(self, id, loan):
        db_loan = self.get_loan(id)
        return LoanCRUD(self.db).update(db_loan, loan)
    
    def delete(self, id):
        db_loan = self.get_loan(id)
        return LoanCRUD(self.db).delete(db_loan)
    
    def get_costumer_loans(self, costumer_id):
        costumer = CostumerCRUD(self.db).get_costumer(costumer_id)
        if not costumer:
            raise HTTPException(status_code=404, detail="Costumer not found.")
        print('bbb')
        loans = LoanCRUD(self.db).get_costumer_loans(costumer_id)
        return loans