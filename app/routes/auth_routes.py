from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
import app.services.auth_service as auth_service

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class Token(BaseModel):
    access_token: str
    token_type: str

@router.post("/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = auth_service.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Credenciais inválidas")
    
    access_token = auth_service.create_access_token(data={"sub": user.username, "role": user.role})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/user")
async def read_users(token: str = Depends(oauth2_scheme)):
    return auth_service.get_user_info(token)

@router.get("/admin")
async def read_admins(token: str = Depends(oauth2_scheme)):
    return auth_service.get_admin_info(token)
