from fastapi import FastAPI

app = FastAPI(title="OkaSan API")


@app.get("/health")
def health():
    return {"status": "ok"}
