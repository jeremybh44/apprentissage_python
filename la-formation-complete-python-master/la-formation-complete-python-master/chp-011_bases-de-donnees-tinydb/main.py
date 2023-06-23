from tinydb import TinyDB, Query, where
# from tinydb.storages import MemoryStorage

db = TinyDB('data.json', indent=4)
#db = TinyDB(storage=MemoryStorage) # enregistrer notre base de donnée en memoire plutot que dans un fichier


users = db.table("Users")
roles = db.table("Roles")

users.insert({"name": "Patrick", "salary": 25000})
users.insert({"name": "Paul", "salary": 35000})
users.insert({"name": "Julie", "salary": 45000})

roles.insert_multiple([
    {"name": "Pythonista"},
    {"name": "Javaista"},
    {"name": "JavaScripta"},
])