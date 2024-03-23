from fastapi import APIRouter, HTTPException, Depends, Query
from db.session import get_session
from sqlalchemy.orm import Session
from db.models.models import User
from .services import CostumerService
from .schemas import CostumerSchema
from ..users.services import get_current_user
router = APIRouter(prefix="/customers", tags=["Customers"])

# Create: Permite crear un nuevo cliente en la base de datos.
# List: Devuelve una lista de todos los clients existentes.
# Retrieve: Obtiene los detalles de un cliente específico.
# Update: Actualiza la información de un cliente existente.
# Delete: Elimina un cliente de la base de datos.


@router.get("/retrieve/{id}")
def retrieve_costumer(id: str, db: Session = Depends(get_session), current_user: User = Depends(get_current_user)):
    result = CostumerService(db).get_costumer(id)
    return {"Costumer": result}

@router.get("/list")
def list_all_costumers(page: int = Query(None, ge = 0), page_size: int = Query(None, ge = 0), db: Session = Depends(get_session), current_user: User = Depends(get_current_user)):
    result = CostumerService(db).get_all(page, page_size)
    return {"Costumer": result}

@router.post("/create")
def create_costumer(costumer: CostumerSchema, db: Session = Depends(get_session), current_user: User = Depends(get_current_user)):
    result = CostumerService(db).create(costumer)
    return {"Message": f'Created {result.full_name} successfully with ID: {result.id}'}

@router.put("/update/{id}")
def update_costumer(id: str, costumer: CostumerSchema, db: Session = Depends(get_session), current_user: User = Depends(get_current_user)):
    result = CostumerService(db).update(id, costumer)
    print(result)
    return {"Message": f'Updated {result.full_name} successfully'}

@router.delete("/delete/{id}")
def update_costumer(id: str, db: Session = Depends(get_session), current_user: User = Depends(get_current_user)):
    result = CostumerService(db).delete(id)
    return {"Message": f'Deleted {result.full_name} successfully'}