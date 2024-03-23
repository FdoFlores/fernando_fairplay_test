
from fastapi import APIRouter, HTTPException, Depends

from db.session import get_session
from sqlalchemy.orm import Session
from db.models.models import Customer, Loan
from .services import LoanService
from .schemas import LoanSchema
from ..users.services import get_current_user, User

router = APIRouter(prefix="/loans", tags=["Loans"])


# Create: Permite crear un nuevo cliente en la base de datos.
# List: Devuelve una lista de todos los clients existentes.
# Retrieve: Obtiene los detalles de un cliente específico.
# Update: Actualiza la información de un cliente existente.
# Delete: Elimina un cliente de la base de datos.

@router.get("/retrieve/{id}")
def retrieve_loan(id: str, db: Session = Depends(get_session), current_user: User = Depends(get_current_user)):
    result = LoanService(db).get_loan(id)
    return {"Loan": result}

@router.get("/list")
def list_all_loans(db: Session = Depends(get_session), current_user: User = Depends(get_current_user)):
    result = LoanService(db).get_all()
    return {"Loan": result}

@router.post("/create/{customer_id}")
def create_loan(customer_id: str, loan: LoanSchema, db: Session = Depends(get_session), current_user: User = Depends(get_current_user)):
    result = LoanService(db).create(customer_id, loan)
    return {"Message": f'Created {result.amount} successfully with ID: {result.id}'}

@router.put("/update/{id}")
def update_loan(id: str, loan: LoanSchema, db: Session = Depends(get_session), current_user: User = Depends(get_current_user)):
    result = LoanService(db).update(id, loan)
    return {"Message": f'Updated {id} successfully'}

@router.delete("/delete/{id}")
def update_loan(id: str, db: Session = Depends(get_session), current_user: User = Depends(get_current_user)):
    result = LoanService(db).delete(id)
    return {"Message": f'Deleted {id} successfully'}