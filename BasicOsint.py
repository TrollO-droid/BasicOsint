#Telegram: @TrollOffical
import os
import sys
import time
import threading
import subprocess

# Renkler
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
RESET = "\033[0m"

# Otomatik Kütüphane Yükleyici
REQUIRED_MODULES = [
    "requests",
    "phonenumbers",
    "ipwhois",
    "whois"
]

def install_missing_modules():
    def animate():
        animation = "|/-\\"
        idx = 0
        while not done:
            print(f"\r{CYAN}Lütfen bekleyin, gerekli kütüphaneler indiriliyor... {animation[idx % len(animation)]} {RESET}", end="")
            idx += 1
            time.sleep(0.1)

    global done
    done = False
    t = threading.Thread(target=animate)
    t.start()

    for module in REQUIRED_MODULES:
        try:
            __import__(module)
        except ImportError:
            subprocess.call([sys.executable, "-m", "pip", "install", module])

    done = True
    time.sleep(0.3)
    print(f"\n{GREEN}✓ Kütüphaneler yüklendi. Devam ediliyor...{RESET}")
    print(f"{BLUE}İletişim: Tg:@TrollOffical{RESET}")
    time.sleep(1.5)

install_missing_modules()

# Kütüphaneleri yükledikten sonra import et
import requests
import phonenumbers
from phonenumbers import geocoder, carrier
from ipwhois import IPWhois
import whois
import random
import string

def ip_lookup():
    ip = input(f"{CYAN}IP adresini girin: {RESET}")
    try:
        print(f"\n{YELLOW}[+] Temel IP bilgisi:{RESET}")
        obj = IPWhois(ip)
        results = obj.lookup_rdap()
        print(f"  Network Name: {results.get('network', {}).get('name')}")
        print(f"  ASN: {results.get('asn')}")
        print(f"  Country: {results.get('asn_country_code')}")

        print(f"\n{YELLOW}[+] GeoIP bilgisi:{RESET}")
        geo = requests.get(f"https://ipapi.co/{ip}/json").json()
        for key in ["ip", "city", "region", "country_name", "org", "latitude", "longitude"]:
            print(f"  {key.capitalize()}: {geo.get(key)}")
    except Exception as e:
        print(f"{RED}Hata: {e}{RESET}")

def phone_lookup():
    number = input(f"{CYAN}Telefon numarasını uluslararası formatta girin (örn: +905xxxxxxxxx): {RESET}")
    try:
        parsed_number = phonenumbers.parse(number)
        print(f"\n{YELLOW}[+] Telefon Bilgisi:{RESET}")
        print(f"  Ülke: {geocoder.description_for_number(parsed_number, 'tr')}")
        print(f"  Operatör: {carrier.name_for_number(parsed_number, 'tr')}")
        print(f"  Geçerli mi?: {phonenumbers.is_valid_number(parsed_number)}")
        print(f"  Olası mı?: {phonenumbers.is_possible_number(parsed_number)}")
    except Exception as e:
        print(f"{RED}Hata: {e}{RESET}")

def whois_lookup():
    domain = input(f"{CYAN}Alan adını girin (örn: google.com): {RESET}")
    try:
        w = whois.whois(domain)
        print(f"\n{YELLOW}[+] WHOIS Bilgisi:{RESET}")
        for key in ["domain_name", "registrar", "creation_date", "expiration_date", "emails"]:
            print(f"  {key.capitalize()}: {w.get(key)}")
    except Exception as e:
        print(f"{RED}Hata: {e}{RESET}")

def password_generator():
    try:
        length = int(input(f"{CYAN}Kaç haneli şifre istersiniz?: {RESET}"))
        chars = string.ascii_letters + string.digits
        password = ''.join(random.choice(chars) for _ in range(length))
        print(f"\n{GREEN}[+] Oluşturulan Şifre: {password}{RESET}")
    except:
        print(f"{RED}Lütfen geçerli bir sayı girin.{RESET}")

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def menu():
    while True:
        clear()
        # ASCII SANATI ALANI
        print(f"""{BLUE}
 ▄▄▄▄    ▄▄▄        ██████  ██▓ ▄████▄      ▒█████    ██████  ██▓ ███▄    █ ▄▄▄█████▓
▓█████▄ ▒████▄    ▒██    ▒ ▓██▒▒██▀ ▀█     ▒██▒  ██▒▒██    ▒ ▓██▒ ██ ▀█   █ ▓  ██▒ ▓▒
▒██▒ ▄██▒██  ▀█▄  ░ ▓██▄   ▒██▒▒▓█    ▄    ▒██░  ██▒░ ▓██▄   ▒██▒▓██  ▀█ ██▒▒ ▓██░ ▒░
▒██░█▀  ░██▄▄▄▄██   ▒   ██▒░██░▒▓▓▄ ▄██▒   ▒██   ██░  ▒   ██▒░██░▓██▒  ▐▌██▒░ ▓██▓ ░ 
░▓█  ▀█▓ ▓█   ▓██▒▒██████▒▒░██░▒ ▓███▀ ░   ░ ████▓▒░▒██████▒▒░██░▒██░   ▓██░  ▒██▒ ░ 
░▒▓███▀▒ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░░▓  ░ ░▒ ▒  ░   ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░▓  ░ ▒░   ▒ ▒   ▒ ░░   
▒░▒   ░   ▒   ▒▒ ░░ ░▒  ░ ░ ▒ ░  ░  ▒        ░ ▒ ▒░ ░ ░▒  ░ ░ ▒ ░░ ░░   ░ ▒░    ░    
 ░    ░   ░   ▒   ░  ░  ░   ▒ ░░           ░ ░ ░ ▒  ░  ░  ░   ▒ ░   ░   ░ ░   ░      
 ░            ░  ░      ░   ░  ░ ░             ░ ░        ░   ░           ░          
      ░                        ░                                               
{RESET}{CYAN}Created By:@TrollOffical{RESET}
""")

        print(f"{CYAN}========== TOOL MENÜ =========={RESET}")
        print(f"{GREEN}1.{RESET} IP Adresi Bilgisi + GeoIP")
        print(f"{GREEN}2.{RESET} Telefon Numarası Bilgisi")
        print(f"{GREEN}3.{RESET} WHOIS Sorgusu")
        print(f"{GREEN}4.{RESET} Rastgele Şifre Üret")
        print(f"{GREEN}5.{RESET} Çıkış")
        secim = input(f"\n{YELLOW}Seçiminiz: {RESET}")

        if secim == "1":
            ip_lookup()
        elif secim == "2":
            phone_lookup()
        elif secim == "3":
            whois_lookup()
        elif secim == "4":
            password_generator()
        elif secim == "5":
            print(f"{CYAN}Çıkılıyor...{RESET}")
            break
        else:
            print(f"{RED}Geçersiz seçim!{RESET}")
        input(f"\n{CYAN}Devam etmek için Enter tuşuna bas...{RESET}")

if __name__ == "__main__":
    menu()
#Telegram: @TrollOffical