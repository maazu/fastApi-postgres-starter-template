import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME:str 
    VERSION:str 
    DESCRIPTION:str  
    DB_URI:str
    ECHO_SQL:bool

    class Config:
        case_sensitive = True
        env_file = '.env'
        
    
settings = Settings()