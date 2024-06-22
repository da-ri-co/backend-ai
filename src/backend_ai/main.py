from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router.router import router
from dotenv import load_dotenv

app = FastAPI(title="bedrock")

load_dotenv()

# app.add_middleware(
#    CORSMiddleware,
#    allow_credentials=True,
#    allow_origins=["*"],
#    allow_methods=["*"],
#    allow_headers=["*"],
# )


@app.get("/check_health")
async def hello():
    return {"message": "ok"}


app.include_router(router, prefix="/api/v1")
