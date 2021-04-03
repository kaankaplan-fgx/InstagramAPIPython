from defines import getCreds, makeApiCall

def getLongLivedAccessToken( params ) :

	endpointParams = dict() 
	endpointParams['grant_type'] = 'fb_exchange_token' 
	endpointParams['client_id'] = params['client_id'] 
	endpointParams['client_secret'] = params['client_secret'] 
	endpointParams['fb_exchange_token'] = params['access_token'] # access tokeni uzun ömürlü tokenle değiştir

	url = params['endpoint_base'] + 'oauth/access_token?' # son url

	return makeApiCall( url, endpointParams, params['debug'] ) # api çağrısı yap

params = getCreds() # cred'leri al
params['debug'] = 'yes' # debug'ua ayarla
response = getLongLivedAccessToken( params ) # apiye istek at

print ("\n ---- ACCESS TOKEN INFO ----\n") 
print ("Access Token:")  
print (response['json_data']['access_token']) # access tokeni görüntüle