from bs4 import BeautifulSoup
from config import  MONGO_STORAGE_INPUT_DICT
from models import insert
class MyntraParser(object):
	
	def __init__(self,page):
		#self.title=""
		#self.price=0
		#self.sizes=""
		#self.brand=""
		self.page=page

	def parser(self,driver):
		bs=BeautifulSoup(self.page,"html.parser")
		products=bs.findAll('a',class_='product-link')
		count=0
		for product in products:
			title=product.find('div',class_='product').text
			brand=product.find('div',class_='brand').text
			sizes=product.find('div',class_='sizes').text
			price=product.find('div',class_='price').text
				#strike=price.find('')
			print (title+' '+brand+' '+sizes+' '+price+'\n')
			data_layer = MONGO_STORAGE_INPUT_DICT
			data_layer['title'] = title
			data_layer['brand'] = brand
			data_layer['sizes'] = sizes
			data_layer['price'] = price
			insert(data_layer)
 

		#print(count)
