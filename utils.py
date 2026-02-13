import uuid
import hashlib
import json

def generate_uuid():
    return str(uuid.uuid4())

def hash_metadata(data: dict):
    metadata_string = json.dumps(data, sort_keys=True)
    return hashlib.sha256(metadata_string.encode()).hexdigest()

import qrcode

def generate_qr_code(data: str, filename: str):
    qr = qrcode.make(data)
    qr.save(f"{filename}.png")
