"""Database description, a la sqlalchemy."""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Session = sessionmaker()

postgres_url = "postgresql://{}:{}@{}:{}/{}".format(
    os.environ.get("BPM_DB_USER", None),
    os.environ.get("BPM_DB_PASSWORD", None),
    os.environ.get("BPM_DB_IP", None),
    os.environ.get("BPM_DB_PORT", None),
    os.environ.get("BPM_DB_NAME", None)
)
db = create_engine(postgres_url)
Base = declarative_base()


class Song(Base):
    """Song table."""
    __tablename__ = 'song'

    id = Column(Integer, primary_key=True)
    songTitle = Column(String)
    artist = Column(String)
    album = Column(String)
    bpm = Column(Integer)
    artwork = Column(String)

    def __repr__(self):
        """Song repr method."""
        return "<Song(songTitle='%s', id='%s', artist='%s', bpm='%s')>" % (
            self.songTitle, self.id, self.artist, self.bpm)

Session = sessionmaker(db)

Base.metadata.create_all(db)
