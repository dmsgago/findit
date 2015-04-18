from bottle import route, default_app, get, post, template, request, static_file, response
import requests, os
from requests_oauthlib import OAuth1
from urlpase import parse_qs
from bottle import TEMPLATE_PATH
TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi/views/'))

application=default_app()


# Función para obtener el token de solicitud y su secreto
def get_request_token():
    oauth = OAuth1(CONSUMER_KEY, client_secret=CONSUMER_SECRET)
    r = requests.post(url=REQUEST_TOKEN_URL, auth=oauth)
    credentials = parse_qs(r.content)
    TOKENS["request_token"] = credentials.get('oauth_token')[0]
    TOKENS["request_token_secret"] = credentials.get('oauth_token_secret')[0]
    authorize_url = AUTHENTICATE_URL + TOKENS["request_token"]
    return template('index.tpl', authorize_url=authorize_url)

# OAuth1
REQUEST_TOKEN_URL = " https://api.twitter.com/oauth/request_token"
AUTHENTICATE_URL = "https://api.twitter.com/oauth/authenticate?oauth_token="
ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"
CONSUMER_KEY = "otZEhc6iU81FfeaY4PFs91y9N"
CONSUMER_SECRET = "8ZspqHV33gQLeyHH2maeMLEiRKOgUBRY1TsdBVIL2PIFhxFzI7"
TOKENS = {}

@route('/')
def index():
    get_request_token()
