import os

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "mysql+pymysql://root:root@db:3306/clinica",  # valor por defecto si no existe
)
