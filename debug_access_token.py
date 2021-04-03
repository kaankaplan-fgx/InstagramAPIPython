from defines import getCreds, makeApiCall
import datetime

def debugAccessToken( params ) :

	endpointParams = dict() # endpoint'e gönderilicek parametreler
	endpointParams['input_token'] = params['access_token'] # access tokenini gir
	endpointParams['access_token'] = params['access_token'] # hata ayıklama bilgilerini almak için access token

	url = params['graph_domain'] + '/debug_token' # endpoint url

	return makeApiCall( url, endpointParams, params['debug'] ) #api çağrısı döndür

params = getCreds() # creds'leri al
params['debug'] = 'yes' # debug'u ayarla
response = debugAccessToken( params ) # apiye bilgileri almak için istek

print ("\nData Access Expires at: ") # label
print (datetime.datetime.fromtimestamp( response['json_data']['data']['data_access_expires_at'] )) # token'in süresi dolduğunda göster

print ("\nToken Expires at: ") # label
print (datetime.datetime.fromtimestamp( response['json_data']['data']['expires_at'] )) # token'in süresi dolduğunda göster