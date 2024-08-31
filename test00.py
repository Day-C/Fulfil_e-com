#!/usr/bin/python3
"""testing db_storage"""
from models.storage_engine.db_storage import DbStorage
from models.user import User
import models
#get database credentials from envirunment


#storage.reload()
#print(admin.to_dict())
#admin.save()
#print(admin)

alls = models.storage.get ('user', 'e9fd550a-d7e1-46c8-8367-fb9e953d7460')
print(models.storage.count("user"))
