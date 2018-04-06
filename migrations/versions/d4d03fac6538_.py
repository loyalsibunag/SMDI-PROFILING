"""empty message

Revision ID: d4d03fac6538
Revises: 
Create Date: 2018-04-06 13:54:13.720279

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd4d03fac6538'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('filetable', 'Client',
               existing_type=mysql.VARCHAR(length=10),
               nullable=True)
    op.alter_column('filetable', 'Day',
               existing_type=mysql.VARCHAR(length=10),
               nullable=True)
    op.alter_column('filetable', 'Latitude',
               existing_type=mysql.VARCHAR(length=100),
               nullable=True)
    op.alter_column('filetable', 'Location',
               existing_type=mysql.VARCHAR(length=255),
               nullable=True)
    op.alter_column('filetable', 'Longitude',
               existing_type=mysql.VARCHAR(length=100),
               nullable=True)
    op.alter_column('filetable', 'Month',
               existing_type=mysql.VARCHAR(length=20),
               nullable=True)
    op.alter_column('filetable', 'PC',
               existing_type=mysql.VARCHAR(length=100),
               nullable=True)
    op.alter_column('filetable', 'Station_Code',
               existing_type=mysql.VARCHAR(length=20),
               nullable=True)
    op.alter_column('filetable', 'Station_Name',
               existing_type=mysql.VARCHAR(length=100),
               nullable=True)
    op.alter_column('filetable', 'Type',
               existing_type=mysql.VARCHAR(length=5),
               nullable=True)
    op.alter_column('filetable', 'Weather',
               existing_type=mysql.VARCHAR(length=20),
               nullable=True)
    op.alter_column('filetable', 'Year',
               existing_type=mysql.VARCHAR(length=20),
               nullable=True)
    op.alter_column('filetable', 'isActive',
               existing_type=mysql.VARCHAR(length=10),
               nullable=True)
    op.drop_index('ID', table_name='filetable')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ID', 'filetable', ['ID'], unique=True)
    op.alter_column('filetable', 'isActive',
               existing_type=mysql.VARCHAR(length=10),
               nullable=False)
    op.alter_column('filetable', 'Year',
               existing_type=mysql.VARCHAR(length=20),
               nullable=False)
    op.alter_column('filetable', 'Weather',
               existing_type=mysql.VARCHAR(length=20),
               nullable=False)
    op.alter_column('filetable', 'Type',
               existing_type=mysql.VARCHAR(length=5),
               nullable=False)
    op.alter_column('filetable', 'Station_Name',
               existing_type=mysql.VARCHAR(length=100),
               nullable=False)
    op.alter_column('filetable', 'Station_Code',
               existing_type=mysql.VARCHAR(length=20),
               nullable=False)
    op.alter_column('filetable', 'PC',
               existing_type=mysql.VARCHAR(length=100),
               nullable=False)
    op.alter_column('filetable', 'Month',
               existing_type=mysql.VARCHAR(length=20),
               nullable=False)
    op.alter_column('filetable', 'Longitude',
               existing_type=mysql.VARCHAR(length=100),
               nullable=False)
    op.alter_column('filetable', 'Location',
               existing_type=mysql.VARCHAR(length=255),
               nullable=False)
    op.alter_column('filetable', 'Latitude',
               existing_type=mysql.VARCHAR(length=100),
               nullable=False)
    op.alter_column('filetable', 'Day',
               existing_type=mysql.VARCHAR(length=10),
               nullable=False)
    op.alter_column('filetable', 'Client',
               existing_type=mysql.VARCHAR(length=10),
               nullable=False)
    # ### end Alembic commands ###