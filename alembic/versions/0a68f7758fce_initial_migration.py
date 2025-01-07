# 0a68f7758fce_initial_migration.py

"""create users table

Revision ID: 0a68f7758fce
Revises: None
Create Date: 2025-01-07 12:00:00
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# Revisiyon ID va Down Revision
revision = '0a68f7758fce'
down_revision = None  # Bu birinchi migratsiya, shuning uchun down_revision = None

def upgrade():
    # Bu yerga yangi jadval yaratish kodini yozing
    op.create_table(
        'users',
        sa.Column('id', sa.BigInteger(), nullable=False),
        sa.Column('telegram_id', sa.BigInteger(), nullable=False),
        sa.Column('username', sa.String(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False, server_default=sa.func.now()),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    # Migratsiyani bekor qilish uchun kerakli kodni yozing
    op.drop_table('users')
