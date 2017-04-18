import requests #IMPORT LIBRARY BY REQUEST

# define function to enter user name entered by app uers nd desired task
def username():
    a  = raw_input("enter instagram user name =  ")
    print a

username()

#print all the option for user to do specific task
print " 1. \n get user id by username" \
          " 2. \n get user recent post" \
          " 3. \n like a post of user" \
          " 4. \n comment on a post of user" \
         "  5. \n get comment id of user " \
         " 6. \n delete the comment from a post of user " \
         " 7. \n get average no  of comments "


#using a access token for app
APP_ACCESS_TOKEN = '1560024934.53ba031.1ef6f902d8044a77bccbd08b0c200f96'
#using base url from instagram api
BASE_URL = 'https://api.instagram.com/v1'
payload  = {'access_token': APP_ACCESS_TOKEN} #payload to use like a post function


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
    request_url = (BASE_URL + '/users/search?q=%s&access_token=%s') % (insta_username , APP_ACCESS_TOKEN)
    print 'requesting url for data: ' + request_url
    search_results = requests.get(request_url).json()
    print search_results

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
           print recent_posts
           return recent_posts['data'][10]['id']
       else:
           print "no recent post by user!!!!"
    else:
       print "status code other than 200!!!"

get_user_recent_posts('shubham.is.here')

 #function define to like a instagram post by id
def like_a_post(insta_username):
    post_id =  get_user_recent_posts(insta_username)
    request_url = ( BASE_URL + '/media/%s/likes') % post_id
    like_a_post  = requests.post(request_url, payload).json()
    print like_a_post

    if like_a_post['meta']['code'] == 200:
        print "\n you got a post to like"
    else:
        print "\n try again!!"

like_a_post('shubham.is.here')


#define a function to comment
def comment_on_post(insta_username):
    post_id = get_user_recent_posts(insta_username)
    request_url = (BASE_URL + 'media/%s/comments') % (post_id)
    request_data = {'access_token': APP_ACCESS_TOKEN, 'text':'comment by access token owner'}
    get_comment = requests.post(request_url, request_data).json()
    if get_comment['meta']['code'] == 200:
      print "comment done"
    else:
      print "try agian!!! "
comment_on_post('shubham.is.here')

#define function to get comment id
def get_comment_id(insta_username):
    post_id = get_user_recent_posts(insta_username)
    request_url = ( BASE_URL + 'media/%s/comments?access_token=%s') % (post_id, APP_ACCESS_TOKEN)
    get_a_commentID = requests.get(request_url).json()
    wordInTheComment = raw_input("Enter a word that you think is in the comment:")
    if get_a_commentID['meta']['code'] == 200:
        for i in len(get_a_commentID['data']):
            if wordInTheComment in get_a_commentID['data'][i]['text']:
                print "comment found"
            return get_a_commentID['data'][i]['id']
        else:
            print "no comment found"
    else:
        print "code is other than 200"

get_comment_id('shubham.is.here')


#define function to delete a comment
def delete_comment(insta_username):
    media_id = get_comment_id(insta_username)
    request_url = ( BASE_URL + '/media/%s/comments/{comment-id}?access_token=%s') % (media_id , APP_ACCESS_TOKEN)
    delete_comment  = requests.get(request_url).json()
    word_in_comment = raw_input("enter word u thing in comment=")
    if delete_comment['meta']['code'] == 200:
       for i in range(len(delete_comment['data'])):
         if word_in_comment in delete_comment['data'][i]['text']:
           print "comment found "
           request_url = ( BASE_URL + '/media/%s/comments/{comment-id}?access_token=%s' ) % (media_id , APP_ACCESS_TOKEN)
           delete_comment = requests.get(request_url).json()
           print " comment deleted"
           return delete_comment['data'][i]['id']
         else:
           print "no comment found"
       else:
         print "error"

delete_comment('shubham.is.here')

#define function to print words of every comment
def average_num_of_words_in_comment(insta_username):
    media_id  = comment_on_post(insta_username)
    request_url = ( BASE_URL + ' media/%s/comments?access_token=%s ') % ( media_id ,APP_ACCESS_TOKEN)
    get_list_of_comments = requests.get(request_url).json()
    print get_list_of_comments
    for comment in get_list_of_comments ['data']:
        print comment ['text'].split()
        print "total no of word in comment = %s\n" % (len(comment['text'].split()))

average_num_of_words_in_comment(get_comment_id('shubham.is.here'))

#make a control flow to select desired task to with selected user

select_option = raw_input("enter the derised task to do with selected user")

if select_option == 1:
    get_user_id_by_username('shubhsm.is.here')
elif select_option == 2:
    get_user_recent_posts('shubhsm.is.here')
elif select_option == 3:
    like_a_post('shubhsm.is.here')
elif select_option == 4:
    comment_on_post('shubhsm.is.here')
elif select_option ==5:
    get_comment_id('shubhsm.is.here')
elif select_option ==6:
    delete_comment('shubhsm.is.here')
elif select_option == 7:
    average_num_of_words_in_comment('shubhsm.is.here')
else :        print " invalid selection"