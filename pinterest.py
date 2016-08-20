#This module handles pinterest.com and return the list of extracted image 
#URLs.
#This module doesn't use an api key.
# As there is no way to use search api in pinterest.com, I have taken the 
# liberty to use web api of pinterest.

import requests

#num- number of images , tag- image tags , place - location
def pinterestAPI(num , tag ,place=""):
	
	#use pinterest web search and find the pins in the source.
	url = 'https://www.pinterest.com/search/pins/?q='+tag+'+'+place
	tag = '<a href="/pin/'
	html = str(requests.get(url).content)
	tagEnd=0
	pinlist =[]
	media = []

	#if the required images ==0 or tag is empty
	if num==0 or tag.strip()=="":
		return media
	
	#Manually find all the 'pin' tags and end the loop when finished.
	while True:
		try:
			tagIndex = html.index(tag,tagEnd)
			tagStart = tagIndex + len(tag)
			tagEnd = html.index('/',tagStart)
			pinID = html[tagStart:tagEnd]
			pinURL =  'https://www.pinterest.com/pin/'+pinID+'/'
       			pinlist.append(pinURL)
		except ValueError:
			break       
	
	for pin in pinlist:

		#if the number of images required is satisfied	
		if len(media)==num:
			break
		#manually find the image in pin urls
		html = str(requests.get(pin).content)
		tag = '<img        src="'
		try:
			imgTag = html.index(tag,0)
			imageStart = imgTag + len(tag)
			imageEnd = html.index('"',imageStart)
			imageSrc = html[imageStart:imageEnd]
			media.append(imageSrc)
		except ValueError,e:
			print "Error occure.pinterest.py" , e
		
	return media


