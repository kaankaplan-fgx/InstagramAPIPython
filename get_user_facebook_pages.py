from defines import getCreds, makeApiCall

def getUserPages( params ) :

	endpointParams = dict() 
	endpointParams['access_token'] = params['access_token'] 

	url = params['endpoint_base'] + 'me/accounts' 

	return makeApiCall( url, endpointParams, params['debug'] ) # api çağrısı yap

params = getCreds() # credsleri'al
params['debug'] = 'no' # debug ayarla
response = getUserPages( params ) # debug infoyu al

print ("\n---- FACEBOOK PAGE INFO ----\n") #
print ("Page Name:") 
print (response['json_data']['data'][0]['name']) 
print ("\nPage Category:") 
print (response['json_data']['data'][0]['category']) 
print ("\nPage Id:") 
print (response['json_data']['data'][0]['id']) 