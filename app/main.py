from fastapi import FastAPI

app = FastAPI(
    title="AEGIS",
    version="0.1.0"
)

@app.get("/")
def root():
    return{
        "project":"AEGIS",
        "status":"running"
    }