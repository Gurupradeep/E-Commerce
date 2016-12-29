from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from optparse import OptionParser
from config import URL_FORMAT
from parser import MyntraParser



driver = None


def get_page_source(driver,url):
	driver.get(url)
	return driver.page_source


def crawl(driver,keyword):
	html_data=get_page_source(driver,URL_FORMAT % keyword)
	mp=MyntraParser(html_data)
	mp.parser(driver)

def crawler_machine(search_word=None):
	global driver
	optparser=OptionParser()
	optparser.add_option("-s","--search",type="string",dest="search")
	(options,args)=optparser.parse_args()
	keyword=options.search or search_word
	print "keyword="+keyword
	try:
		try:
			driver=webdriver.PhantomJS(service_args=['--ssl-protocol=any'])
			#print driver.window_handles
		except:
			driver=webdriver.FireFox()
		crawl(driver,keyword)
	
	finally:
		driver.close()

if __name__=='__main__':
	crawler_machine()
