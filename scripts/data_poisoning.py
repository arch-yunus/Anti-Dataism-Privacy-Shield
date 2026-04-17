"""
=============================================================================
 ADPS-Core : Data Poisoning Tool (Concept)
=============================================================================
This script is a proof-of-concept for 'Layer 1: Algorithmic Disobedience'.
It randomly generates search queries from a list of disparate topics and 
executes them in the background, polluting the predictive profile built 
by data brokers.

Disclaimer: Use responsibly. Ensure compliance with terms of service.
=============================================================================
"""

import time
import random
import requests

# A diverse set of topics to confuse classification algorithms
TOPICS = [
    "quantum computing basics", "how to knit a sweater", 
    "history of the Byzantine Empire", "best heavy metal bands 1980s",
    "advanced organic chemistry tutorials", "vegan recipes for dogs",
    "buy luxury yachts online", "existentialism vs nihilism",
    "cheap flights to Ulaanbaatar", "learning ancient Greek",
    "diy solar panels", "artificial intelligence alignment",
    "the philosophy of stoicism", "how to grow tomatoes",
    "urban guerrilla gardening", "understanding the federal reserve"
]

SEARCH_ENGINES = [
    "https://duckduckgo.com/?q={}",
    "https://www.ecosia.org/search?q={}"
]

def generate_noise(iterations=5):
    print("[*] Initiating Data Poisoning Protocol...")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) ADPS-Obfuscator/1.0"
    }

    for i in range(iterations):
        query = random.choice(TOPICS)
        # Simple URL encoding replacement for spaces
        encoded_query = query.replace(" ", "+")
        engine = random.choice(SEARCH_ENGINES).format(encoded_query)
        
        print(f"[-] Injecting fake interest: '{query}'")
        try:
            # Send a HEAD request to avoid downloading massive payloads
            response = requests.head(engine, headers=headers, timeout=5)
            print(f"    [+] Status: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"    [!] Request failed: {e}")
        
        # Random sleep to mimic human behavior
        sleep_time = random.uniform(2.0, 7.0)
        time.sleep(sleep_time)

if __name__ == "__main__":
    generate_noise()
    print("[*] Protocol Complete. Profile polluted.")
