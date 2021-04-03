import subprocess
import argparse, os, csv
import time
from defines import getCreds, makeApiCall
import sys
import sqlite3

if __name__ == '__main__':
        db = sqlite3.connect('instagram.db')
        cursor = db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS en_yeni_hashtag (username,hashtag_data)")

        filename = 'ig_hashtag_recent_media.csv'
        open(filename, 'w').close()
        input = open('ig_hashtag_input.csv', 'r')
        content  = input.readlines()
        for line in content: 
                if line: 
                    ig_hashtag = line.strip()
                    def getHashtagInfo( params ) :
                        endpointParams = dict() # endpoint'e gönderilicek parametreler
                        endpointParams['user_id'] = params['instagram_account_id'] # istek yapılan kullanıcı id'si
                        endpointParams['q'] = ig_hashtag # hashtag ismi
                        endpointParams['fields'] = 'id,name' # geri alınacak alanlar
                        endpointParams['access_token'] = params['access_token'] # access token

                        url = params['endpoint_base'] + 'ig_hashtag_search' # endpoint url

                        return makeApiCall( url, endpointParams, params['debug'] )
            
                    
                    def getHashtagMedia( params ) :

                        endpointParams = dict() # endpoint'e gönderilicek parametreler
                        endpointParams['user_id'] = params['instagram_account_id'] # istek yapılan kullanıcı id'si
                        endpointParams['fields'] = 'id,permalink,comments_count,like_count,media_type,media_url,timestamp,caption' # eri alınacak alanlar
                        endpointParams['access_token'] = params['access_token'] # access token
                        
                        hashtagInfoResponse = getHashtagInfo( params ) # apiye çağrı yap
                        params['hashtag_id'] = hashtagInfoResponse['json_data']['data'][0]['id']
                        
                        params['type'] = 'recent_media' # hashtag için en iyi medyayı almak için çağrıyı ayarla

                        url = params['endpoint_base'] + params['hashtag_id'] + '/' + params['type'] # endpoint url

                        return makeApiCall( url, endpointParams, params['debug'] ) # api isteğini döndür

                    params = getCreds() # creds'leri al
                    params['debug'] = 'no' # debug ayarla
                    response = getHashtagMedia( params ) # kullanıcıların medyalarını apiden al
                

                try:               
                    #JSON'dan datayı al
                    hashtag_post = response['json_data']['data']

                    #datayı CSV'ye ekle
                    with open(filename, 'a', encoding='utf-8') as csvfile:
                        employee_writer = csv.writer(csvfile, delimiter='\t', lineterminator='\r', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        for pid in hashtag_post:
                            employee_writer.writerow([ig_hashtag,', ', pid.values()])

                    #veriyi veritabanına ekle
                    for pid in hashtag_post:
                        values = str(pid.values())
                        cursor.execute("INSERT INTO en_yeni_hashtag VALUES(?,?)",(ig_hashtag,values))
                        db.commit()

                    print(ig_hashtag + ' --- Başarılı')
                except:
                    print(ig_hashtag + ' --- Başarısız')
        db.close()