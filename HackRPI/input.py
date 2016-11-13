import urllib 
import urllib2 
import re 
import cookielib 
  
jar = cookielib.FileCookieJar("cookie") 
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(jar)) 
  
url = 'http://example.com/login.php' 
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' 
  
data = { 
       "Submit": " ", 
         "username":"x", 
        "password":"x", 
} 
  
data = urllib.urlencode(data) 
login_request = urllib2.Request(url, data) 
login_reply = opener.open(login_request) 
login_reply_data = login_reply.read() 
  
login_success_msg = re.compile("Login Successful") 
