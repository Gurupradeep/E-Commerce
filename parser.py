from bs4 import BeautifulSoup

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
		while(True):
			for product in products:
				title=product.find('div',class_='product').text
				brand=product.find('div',class_='brand').text
				sizes=product.find('div',class_='sizes').text
				price=product.find('div',class_='price').text
				#strike=price.find('')
				print (title+' '+brand+' '+sizes+' '+price+'\n')
				count=count+1
			print(count)
			next_page_elem=driver.find_element_by_class_name("show-more")
			style=bs.findAll('div',class_='show-more',style='')
			if(style):
				next_page_elem.click()
			else:
				break
		#print(count)
