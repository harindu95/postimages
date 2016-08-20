#The interface for the user.

import sys
import flickr
import insta
import ebay
import pinterest
import vam
import urllib2
import wordpress
import traceback



def setupKeys():
	flickr_key,ebay_key ="",""
	f = open('keys.txt','r')
	for line in f:
		if line.startswith('#'):
			continue
		else:
			if line.startswith('ebay'):
				i = line.index('"')+1		
				ebay_key = line[i:line.index('"',i)]
			if line.startswith('flickr'):
				i = line.index('"') +1
				e = line.index('"',i)
				flickr_key = line[i:e]
	return flickr_key,ebay_key
		


def main():
	tag = ""
	place = ""
	num =0
	#Check the command line arguments
	if len(sys.argv) <=2:
		print "Enter at least 2 parameters. Eg-'python postimages.py tower 3'"
		return
	
	elif len(sys.argv)>2:
		tag = sys.argv[1]
		tag = " ".join(tag.split("+"))
		#Check the number of images from arguments
		try:
			if len(sys.argv)==3:
				num = int(sys.argv[2])
			elif len(sys.argv)==4:
				place = " ".join(sys.argv[2].split("+"))
				num = int(sys.argv[3])
			if num<0:
				raise ValueError
		except ValueError:
			print "Please enter a positive integer.Follow the format 'python postimages.py tower 3' or 'python postimages.py tower paris 4'"
			return
		
		media = []
		#Call the various functions to retrieve images.
		try:
			print "Retrieving images.This may take a few minutes"
			media.extend(vam.vamAPI(num,tag,place))
			media.extend(flickr.flickrAPI(flickr_key,num,tag,place))
			media.extend(insta.instagramAPI(num,tag,place))
			media.extend(pinterest.pinterestAPI(num,tag,place))
			media.extend(ebay.ebayAPI(ebay_key,num,tag,place))
			print "Number of images found: ",len(media)
			print "Uploading images to wordpress."
			wordpress.post_to_blog(media,tag+place)
			print "Completed.Check your wordpress blog after a few minutes."
		except urllib2.URLError,e:
			print "Check your internet conncetion.",e
		except Exception, e:
			print "Script has stopped working.",e , type(e)
			traceback.print_exc()

flickr_key,ebay_key =setupKeys()
main()
