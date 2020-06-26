#
#============================================
# Title: 9.3
# Author: Zachary Dahir
# Date: 6-23-20
# Description: Updating Documents
#===========================================
#

#import statements
import pymongo
import pprint
import datetime

from pymongo import MongoClient

client = MongoClient('localhost', 27017)

#Use Web 335
db = client.web335

#Update Email
db.users.update_one(
    {'employee_id': "0000005"},
    {"$set": {"email": "zdahir@my365.bellevue.edu"}}
)

#print user
pprint.pprint(db.users.find_one({'employee_id': "0000005"}))