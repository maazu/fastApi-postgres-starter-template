import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME:str 
    VERSION:str 
    DESCRIPTION:str  
    DATABASE_URL:str


    class Config:
        case_sensitive = True
        env_file = '.env'
        
    
settings = Settings()