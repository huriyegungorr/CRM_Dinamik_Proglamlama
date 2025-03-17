import numpy as np

def musteri_destek_temsilcisi_atama(musteriler, temsilciler):
    """
    Zaman Karmaşıklığı:
    - Her müşteri için tüm temsilci kombinasyonlarını değerlendirdiğimiz için O(n * m) karmaşıklığı vardır.
    - n: müşteri sayısı, m: temsilci sayısı.
    """
    dp = {}
    atamalar = {}

    def ata(i, temsilci_kapasiteleri):
        if i >= len(musteriler):
            return 0, {}

        if (i, tuple(temsilci_kapasiteleri)) in dp:
            return dp[(i, tuple(temsilci_kapasiteleri))]

        en_iyi, en_iyi_atama = ata(i + 1, temsilci_kapasiteleri)

        for j in range(len(temsilciler)):
            if temsilci_kapasiteleri[j] > 0 and temsilciler[j][0] == musteriler[i][0]:
                yeni_kapasiteler = list(temsilci_kapasiteleri)
                yeni_kapasiteler[j] -= 1
                yeni_sonuc, yeni_atamalar = ata(i + 1, yeni_kapasiteler)
                yeni_sonuc += 1
                
                if yeni_sonuc > en_iyi:
                    en_iyi = yeni_sonuc
                    en_iyi_atama = yeni_atamalar.copy()
                    en_iyi_atama[musteriler[i]] = temsilciler[j][2]  

        dp[(i, tuple(temsilci_kapasiteleri))] = (en_iyi, en_iyi_atama)
        return en_iyi, en_iyi_atama

    max_atama, atamalar = ata(0, [temsilci[1] for temsilci in temsilciler])
    
    print("\n **Müşteri Temsilcisi Yönlendirme Sonuçları:**")
    for musteri, temsilci in atamalar.items():
        print(f" Müşteri {musteri} -> Temsilci {temsilci}")

    return max_atama

def pazarlama_yatirim_getirisi_maksimum(butce, kampanyalar):
    """
    Zaman Karmaşıklığı:
    - Knapsack DP tabanlı olduğu için O(n * B) karmaşıklığı vardır.
    - n: kampanya sayısı, B: bütçe limiti.
    """
    n = len(kampanyalar)
    dp = np.zeros((n + 1, butce + 1))
    secilen_kampanyalar = np.zeros((n + 1, butce + 1), dtype=object)

    for i in range(1, n + 1):
        maliyet, getiri, kampanya_id = kampanyalar[i - 1]
        for b in range(butce + 1):
            if maliyet <= b:
                if getiri + dp[i - 1][b - maliyet] > dp[i - 1][b]:
                    dp[i][b] = getiri + dp[i - 1][b - maliyet]
                    secilen_kampanyalar[i][b] = (secilen_kampanyalar[i - 1][b - maliyet] or []) + [kampanya_id]
                else:
                    dp[i][b] = dp[i - 1][b]
                    secilen_kampanyalar[i][b] = secilen_kampanyalar[i - 1][b]
            else:
                dp[i][b] = dp[i - 1][b]
                secilen_kampanyalar[i][b] = secilen_kampanyalar[i - 1][b]

    print("\n **Seçilen Pazarlama Kampanyaları:**")
    for kampanya in secilen_kampanyalar[n][butce] or []:
        print(f" Kampanya {kampanya} seçildi!")

    return dp[n][butce]

# Test Senaryosu
if __name__ == "__main__":
    musteriler = [("Istanbul", 1), ("Ankara", 2), ("Istanbul", 3)]
    temsilciler = [("Istanbul", 2, "T1"), ("Ankara", 1, "T2")]

    print("\n **Maksimum müşteri yönlendirme:**", musteri_destek_temsilcisi_atama(musteriler, temsilciler))

    kampanyalar = [(5, 10, "K1"), (10, 25, "K2"), (15, 40, "K3"), (7, 12, "K4")]
    butce = 20

    print("\n **En yüksek yatırım getirisi:**", pazarlama_yatirim_getirisi_maksimum(butce, kampanyalar))
