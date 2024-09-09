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

alls = models.storage.all('user')
for key in alls.keys():
    print(alls[key].__dict__)
print(models.storage.count("user"))
user10 = models.storage.get('user', 'ba8efdd2-fdb2-41af-b0dd-72ebfb175e68')
user10.delete()

print(models.storage.count("user"))
