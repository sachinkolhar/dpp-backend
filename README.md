# Digital Product Passport (DPP) System

- A cloud-hosted Digital Product Passport system that enables secure product authentication using QR-based verification and cryptographic metadata hashing.

### Live Demo

👉 [https://dpp-backend-h7cz.onrender.com/docs](https://dpp-backend-h7cz.onrender.com/docs)

---

## Features

* UUID-based unique product identity generation
* SHA-256 metadata hashing for integrity assurance
* QR code generation for product verification
* Cloud-hosted verification endpoint
* Dynamic authenticity verification UI
* MongoDB Atlas cloud database integration
* Production deployment on Render

---

## Architecture

Client → FastAPI Backend → MongoDB Atlas
Product Registration → UUID + Hash → Store
QR Scan → Verification Endpoint → Authenticity UI

<img width="1536" height="1024" alt="system" src="https://github.com/user-attachments/assets/f78ee81a-69f2-4e1a-9f5a-7a269f8efee7" />

---

## Tech Stack

* FastAPI
* MongoDB Atlas
* PyMongo
* Jinja2
* Uvicorn
* Render (Cloud Deployment)
* SHA-256 Cryptographic Hashing
* QR Code Generation

---

## Verification Flow

1. Product registered via API
2. Unique UUID generated
3. Metadata hashed using SHA-256
4. QR code generated with verification URL
5. User scans QR
6. System validates product authenticity

---

## Use Case

Designed as a prototype Digital Product Passport platform to address product authenticity, anti-counterfeiting, and supply chain transparency challenges.

---

## Deployment

Deployed on Render with environment-based configuration:

* `MONGO_URI`
* `BASE_URL`

---

## Future Enhancements

* Blockchain anchoring of product hash
* Admin dashboard
* Revocation & expiry management
* Analytics & tracking
* Brand-customized verification UI

---
