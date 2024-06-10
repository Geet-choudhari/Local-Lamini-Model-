import os
from chromadb.config import Settings

# define chorma settings

CHROMA_SETTINGS = Settings(
    # path to the chroma executable
    chroma_db_impl = 'duckb+parquet',
    persist_directory = "db",
    anonymized_telemetry = False
)

