
from fastapi import APIRouter, Depends, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from .models import Link, AccessLog
from .database import get_db
import random, string

router = APIRouter()

def generate_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@router.post("/api/shorten")
async def shorten(url: str, db: AsyncSession = Depends(get_db)):
    code = generate_code()
    link = Link(original_url=url, short_code=code)
    db.add(link)
    await db.commit()
    return {"short_url": f"http://short.localhost/{code}"}

@router.get("/{code}")
async def redirect(code: str, request: Request, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Link).filter_by(short_code=code))
    link = result.scalars().first()
    if not link:
        return {"error": "Link not found"}

    link.clicks += 1
    db.add(link)
    access = AccessLog(
        short_code=code,
        ip=request.client.host,
        user_agent=request.headers.get("user-agent")
    )
    db.add(access)
    await db.commit()
    return RedirectResponse(link.original_url)
