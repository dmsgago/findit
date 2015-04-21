
# -*- coding: utf-8 -*-
from bottle import default_app, get, post, template, request, static_file, response
import requests
from requests_oauthlib import OAuth1
from urlparse import parse_qs
from bottle import TEMPLATE_PATH
TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi/views/'))

application=default_app()

# OAuth1
REQUEST_TOKEN_URL = " https://api.twitter.com/oauth/request_token"
AUTHENTICATE_URL = "https://api.twitter.com/oauth/authenticate?oauth_token="
ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"
CONSUMER_KEY = "otZEhc6iU81FfeaY4PFs91y9N"
CONSUMER_SECRET = "8ZspqHV33gQLeyHH2maeMLEiRKOgUBRY1TsdBVIL2PIFhxFzI7"
TOKENS = {}


# Funcion para obtener el token de solicitud y su secreto
def get_request_token():
    oauth = OAuth1(CONSUMER_KEY,client_secret=CONSUMER_SECRET)
    r = requests.post(url=REQUEST_TOKEN_URL,auth=oauth)
    credentials = parse_qs(r.content)
    TOKENS["request_token"] = credentials.get('oauth_token')[0]
    TOKENS["request_token_secret"] = credentials.get('oauth_token_secret')[0]
    
'''
# Funcion que devuelve a la aplicacion un token de acceso
def get_access_token(TOKENS):
    oauth = OAuth1(CONSUMER_KEY,
                   client_secret=CONSUMER_SECRET,
                   resource_owner_key=TOKENS["request_token"],
                   resource_owner_secret=TOKENS["request_token_secret"],
                   verifier=TOKENS["verifier"],
    )
    r = requests.post(url=ACCESS_TOKEN_URL, auth=oauth)
    credentials = parse_qs(r.content)
    TOKENS["access_token"] = credentials.get('oauth_token')[0]
    TOKENS["access_token_secret"] = credentials.get('oauth_token_secret')[0]
    return template('buscador.tpl')
'''
@get('/')
def index():
    get_request_token()
    authorize_url = AUTHENTICATE_URL + TOKENS["request_token"]
    return template('index.tpl', authorize_url=authorize_url)
'''
# CALLBACK URL, Pagina que se carga tras la autorizacion del usuario
@get('/map')
def get_verifier():
    TOKENS["verifier"] = request.query.oauth_verifier
    get_access_token(TOKENS)

# Carga el buscador
@post('/map')
def buscador_submit():
    hashtag = request.forms.get("hashtag")
    oauth = OAuth1(CONSUMER_KEY,
                   client_secret=CONSUMER_SECRET,
                   resource_owner_key=TOKENS["access_token"],
                   resource_owner_secret=TOKENS["access_token_secret"])
 
    url = 'https://api.twitter.com/1.1/search/tweets.json?q='
 
    r = requests.post(url=url+hashtag+'result_type=recent',
                      data={"status":hashtag},
                      auth=oauth)
    if r.status_code == 200:
        return template('mapa.tpl')
    else:
        return "<p>Hubo un problema en el buscador</p>"
'''
