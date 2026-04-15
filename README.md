## About
This project is about building and deploying a personal API

## How to Run Locally
```bash
git clone https://github.com/BBello254/hng_internship.git
cd hng_internship
pip install -r requirements.txt
python3 -m uvicorn api:app
```

Then visit http://localhost:8000 in your browser.

## Endpoints

GET /         → {"message": "API is running"}
GET /health   → {"message": "healthy"}
GET /me       → {"name": "Bashirat Bello", "email": "basheerahbello@gmail.com", "github": "https://github.com/BBello254"}

## Live URL
http://142.93.122.1