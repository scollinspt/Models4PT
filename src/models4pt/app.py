from fastapi import FastAPI

app = FastAPI(
    title="Models4PT",
    description="Minimal starting scaffold for the Models4PT knowledge platform backend.",
    version="0.1.0",
)


@app.get("/", tags=["health"])
def root() -> dict:
    return {"message": "Models4PT backend is running."}


@app.get("/health", tags=["health"])
def health_check() -> dict:
    return {"status": "ok"}
