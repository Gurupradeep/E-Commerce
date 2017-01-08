from pymongo import MongoClient, DESCENDING,ASCENDING
from datetime import datetime
from bson import json_util
import re
import json

def connect_to_db(collection=False) :
	connection = MongoClient('localhost',27017)
	db = connection['myntra']
	try :
		if collection :
			return db.myntraitems
		return db

	except Exception as e :
		pass


def insert(input_dict) :
	table = connect_to_db(collection = True)
	table.insert({'crawled_at':datetime.utcnow(),\
		'id':input_dict.get('id',None),\
		'title':input_dict.get('title',None),\
		'brand':input_dict.get('brand',None),\
		'sizes':input_dict.get('sizes',None),\
		'original_price':input_dict.get('original_price',None),\
		'discounted_price':input_dict.get('discounted_price',None)
		})

def fetch_by_title(title,_as=None):
	print "Title:",title
	result=[]
	table=connect_to_db(collection=True)
	regex='.*'+title+'.*'
	for row in table.find({"title": re.compile(regex,re.IGNORECASE)}).sort('id',ASCENDING):
		result.append(row)
	if _as =='json':
		return json.dumps({title:result},default=json_util.default)
	return result