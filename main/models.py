import sqlalchemy
from sqlalchemy import DateTime, func

from main.constants import UserStatus, ReportType, ReportStatus
from main.database import metadata

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("username", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("full_name", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("language", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("chat_id", sqlalchemy.BigInteger, unique=True, nullable=False),
    sqlalchemy.Column("phone_number", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("status", sqlalchemy.String, default=UserStatus.active, nullable=False),
    sqlalchemy.Column('created_at', DateTime(timezone=True), server_default=func.now(), nullable=False),
    sqlalchemy.Column('updated_at', DateTime(timezone=True), onupdate=func.now(), nullable=False)
)

reports = sqlalchemy.Table(
    "reports",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"), nullable=False),
    sqlalchemy.Column("amount", sqlalchemy.Integer or sqlalchemy.Float, nullable=False),
    sqlalchemy.Column("description", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("type", sqlalchemy.String, default=ReportType.income, nullable=False),
    sqlalchemy.Column("status", sqlalchemy.String, default=ReportStatus.activated, nullable=False),
    sqlalchemy.Column("created_at", DateTime(timezone=True), server_default=func.now(), nullable=False),
    sqlalchemy.Column("updated_at", DateTime(timezone=True), onupdate=func.now(), nullable=False)
)
