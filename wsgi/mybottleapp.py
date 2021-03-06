# -*- coding: utf-8 -*-
from bottle import default_app, get, post, template, request, static_file, response
import requests
import json
from requests_oauthlib import OAuth1
from urlparse import parse_qs

# Constantes OAuth1


REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
AUTHENTICATE_URL = "https://api.twitter.com/oauth/authenticate?oauth_token="
ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"

CONSUMER_KEY = "otZEhc6iU81FfeaY4PFs91y9N"
CONSUMER_SECRET = "8ZspqHV33gQLeyHH2maeMLEiRKOgUBRY1TsdBVIL2PIFhxFzI7"

TOKENS = {}

elementos = {}
ubicaciones = []

# Funcion para obtener el token de solicitud y su secreto
def get_request_token():
    oauth = OAuth1(CONSUMER_KEY,
                   client_secret=CONSUMER_SECRET,
    )
    r = requests.post(url=REQUEST_TOKEN_URL, auth=oauth)
    credentials = parse_qs(r.content)
    TOKENS["request_token"] = credentials.get('oauth_token')[0]
    TOKENS["request_token_secret"] = credentials.get('oauth_token_secret')[0]

# Funcion que almacena el token de acceso y su secreto en el diccionario TOKENS
def get_access_token(TOKENS):
    oauth = OAuth1(CONSUMER_KEY,
                   client_secret=CONSUMER_SECRET,
                   resource_owner_key=TOKENS["request_token"],
                   resource_owner_secret=TOKENS["request_token_secret"],
                   verifier=TOKENS["verifier"],)
    r = requests.post(url=ACCESS_TOKEN_URL, auth=oauth)
    credentials = parse_qs(r.content)
    TOKENS["access_token"] = credentials.get('oauth_token')[0]
    TOKENS["access_token_secret"] = credentials.get('oauth_token_secret')[0]

def send_oauth(TOKENS):
  oauth = OAuth1(CONSUMER_KEY,
                   client_secret=CONSUMER_SECRET,
                   resource_owner_key=TOKENS['access_token'],
                   resource_owner_secret=TOKENS['access_token_secret'])
  return oauth
    
@get('/')
def index():
    get_request_token()
    authorize_url = AUTHENTICATE_URL + TOKENS["request_token"]
    return template('index.tpl', authorize_url=authorize_url)

# CALLBACK URL, Pagina que se carga tras la autorizacion del usuario
@get('/map')
def get_verifier():
    TOKENS["verifier"] = request.query.oauth_verifier
    get_access_token(TOKENS)
    return template('buscador.tpl')

# Recibe el dato a buscar y utiliza la API de Twitter para conseguir el fichero JSON
@post('/map')
def findit():
    tipobusqueda = request.forms.get("TipoBusqueda")
    ubicaciones = []
    tuit = []
    if tipobusqueda == "0":
        elementos["q"] = request.forms.get("hashtag")
        elementos["count"] = "100"
        oauth = send_oauth(TOKENS)
        url = "https://api.twitter.com/1.1/search/tweets.json"
        r = requests.get(url, params=elementos, auth=oauth)
        if r.status_code == 200:
            respuesta = r.json()
            # Recorre cada tuit
            for tweet in respuesta["statuses"]:                
                if tweet["geo"] != None:
                    # Comprueba que la geolocalizacion no es cero
                    if tweet["geo"]["coordinates"][0] != 0 and tweet["geo"]["coordinates"][1] != 0:
                        # Almacena la ubicacion en una lista
                        ubicaciones.append(tweet["geo"]["coordinates"])
                        imagen = str(tweet["user"]["profile_image_url"].encode("utf-8"))
                        texto = str(tweet["text"].encode("utf-8"))
                        nombre = str(tweet["user"]["screen_name"].encode("utf-8"))
                        fecha = tweet["created_at"].encode("utf-8")
                        fecha = fecha[:19]
                        tuit.append("<img src='"+imagen+"' style='float:left; padding: 5px;' /><a href='https://twitter.com/"+nombre+"'><strong>"+nombre+"</strong></a>: "+texto+" ("+fecha+")")
        else:
            return ('<p>JSON no obtenido.</p>')

        # Comprueba que se han obtenido ubicaciones
        if len(ubicaciones) == 0:
            return template('nogeo.tpl')
        else:
            return template('mapa.tpl', ubicaciones=ubicaciones, tuit=tuit)

    #Busqueda por nombre de usuario
    else:
        elementos["screen_name"] = request.forms.get("username")
        elementos["count"] = "200"
        oauth = send_oauth(TOKENS)
        url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
        r = requests.get(url, params=elementos, auth=oauth)        
        if r.status_code == 200:
            respuesta = r.json()
            # Recorre cada tuit
            for tweet in respuesta:
                if tweet["geo"] != None:
                    # Comprueba que la geolocalizacion no es cero
                    if tweet["geo"]["coordinates"][0] != 0 and tweet["geo"]["coordinates"][1] != 0:
                        # Almacena la ubicacion en una lista
                        ubicaciones.append(tweet["geo"]["coordinates"])
                        #Almacena los datos del tuit
                        imagen = tweet["user"]["profile_image_url"].encode("utf-8", "ignore")
                        texto = tweet["text"].encode("utf-8", "ignore")
                        nombre = tweet["user"]["screen_name"].encode("utf-8", "ignore")
                        fecha = tweet["created_at"].encode("utf-8")
                        fecha = fecha[:19]
                        tuit.append("<img src='"+imagen+"' style='float:left; padding: 5px;' /><a href='https://twitter.com/"+nombre+"'><strong>"+nombre+"</strong></a>: "+texto+" ("+fecha+")")
        else:
            return ('<p>JSON no obtenido.</p>')

        # Comprueba que se han obtenido ubicaciones
        if len(ubicaciones) == 0:
            return template('nogeo.tpl')
        else:
            return template('mapa.tpl', ubicaciones=ubicaciones, tuit=tuit)

# This must be added in order to do correct path lookups for the views
import os
from bottle import TEMPLATE_PATH
TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi/views/'))

application=default_app()
