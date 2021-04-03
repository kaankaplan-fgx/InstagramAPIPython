import requests
import json

def getCreds() :

	creds = dict() # her şeyi tutan sözlük
	creds['access_token'] = 'access token' #tüm api çağrılarında kullanım için access token
	creds['client_id'] = 'client id' # client id 
	creds['client_secret'] = 'client secret' # client secret 
	creds['graph_domain'] = 'https://graph.facebook.com/' # api cağrıları için base domain
	creds['graph_version'] = 'v10.0' # graph api versiyon
	creds['endpoint_base'] = creds['graph_domain'] + creds['graph_version'] + '/' # temel endpoint domain ve versiyon
	creds['debug'] = 'no' # api çağrıları için debug mod ayarlanması
	creds['page_id'] = 'page id' # "get_user_facebook_page.py" çalıştırdıktan sonra page id"
	creds['instagram_account_id'] = 'account id' # "get_user_instagram_page.py" çalıştırdıktan sonra gelen account id
	creds['ig_username'] = 'username' # ig username to get details

	return creds

def makeApiCall( url, endpointParams, debug = 'no' ) :

	data = requests.get( url, endpointParams ) # get isteği

	response = dict() # yanıt bilgilerini tut
	response['url'] = url # çağrı url'si
	response['endpoint_params'] = endpointParams #endpoint'e gönderilicek parametreler
	response['endpoint_params_pretty'] = json.dumps( endpointParams, indent = 4 )
	response['json_data'] = json.loads( data.content ) # API'den gelen yanıt verileri
	response['json_data_pretty'] = json.dumps( response['json_data'], indent = 4 ) 

	if ( 'yes' == debug ) : # yanıt bilgileri
		displayApiCallData( response ) # yanıtı görüntüle

	return response # içeriğ al ve content'i döndür

def displayApiCallData( response ) :
	""" Print out to cli response from api call """

	print ("\nURL: ") 
	print (response['url']) # url çağrısını görüntüle
	print ("\nEndpoint Params: ") 
	print (response['endpoint_params_pretty']) 
	print ("\nResponse: ") 
	print (response['json_data_pretty']) 

