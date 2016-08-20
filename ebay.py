# This module handles ebay.com and return a list of image URLs.
# This module uses an api key.
# I have taken the liberty to find items with tags including the location, # not specifically in the geological place.
# Change the api_key to your api key
api_key = 'HarinduG-pythonSc-PRD-890ed7b6b-5337fd95'

import urllib
import urllib2 
import json


#num- number of images , tag- image tags , place - location
def ebayAPI(api_key,num,tag,place =""):
	media = []

	#if the required images ==0 or tag is empty
	if num==0 or tag.strip()=="":
		return media

	# Use ebay findItemByKeywords api to get items for the given
	# tags. Returns a JSON without wrapper.
	#use urllib2 to use a GET request to get JSON item
	
	data = {'OPERATION-NAME':'findItemsByKeywords',
          'SERVICE-VERSION':'1.0.0',
          'SECURITY-APPNAME' :api_key,
	  'GLOBAL-ID':'EBAY-US',
	  'RESPONSE-DATA-FORMAT':'JSON',
	  
	  'REST-PAYLOAD':'',
	  'keywords':" ".join((tag,place)),
	  'paginationInput.entriesPerPage':num
	 }
	url = 'http://svcs.ebay.com/services/search/FindingService/v1'
	url_values = urllib.urlencode(data)
	full_url = url + '?' + url_values
	response = urllib2.urlopen(full_url)
	dic = json.loads(response.read())
		
	#Find the image in the url of ebay item.
	##Find the image tag manually in the html source of URLs.	
	tag = '<meta  property="og:image" content="'
	try:
		for item in dic['findItemsByKeywordsResponse'][0]['searchResult'][0]['item']:
			#if the number of images required is satisfied	
			if len(media)==num:
				break
			html = urllib2.urlopen(str(item['viewItemURL'][0])).read()
			try:			
				tagIndex = html.index(tag)
				tagStart = tagIndex + len(tag)
				#image tag ends with '/>'
				tagEnd = html.index('" />',tagStart)
				imageSrc = html[tagStart:tagEnd]
				media.append(imageSrc)
			except ValueError:
				print "Error occured.ebay.py: ",e
		
	except KeyError,e:
		print "Error occured.ebay.py: ",e
	return media


