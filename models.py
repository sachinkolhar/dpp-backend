from pydantic import BaseModel

class Product(BaseModel):
    name: str
    brand: str
    manufacturer: str
    production_date: str
