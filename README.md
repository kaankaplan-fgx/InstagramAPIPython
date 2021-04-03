Gerekli Kütüphaneler

1. subprocess
2. argparse
3. os
4. csv
5. requests
6. json
7. sqlite


```
## KULLANMAK İÇİN 
1. 1 Saat için geçerli Access Token oluşturun

2. Access Token'i kopyalayın ve şuradaki alana yapıştırın ->  ***defines.py***

3. Developers.facebook.com Uygulamasından ** Client ID ** ve ** Client Secret Key ** kopyalayın

4. Şimdi *** Graph API *** bağlantısını kontrol etmek için *** debug_access_token.py *** dosyasını çalıştırın

5. 60 Gün boyunca geçerli Access Token almak için şimdi *** get_long_lived_access_token.py *** çalıştırın ve bunu *** defines.py alanına girin

6. Şimdi ** Facebook Sayfa Kimliğini ** almak için *** get_user_facebook_pages.py *** çalıştırın & Bunu *** defines.py alanına girin ***

7. Şimdi ** Instagram Hesap Kimliğini ** almak için *** get_user_instagram_account.py *** çalıştırın ve bunu *** defines.py alanına girin ***

8. Şimdi ayrıntılarını almak istediğiniz Instagram Kullanıcı Adını *** ig_username.csv *** dosyasına girin

9. Şimdi *** ig_username.csv *** dosyasına girdiğiniz kullanıcı adlarının ayrıntılarını almak için *** business_discovery.py *** çalıştırın

10. Şimdi yeni oluşturulan *** ig_business.csv *** dosyasını açın ve istenen sonuçları doğrulayın ve veritabanına bakın.

11. Şimdi *** ig_username.csv *** dosyasına girdiğiniz kullanıcı adlarının ayrıntılarını almak için *** media_discovery.py *** çalıştırın

12. Şimdi yeni oluşturulan *** ig_media.csv *** dosyasını açın ve istenen sonuçları doğrulayın ve veritabanına bakın.

13. Şimdi Gönderiyi almak istediğiniz Instagram Hashtag'i *** ig_hashtag_input.csv *** dosyasına girin

14. Şimdi *** ig_hashtag_input.csv *** dosyasına girdiğiniz hashtag'ların ayrıntılarını almak için *** hashtag_discovery_recent_media.py *** dosyasını çalıştırın (en yeniler)

15. Şimdi yeni oluşturulan *** ig_hashtag_top_media.csv *** dosyasını açın ve istenen sonuçları doğrulayın ve veritabanına bakın

16. Şimdi *** ig_hashtag_input.csv *** dosyasına girdiğiniz hashtag'ların ayrıntılarını almak için *** hashtag_discovery_top_media.py *** dosyasını çalıştırın(en popülerler)

27. Şimdi yeni oluşturulan *** ig_hashtag_top_media.csv *** dosyasını açın ve istenen sonuçları doğrulayın ve veritabanına bakın

28. Şimdi verilerin hepsi veritabanına ve gerekli csv dosyalarına yüklenmiştir.


