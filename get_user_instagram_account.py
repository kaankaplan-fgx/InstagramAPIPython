from defines import getCreds, makeApiCall

def getInstagramAccount( params ) :

	endpointParams = dict() #
	endpointParams['access_token'] = params['access_token'] 
	endpointParams['fields'] = 'instagram_business_account' 

	url = params['endpoint_base'] + params['page_id'] 

	return makeApiCall( url, endpointParams, params['debug'] ) # api çağrısı yap

params = getCreds() # credsleri al
params['debug'] = 'yes' # debug'ayarlra
response = getInstagramAccount( params ) # debug bilgisini al

print ("\n---- INSTAGRAM ACCOUNT INFO ----\n")
print ("Page Id:") 
print (response['json_data']['id']) 
print ("\nInstagram Business Account Id:") 
print (response['json_data']['instagram_business_account']['id']) 