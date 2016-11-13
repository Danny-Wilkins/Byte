from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

auth = Oauth1Authenticator(
    consumer_key = "8ocQu2I1gBxc7OcsSfYt2A",
    consumer_secret = "F5ulxGBDWJK3aNFen_CoLe3Ma0w",
    token = "0P8KGvetjnc_sJaQwG3OuzIentzaAcI9",
    token_secret = "Coxq7Z_FCpMO5_0GpDl32uOC9LM"
)

client = Client(auth)

unimportant = ["the", "and", "am", "for", "or", "of"]

def print_list_per_newline(input_list):
    for i in input_list:
        print i

def get_yelp_results(address, keyword_input):
    params = { 'term' : keyword_input }
    return client.search(address, **params)

def get_yelp_b_names(response):
    #create list with names and distance
    name_distance = []
    for b in response.businesses:
        print b.name, b.distance, b.rating, b.review_count
        temp = [b.name, b.distance]
        name_distance.append(temp)
    ##print_list_per_newline(name_distance)
    #sort list by distance
    name_distance.sort(key = lambda x : x[1])
    #create list of only names
    sorted_names = []
    for i in name_distance:
        sorted_names.append(i[0])
    #return list of ordered names
    return sorted_names

def get_num_matched_words(name_on_yelp, name_list):
    matches = 0
    for word in name_list:
        if word in name_on_yelp:
            matches += 1
    return matches

def replace_sym2space(input_str):
    result_str = ""
    for ch in input_str:
        if( ord(ch) < 65 or ( ord(ch) > 65 + 26 - 1 and ord(ch) < 97 ) or ord(ch) > 97 + 26 - 1):
            result_str += ' '
        else:
            result_str += ch
    return result_str

def remove_unimportant(input_list):
    result_list = []
    for i in input_list:
        if i not in unimportant:
            result_list.append(i)
    return result_list
    
def find_best_yelp_name(list_possibilities, name):
    num_matched_list = []
    name = replace_sym2space(name)
    name = name.lower()
    name_list = name.split()
    name_list = remove_unimportant(name_list)
    for p in list_possibilities:
        num_matched_list.append( get_num_matched_words( p.lower(), name_list ) )
    max_val = max(num_matched_list)
    for i in range(len(num_matched_list)):
        if num_matched_list[i] == max_val:
            return i
    return 0

def get_id(response, yelp_name):
    for b in response.businesses:
        if b.name == yelp_name:
            return b.id
    return "awaheed_error"

def get_rating(yelp_b_id):
    response = client.get_business(yelp_b_id)
    return response.business.rating

def get_num_of_ratings(yelp_b_id):
    response = client.get_business(yelp_b_id)
    return response.business.review_count

def get_rating_and_num_rating(yelp_b_id):#better performace
    response = client.get_business(yelp_b_id)
    return response.business.rating, response.business.review_count    

def main():
    
    address = "11368"
    query = "food"

    name_from_non_yelp = "cabana triangulo"
    response = get_yelp_results(address, query)
    names = get_yelp_b_names(response)
    idx = find_best_yelp_name(names, name_from_non_yelp)

    [rat, num_rat] = get_rating_and_num_rating(get_id(response, names[idx]))
    print rat, num_rat

main()
