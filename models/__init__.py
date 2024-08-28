#!/usr/bin/python3
"""lint to storage system."""
from models.storage_engine.db_storage import DbStorage

#create a DbStorage object
storage = DbStorage()
#reload to create tables and session
storage.reload()
