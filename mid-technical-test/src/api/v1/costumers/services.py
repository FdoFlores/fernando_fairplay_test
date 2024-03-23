from fastapi import HTTPException
# from comun.models.user import UsersDB
from .dao import CostumerCRUD
from ..utils import DBSessionContext
from .schemas import ReturnCostumer, ReturnLoanSchema
from ..loans.services import LoanService

class CostumerService(DBSessionContext):

    def get_all(self, page, page_size):

        costumers = CostumerCRUD(self.db).get_all()

        if not costumers:
            raise HTTPException(status_code=404, detail="Costumers not found.")

        # Returns specific objects depending on the pagination parameters if they were sent.
        if page and page_size:
            start_i = (page - 1) * page_size
            end_i = start_i + page_size
            return costumers[start_i:end_i]
        else:
            return costumers
    
    
    def costumer_exists(self, id: str):
        costumer = CostumerCRUD(self.db).get_costumer(id)
        if not costumer:
            raise HTTPException(status_code=404, detail="Costumer not found.")
        return costumer
    
    def get_costumer(self, id: str):
        costumer = CostumerCRUD(self.db).get_costumer(id)

        if not costumer:
            raise HTTPException(status_code=404, detail="Costumer not found.")

        # Fill a loans list with the schema ReturnLoanSchema to send it to the ReturnCustomer schema.
        c_loans = []
        loans = LoanService(self.db).get_costumer_loans(id)
        for loan in loans:
            c_loans.append(
                ReturnLoanSchema(
                    amount = loan.amount,
                    customer_id = loan.customer_id,
                    id = loan.id,
                    created = loan.created,
                    modified = loan.modified
                )
            )

        response = ReturnCostumer(
            full_name = costumer.full_name,
            email = costumer.email,
            loans = c_loans
        )

        return response

    def get_costumer_by_fullname(self, fullname: str):
        costumer = CostumerCRUD(self.db).get_costumer_by_fullname(fullname)

        if not costumer:
            raise HTTPException(status_code=404, detail="")
        
        return costumer
    
    def create(self, costumer):
        return CostumerCRUD(self.db).create(costumer)
    
    def update(self, id, costumer):
        db_costumer = self.costumer_exists(id)
        return CostumerCRUD(self.db).update(db_costumer, costumer)
    
    def delete(self, id):
        db_costumer = self.costumer_exists(id)
        # If costumer has loans we need to delete them all before deleting the costumer.
        loans = LoanService(self.db).get_costumer_loans(id)
        if loans:
            for loan in loans:
                LoanService(self.db).delete(loan.id)
        return CostumerCRUD(self.db).delete(db_costumer)