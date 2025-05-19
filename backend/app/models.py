
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Link(Base):
    __tablename__ = 'links'
    id = Column(Integer, primary_key=True)
    original_url = Column(String, nullable=False)
    short_code = Column(String, unique=True, nullable=False)
    clicks = Column(Integer, default=0)
    created_at = Column(DateTime, server_default=func.now())
    accesses = relationship("AccessLog", back_populates="link")

class AccessLog(Base):
    __tablename__ = 'access_logs'
    id = Column(Integer, primary_key=True)
    short_code = Column(String, ForeignKey("links.short_code"))
    ip = Column(String)
    user_agent = Column(String)
    timestamp = Column(DateTime, server_default=func.now())
    link = relationship("Link", back_populates="accesses")
