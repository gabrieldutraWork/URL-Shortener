from fastapi import FastAPI
from contextlib import asynccontextmanager
from .routes import router
from .models import Base
from .database import engine

import asyncio
from sqlalchemy.ext.asyncio import AsyncEngine

async def wait_for_db(engine: AsyncEngine, retries: int = 10, delay: int = 2):
    for attempt in range(retries):
        try:
            async with engine.begin() as conn:
                await conn.run_sync(lambda _: None)
            print("✅ Banco de dados está pronto!")
            return
        except Exception as e:
            print(f"⏳ Aguardando banco de dados... tentativa {attempt+1}/{retries}")
            await asyncio.sleep(delay)
    raise Exception("❌ Banco de dados não respondeu a tempo.")

@asynccontextmanager
async def lifespan(app: FastAPI):
    await wait_for_db(engine)  # <- espera o banco de dados
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(router)


@app.get("/")
async def root():
    return {"message": "API está funcionando!"}
