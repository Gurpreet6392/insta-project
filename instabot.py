import requests #IMPORT LIBRARY BY REQUEST

# define function to enter user name entered by app uers nd desired task
def username():
    a = raw_input("enter instagram user name =  ")
    b = raw_input("enter what kind of action u want to perform your options are= 1. like a post  2. comment = ")
    print a
    print b
username()

#using a access token for app
APP_ACCESS_TOKEN = '1560024934.53ba031.1ef6f902d8044a77bccbd08b0c200f96'
#using base url from instagram api
BASE_URL = 'https://api.instagram.com/v1'

#define a function to get my info
def self_info():
    request_url = (BASE_URL + '/users/self/?access_token=%s ') %( APP_ACCESS_TOKEN )   #getting data by token access +base url
    print 'REQUESTING URL FOR DATA :' + request_url
    my_info = requests.get(request_url).json()              #printing info in json format
    print 'my info on instagram : \n'
    print my_info

self_info()


#define function to get a insta userr id
def get_user_id_by_username(insta_username):
    request_url =(BASE_URL + '/users/search?q=%s&access_token=%s') % (insta_username , APP_ACCESS_TOKEN)
    print 'requesting url for data: ' + request_url
    search_results = requests.get(request_url).json()

    if  search_results['meta']['code'] == 200:
        if len(search_results['data']):
            print search_results['data'][0]['id']
            return search_results['data'][0]['id']
        else:
             print "user doent not exist!!!!"
    else:
        print "request couled not be completed!!!"
    return None

get_user_id_by_username('shubham.is.here')

#define function to get a user post from insta

def get_user_recent_posts(insta_username):
    insta_user_id = get_user_id_by_username(insta_username)
    request_url =(BASE_URL + '/users/%s/media/recent/?access_token=%s') % (  insta_user_id , APP_ACCESS_TOKEN)
    print 'requesting url for data: ' + request_url
    recent_posts = requests.get(request_url).json()

    if recent_posts['meta']['code'] == 200:
       if len(recent_posts['data']):
           return recent_posts['data'][10]['id']
       else:
           print "no recent post by user!!!!"
    else:
       print "status code other than 200!!!"

get_user_recent_posts('shubham.is.here')