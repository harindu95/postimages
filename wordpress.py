#This function sends an email through a smtp server, to create a wordpress 
#post. It takes a list of URLs of images and subject of the post as
#parameters.

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#media - a list of image URLs
def post_to_blog(media,subject="Testing"):
	msg = MIMEMultipart()
	me = 'harindu95dilshan@gmail.com' #Sender's email
	to = 'fixo607wuhu@post.wordpress.com' #The email provided by wordpress to use email to post function
	msg['Subject'] = subject
	msg['From']=me
	msg['To'] = to
	string =''
        #images are created as html img tags
	for item in media:
	   string = string + '<img src="'+str(item)+'" >'
	
	msg.attach(MIMEText(string,'html')) 
	#Use a custom smtp server to send email
	server = smtplib.SMTP('smtp.sendgrid.net:2525')
	server.ehlo()
	server.starttls()
	server.login('zuko95','password')
	server.sendmail(me, to, msg.as_string())
	server.quit()
