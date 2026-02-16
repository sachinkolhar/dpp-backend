from fastapi import FastAPI, HTTPException
from database import collection
from models import Product
from utils import generate_uuid, hash_metadata, generate_qr_code
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
import os

BASE_URL = os.getenv("BASE_URL", "http://127.0.0.1:8000")

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.post("/register-product")
def register_product(product: Product):
    product_data = product.dict()
    
    product_id = generate_uuid()
    metadata_hash = hash_metadata(product_data)

    verification_url = f"{BASE_URL}/verify-product/{product_id}"


    generate_qr_code(verification_url, product_id)

    record = {
        "product_id": product_id,
        "metadata": product_data,
        "metadata_hash": metadata_hash,
        "verification_url": verification_url
    }

    collection.insert_one(record)

    qr_image_url = f"{BASE_URL}/static/{product_id}.png"

    return {
    "message": "Product registered successfully",
    "product_id": product_id,
    "verification_url": verification_url,
    "qr_image_url": qr_image_url
}


@app.get("/verify-product/{product_id}", response_class=HTMLResponse)
def verify_product(request: Request, product_id: str):
    record = collection.find_one({"product_id": product_id}, {"_id": 0})
    
    if not record:
        return templates.TemplateResponse("verify.html", {
            "request": request,
            "product": None
        })

    return templates.TemplateResponse("verify.html", {
        "request": request,
        "product": record
    })
