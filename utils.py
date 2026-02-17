import uuid
import hashlib
import json
import os
import qrcode
import io
import base64
def generate_uuid():
    return str(uuid.uuid4())

def hash_metadata(data: dict):
    metadata_string = json.dumps(data, sort_keys=True)
    return hashlib.sha256(metadata_string.encode()).hexdigest()




def generate_qr_code(data: str):
    qr = qrcode.make(data)
    buffer = io.BytesIO()
    qr.save(buffer, format="PNG")
    buffer.seek(0)

    img_str = base64.b64encode(buffer.read()).decode()
    return img_str

