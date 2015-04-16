from bottle import route, default_app, get, post, template, request, static_file, response
import requests
from requests_oauthlib import OAuth1
from urlpase import parse_qs

# OAuth1
REQUEST_TOKEN_URL = " https://api.twitter.com/oauth/request_token"
AUTHENTICATE_URL = "https://api.twitter.com/oauth/authenticate?oauth_token="
ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"
CONSUMER_KEY = " ZtDMoDKKfSfIVLitOBt6Q3PVZ"
CONSUMER_SECRET = "GxuEDZkEBqysEwfYnsAJFM7omrVDWGUpl2riDH5YxMYNIyqNLb"
TOKENS = {}

@route('/')
def index():
    get_request_token()
    

# This must be added in order to do correct path lookups for the views
import os
from bottle import TEMPLATE_PATH
TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi/views/')) 

application=default_app()
