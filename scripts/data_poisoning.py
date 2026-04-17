"""
=============================================================================
 ADPS-Core : Veri Zehirleme Aracı (Konsept Çalışması)
=============================================================================
Bu betik (script), 'Katman 1: Algoritmik İtaatsizlik' felsefesinin bir
kanıtı (proof-of-concept) niteliğindedir. Alakasız ve birbirinden tamamen 
uzak konularda rastgele arama sorguları oluşturarak bunları arka planda
çalıştırır. Amacı, veri simsarları (data brokers) tarafından sizin
hakkınızda oluşturulan tahmin ve gözetim profillerini kirletmek ve 
yanıltmaktır.

Uyarı: Eğitsel/Kavramsal amaçlıdır. Platformların hizmet şartlarına uygun 
kullanın.
=============================================================================
"""

import time
import random
import requests

# Sınıflandırma algoritmalarının kafasını karıştıracak birbirinden kopuk konular
TOPICS = [
    "kuantum bilgisayarların çalışma mantığı", "evde koyun yünü nasıl örülür", 
    "bizans imparatorluğu'nun tarihi", "1980'lerin en iyi heavy metal grupları",
    "ileri düzey organik kimya problemleri", "köpekler için vegan tarifler",
    "internetten lüks yat satın alma rehberi", "varoluşçuluk ve nihilizm farkı",
    "moğolistan ulan batur ucuz uçak bileti", "antik yunanca dili nasıl öğrenilir",
    "kendin yap güneş paneli kurulumu", "yapay zeka hizalama problemi",
    "stoacı felsefe ve iç huzur", "balkonda sırık domates yetiştiriciliği",
    "şehirde gerilla bahçecilik (guerrilla gardening)", "amerikan merkez bankası nasıl işler"
]

SEARCH_ENGINES = [
    "https://duckduckgo.com/?q={}",
    "https://www.ecosia.org/search?q={}"
]

def generate_noise(iterations=5):
    print("[*] Veri Zehirleme (Data Poisoning) Protokolü Başlatılıyor...")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) ADPS-Obfuscator/1.0"
    }

    for i in range(iterations):
        query = random.choice(TOPICS)
        # Boşlukları basit URL kodlamasına çevir
        encoded_query = query.replace(" ", "+")
        engine = random.choice(SEARCH_ENGINES).format(encoded_query)
        
        print(f"[-] Sahte ilgi alanı enjekte ediliyor: '{query}'")
        try:
            # Büyük dosya yüklemelerini önlemek için sadece HEAD isteği (request) gönder
            response = requests.head(engine, headers=headers, timeout=5)
            print(f"    [+] Durum: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"    [!] İstek başarısız oldu: {e}")
        
        # İnsan davranışını taklit etmek için rastgele bekleme süresi
        sleep_time = random.uniform(2.0, 7.0)
        time.sleep(sleep_time)

if __name__ == "__main__":
    generate_noise()
    print("[*] Protokol Tamamlandı. Gözetim algoritmasının profili zehirlendi.")
