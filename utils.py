import uuid
import hashlib
import json
import os
import qrcode

def generate_uuid():
    return str(uuid.uuid4())

def hash_metadata(data: dict):
    metadata_string = json.dumps(data, sort_keys=True)
    return hashlib.sha256(metadata_string.encode()).hexdigest()



def generate_qr_code(data: str, filename: str):
    os.makedirs("static", exist_ok=True)
    qr = qrcode.make(data)
    qr.save(f"static/{filename}.png")

