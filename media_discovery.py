import subprocess
import argparse, os, csv
import time
from defines import getCreds, makeApiCall
import sqlite3

if __name__ == '__main__':
        db = sqlite3.connect('instagram.db')
        cursor = db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS gönderi_ayrintlilari (username,media_datas)")


        filename = 'ig_media.csv'
        open(filename, 'w').close()
        input = open('ig_username.csv', 'r')
        content  = input.readlines()
        for line in content: 
                if line: 
                    ig_username = line.strip()
                    def getUserMedia( params, pagingUrl = '' ) :
    
                        endpointParams = dict() 
                        endpointParams['fields'] = 'business_discovery.username(' + ig_username + '){media{username,id,permalink,like_count,comments_count,media_type,media_url,timestamp,caption}}' # fields to get back
                        endpointParams['access_token'] = params['access_token'] 

                        if ( '' == pagingUrl ) : # ilk sayfayı getir
                            url = params['endpoint_base'] + params['instagram_account_id'] # endpoint url
                        else : # farklı sayfa getir
                            url = pagingUrl  # endpoint url

                        return makeApiCall( url, endpointParams, params['debug'] ) # api çağrısı yap

                    params = getCreds() #creds'leri al
                    params['debug'] = 'no' # debug ayarla
                    response = getUserMedia( params ) # apiden kullanıcı gönderilerini al
                    
                try:               
                    #Json'dan datayı al (data = veri)
                    user_post = response['json_data'] 
                    post = user_post['business_discovery']['media']['data']

                    #Datayı CSV'ye ekle
                    with open(filename, 'a', encoding='utf-8') as csvfile:
                        employee_writer = csv.writer(csvfile, delimiter='\t', lineterminator='\r', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                        count = 0
                        for pid in post:
                            if count == 0:                                
                                header = pid.keys()
                                count += 1
                            employee_writer.writerow([ig_username,', ', pid.values()])
                    
                    #Datayı veritabanına ekle
                    count == 0
                    for pid in post:
                        if count == 0:
                            header = pid.keys()
                            count +=1
                        values = str(pid.values())
                        cursor.execute("INSERT INTO gönderi_ayrintlilari VALUES(?,?)",(ig_username,values))
                        db.commit()                    
                    print(ig_username + ' --- Başarılı')
                except Exception as e:
                    print(ig_username + ' --- Başarısız')
                    print(e)
        db.close       