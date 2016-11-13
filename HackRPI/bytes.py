from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

auth = Oauth1Authenticator(
    consumer_key = "8ocQu2I1gBxc7OcsSfYt2A",
    consumer_secret = "F5ulxGBDWJK3aNFen_CoLe3Ma0w",
    token = "0P8KGvetjnc_sJaQwG3OuzIentzaAcI9",
    token_secret = "Coxq7Z_FCpMO5_0GpDl32uOC9LM"
)

client = Client(auth)

def get_business_id(busniess_name, business_location):

    return business_id

def get_business_rating(busniess_id):

    return business_rating

def get_business_num_ratings(busniess_id):

    return business_num_ratings



