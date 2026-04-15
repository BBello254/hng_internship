from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API is running"}

@app.get("/health")
def health():
    return {"message": "healthy"}

@app.get("/me")
def me():
    return {
            "name": "Bashirat Bello",
            "email": "basheerahbello@gmail.com",
            "github": "https://github.com/BBello254"
    }