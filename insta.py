#This module handles instagram.com and returns a list of image URLs.
#This module doesn't use an api key.
#As there is no way to use location with tags in instagram.com, I have 
#taken the liberty to find images with tags using google search.
from google import search
import requests

#num- number of images, tag - image tags, place - location
def instagramAPI(num,tag,place=""):
	ls = []
	media=[]

	#if the required images ==0 or tag is empty
	if num==0 or tag.strip()=="":
		return media
	#Use google to search instagram.com and get a list of URLs.
	#use a custom python module called google.py
	for url in search('site:instagram.com "#'+tag+'" "#'+place+'"', stop=num):
		ls.append(url)

	#Find the image tag manually in the html source of URLs.
	tag = '<meta property="og:image" content="'
	for item in ls:
		#if the number of images required is satisfied	
		if len(media) == num:
			break
		html = str(requests.get(item).content)
		try:
			tagIndex = html.index(tag)
			tagStart = tagIndex + len(tag)
			#meta tag ends with '?'
			tagEnd = html.index('?',tagStart)
			imageSrc = html[tagStart:tagEnd]
			media.append(imageSrc)
		
		except ValueError,e :
			print "Error occured.insta.py: ",e
		
	return media


