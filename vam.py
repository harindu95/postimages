#This module handles vam.ac.uk and return the list of extracted image 
#URLs.
#This module doesn't use an api key.

import urllib
import urllib2 
import json

#num- number of images , tag- image tags , place - location
def vamAPI(num,tag , place =""):
 
	#use urllib2 to use the web api and get  JSON as a response.
	data = {'q' : tag,
		'placesearch' : place,
	        'images' : '1',
		  }
	url = 'http://www.vam.ac.uk/api/json/museumobject/'
	url_values = urllib.urlencode(data)
	full_url = url + '?' + url_values
	response = urllib2.urlopen(full_url)
	dic = json.loads(response.read())
	media = []

	for item in dic['records']:

		#if the number of images required is satisfied	
		if len(media)==num:
			break

		imageID= item['fields']['primary_image_id']
		imageURL = 'http://media.vam.ac.uk/media/thira/collection_images/' + imageID[:6]+'/' +imageID +'.jpg'
		media.append(imageURL)
		
	return media


