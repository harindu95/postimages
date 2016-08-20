#This module handles flickr.com and returns a list of image URLs.
#This module uses an api key.
#As there is no way to use location with tags in flickr, I have taken the 
# liberty to find images with tags including the location.

import urllib
import urllib2 
import json

#num- number of images, tag- image tags , place - image location

def flickrAPI(api_key,num , tag , place=""):
	
	media =[]

	#if the required images ==0 or tag is empty
	if num==0 or tag.strip()=="":
		return media
	
	# Use flickr photos.search api to get images for the given
	# tags. Returns a JSON without wrapper.
	#use urllib2 to use a GET request to get JSON item
	data = {'api_key' : api_key,
        	  'format' : 'json',
        	  'tags' : tag +' ' + place,
		  'tag_mode' : 'all',
		  'method' : 'flickr.photos.search',
		  'nojsoncallback' :'?' }

	url = 'https://api.flickr.com/services/rest/'
	url_values = urllib.urlencode(data)
	full_url = url + '?' + url_values
	response = urllib2.urlopen(full_url)
	dic = json.loads(response.read())
	
        #Get the photoID's of the images returned.
	#Use flickr photos.getSizes api to get the links of the image.
	url2 = 'https://api.flickr.com/services/rest/?method=flickr.photos.getSizes'
	
	for item in dic['photos']['photo']:
		
		#if the number of images required is satisfied		
		if len(media)==num:
			break
		#Use urllib2 for a GET request , returns a JSON with a  		#wrapper
		data2 = {'api_key' : api_key,
        	  'format' : 'json',
        	  'photo_id':item['id'],
		  'method' : 'flickr.photos.getSizes',
		  'nojsoncallback' :'?' }
		full_url = url2 + '?' +urllib.urlencode(data2)
		response2 = urllib2.urlopen(full_url)
		imageInfo   =jsonAPI(response2.read())
		i = len(imageInfo['sizes']['size'])
		#Append the largest image available or if possible original
		photoSrc  =  imageInfo['sizes']['size'][i-1]['source']
		media.append(photoSrc)
		
	return media

#Function to remove callback from the JSON returned
def jsonAPI(data):
	data =data.replace("jsonFlickrApi(","")
	data =data.replace(")","")
	return json.loads(data)	

