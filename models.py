from pymongo import MongoClient
from datetime import datetime
from bson import json_util
import re
import json

def connect_to_db(collection=False) :
	connection = MongoClient('localhost',27017)
	db = connection['Myntra']
	try :
		if collection :
			return db.myntraitems
		return db

	except Exception as e :
		pass


def insert(input_dict) :
	table = connect_to_db(collection = True)
	table.insert({'crawled_at':datetime.utcnow(),\
		'title':input_dict.get('title',None),\
		'brand':input_dict.get('brand',None),\
		'sizes':input_dict.get('sizes',None),\
		'price':input_dict.get('price',None)
		})