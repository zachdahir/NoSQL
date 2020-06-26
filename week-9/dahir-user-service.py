#
#============================================
# Title: 9.2
# Author: Zachary Dahir
# Date: 6-23-20
# Description: Querying and Creating Documents
#===========================================
#

import pymongo
import pprint
import datetime

from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.web335

#Create user
user = {
    "first_name": "Thomas",
    "last_name": "Shelby",
    "email": "ShelbyCoLimited@yahoo.com",
    "employee_id": "0000005",
    "date_created": datetime.datetime.utcnow()
}

#Insert User
user_id = db.users.insert_one(user).inserted_id

#Print user
print(user_id)

pprint.pprint(db.users.find_one({"employee_id": "0000005"}))