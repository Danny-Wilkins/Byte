from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

'''
params = {
    'term': 'food',
    'lang': 'fr'
}

client.search('San Francisco', **params)
'''



auth = Oauth1Authenticator(
    consumer_key = "8ocQu2I1gBxc7OcsSfYt2A",
    consumer_secret = "F5ulxGBDWJK3aNFen_CoLe3Ma0w",
    token = "0P8KGvetjnc_sJaQwG3OuzIentzaAcI9",
    token_secret = "Coxq7Z_FCpMO5_0GpDl32uOC9LM"
)

client = Client(auth)

#### Optional
#
#params = {
#    'lang': 'fr'
#}
#
####

response = client.get_business('yelp-san-francisco')
print response.business.name

'''
params = {
    'term': 'food',
    'lang': 'en'
}

responseObj = client.search('97-22 57th ave', **params)
'''
'''
print responseObj.businesses
print "\n"
'''
'''
#shows nearby businesses, their names and ratings and num ratings
for business in responseObj.businesses:
    print business.name, business.rating, business.review_count
'''
'''
print responseObj.businesses[0].display_phone
print responseObj.businesses[0].distance
print responseObj.businesses[0].eat24_url
print responseObj.businesses[0].id
print responseObj.businesses[0].image_url
print responseObj.businesses[0].is_claimed
print responseObj.businesses[0].is_closed
print responseObj.businesses[0].menu_provider
print responseObj.businesses[0].menu_date_updated
print responseObj.businesses[0].mobile_url
print responseObj.businesses[0].name
print responseObj.businesses[0].phone
print responseObj.businesses[0].rating
print responseObj.businesses[0].rating_img_url
print responseObj.businesses[0].rating_img_url_small
print responseObj.businesses[0].rating_img_url_large
print responseObj.businesses[0].reservation_url
print responseObj.businesses[0].review_count
print responseObj.businesses[0].snippet_image_url
print responseObj.businesses[0].snippet_text
print responseObj.businesses[0].url
'''


