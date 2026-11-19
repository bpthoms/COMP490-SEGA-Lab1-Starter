from fastapi import FastAPI

app = FastAPI(title="COMP 490 - Lab 1")


@app.get("/health")
def health_check():
    return {"status": "ok"}
