# CRM_Dinamik_Proglamlama  
Proje Açıklaması:  
Bu proje, bir CRM (Müşteri İlişkileri Yönetimi) Sistemi geliştirerek iki temel işlevi optimize etmeyi amaçlamaktadır:

1) Müşteri Destek Temsilcisi Yönlendirme:

Temsilcileri müşteri taleplerine göre en iyi şekilde yönlendirir.
Müşteri hizmetleri yükünü dengeler.
Dinamik programlama kullanarak maksimum müşteri memnuniyeti sağlanır.  

2)Pazarlama Kampanyası Seçimi:

Belirlenen bütçe ile en yüksek yatırım getirisini (ROI) sağlayan kampanyalar seçilir.
Kampanyaların maliyeti ve getirisi dikkate alınarak en iyi kombinasyon bulunur.
Bu proje, dinamik programlama (DP) teknikleriyle optimizasyon yaparak maliyetleri düşürmeyi ve müşteri memnuniyetini artırmayı hedefler.

Kullanılan Algoritmalar ve Zaman Karmaşıklıkları:  
Algoritma	Açıklama	Zaman Karmaşıklığı (Big-O)
Müşteri Temsilcisi Yönlendirme	Temsilcileri müşteri taleplerine en iyi şekilde yönlendirir (Knapsack DP)	O(n * m)
Pazarlama Kampanya Seçimi	Bütçeye göre en iyi pazarlama kombinasyonunu bulur (Knapsack DP)	O(n * B)

Kurulum ve Çalıştırma:  
1)Gerekli Bağımlılıkları Yükleyin
Python 3.x yüklü olduğundan emin olun ve ardından şu komutu çalıştırın:
pip install -r requirements.txt
2)Ana Python Kodunu Çalıştırın
python main.py  
3)Örnek Çıktı
Kod çalıştırıldığında müşteri temsilcileri ve pazarlama kampanyalarının en iyi kombinasyonu görüntülenecektir.

 Kullanılan Teknikler
 Dinamik Programlama (DP): Daha önce çözülen alt problemleri saklayarak hesaplama süresini azaltır.
 Knapsack Problemi Yaklaşımı: Hem müşteri yönlendirme hem de pazarlama seçiminde optimum kaynak tahsisini sağlar.
 Veri Yapıları: Tablo (2D DP array) kullanarak önceki hesaplamaları saklar ve tekrar işlem yapmayı önler.

 Neden Dinamik Programlama Kullandık?
1) Greedy (Açgözlü) Algoritmalardan Daha Etkili
Greedy algoritmalar her adımda en iyi kararı verir ancak küresel optimumu bulamayabilir.
DP ise tüm olasılıkları hesaplayarak en iyi sonucu garanti eder.

2) Brute Force (Kaba Kuvvet) Çok Yavaş
O(2^n) gibi üstel zaman karmaşıklığı olan yöntemler yerine, DP ile O(n*m) gibi polinomiyal zaman karmaşıklığı elde ettik.

3) Alt Problemleri Tekrar Hesaplamamak

Bellek kullanımı ile işlem süresini dengeler.
Hesaplanan sonuçlar saklanarak tekrar hesaplama önlenir.   

Örnek Senaryo ve Çıktı: CRM Sistemi  
![image](https://github.com/user-attachments/assets/c2f448b7-acdb-4fce-bec5-5f5bd9652922)


 Senaryo:
Bir müşteri destek ekibimiz var ve her temsilcinin belirli bir kapasitesi bulunuyor.
Müşteri taleplerini optimum şekilde yönlendirmek istiyoruz.

 Pazarlama Kampanyası:
Belirli bir bütçemiz var ve maksimum yatırım getirisi (ROI) elde etmek için en uygun kampanyaları seçmeliyiz.

 Bu sistem, şirketlerin müşteri desteğini ve pazarlama bütçesini en verimli şekilde yönetmesini sağlar.


 
