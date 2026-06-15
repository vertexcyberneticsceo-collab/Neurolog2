from fastapi import FastAPI

app = FastAPI(title="Neurolog")


@app.get("/")
def root():
    return {
        "name": "Neurolog",
        "status": "running",
        "message": "Medical event monitoring API"
    }


@app.get("/health")
def health():
    return {"status": "healthy"}
