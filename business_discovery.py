import subprocess
import argparse, os, csv
import time
from defines import getCreds, makeApiCall
import sqlite3

if __name__ == '__main__':
            # Database oluştur
        db = sqlite3.connect('instagram.db')
        cursor = db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS kullanici_ayrintilari (username, user_id, name, follows_count, follower_count, media_count, website, profile_pic, biography)")



        filename = 'ig_business.csv'
        open(filename, 'w').close()
        input = open('ig_username.csv', 'r')
        content  = input.readlines()
        for line in content: 
                if line: 
                    ig_username = line.strip()
                    #Fonksiyon bildirildi
                    def getAccountInfo( params ) :
                        
                        endpointParams = dict() # parameter to send to the endpoint
                        endpointParams['fields'] = 'business_discovery.username(' + ig_username + '){id,name,follows_count,followers_count,media_count,website,profile_picture_url,biography}' # string of fields to get back with the request for the account
                        endpointParams['access_token'] = params['access_token'] # access token

                        url = params['endpoint_base'] + params['instagram_account_id'] # endpoint url

                        return makeApiCall( url, endpointParams, params['debug'] ) # make the api call

                params = getCreds() # creds'ler alındı
                params['debug'] = 'no' # debug ayarlandı
                response = getAccountInfo( params ) # apiye bilgileri almak için istek

                try:               
                    #Json'dan bilgileri al
                    user_id = response['json_data']['business_discovery']['id']
                    name = response['json_data']['business_discovery']['name']
                    follows_count = response['json_data']['business_discovery']['follows_count']
                    follower_count = response['json_data']['business_discovery']['followers_count']
                    media_count = response['json_data']['business_discovery']['media_count']
                    website = response['json_data']['business_discovery']['website']
                    profile_pic = response['json_data']['business_discovery']['profile_picture_url']
                    biography = response['json_data']['business_discovery']['biography']
                    create_time = response['json_data']['business_discovery']['created_time']
                    bio = str(biography.encode("utf-8"))
                    #bilgileri csv dosyasına ekle                    
                    with open(filename, 'a', encoding='utf-8') as csvfile:
                        employee_writer = csv.writer(csvfile, delimiter='\t', lineterminator='\r', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        employee_writer.writerow([ig_username,', ', name,', ', follows_count,', ', follower_count,', ', media_count,', ', user_id,', ', website,', ', profile_pic,', ', bio])
                    
                    #bilgileri veritabanına ekle
                    cursor.execute("INSERT INTO kullanici_ayrintilari VALUES(?,?,?,?,?,?,?,?,?)",(ig_username,user_id,name,follows_count,follower_count,media_count,website,profile_pic,bio))
                    db.commit()
                    print(create_time)
                    print(ig_username + ' --- Başarılı')
                except Exception as e:
                    print(ig_username + ' --- Başarısız')
                    print(e)
                time.sleep(10)  #Her api çağrısında 10 saniye gecikme ayarlandı
        db.close()