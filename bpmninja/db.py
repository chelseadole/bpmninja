"""Postgres DB."""

import os
from sqlalchemy import create_engine, Column, Integer, String, Table, MetaData
from sqlalchemy.orm import sessionmaker


postgres_url = "postgresql://{}:{}@{}:{}/{}".format(
    os.environ.get("BPM_DB_USER", None),
    os.environ.get("BPM_DB_PASSWORD", None),
    os.environ.get("BPM_DB_IP", None),
    os.environ.get("BPM_DB_PORT", None),
    os.environ.get("BPM_DB_NAME", None)
)

metadata = MetaData()

song = Table('song', metadata,
    Column('id', Integer, primary_key=True),
    Column('songTitle', String),
    Column('artist', String),
    Column('album', String),
    Column('bpm', Integer),
    Column('artwork', String)
    )

engine = create_engine(postgres_url)
Session = sessionmaker(bind=engine)

# Creates song table
metadata.create_all(engine)
