import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from colorama import init, Fore
import os
from threading import Thread
from os import system

init(autoreset=True)

def get_links_and_images(url, include_images):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        links = []
        images = []

        for link in soup.find_all("a"):
            href = link.get("href")
            if href and not href.startswith("#"):
                absolute_url = urljoin(url, href)
                parsed_url = urlparse(absolute_url)
                if parsed_url.scheme in ("http", "https") and parsed_url.netloc:
                    links.append(absolute_url)

        if include_images:
            for img in soup.find_all("img"):
                src = img.get("src")
                if src:
                    absolute_src = urljoin(url, src)
                    images.append(absolute_src)

        return links, images

    except Exception as e:
        print(f"{Fore.RED}{url} adresinden linkler ve görseller alınırken bir hata oluştu: {e}")
        return [], []

def crawl(start_url, depth, include_images, keywords, save_links_option, filename):
    visited = set()  # Ziyaret edilen linkleri saklamak için bir küme oluşturuyoruz
    queue = [(start_url, 0)]
    all_links = set()
    link_count = 0

    while queue:
        #Scripted By Ugur Turker Kebeci
        current_url, current_depth = queue.pop(0)
        if current_url not in visited and current_depth <= depth:
            print(f"{Fore.CYAN}|{'-' * 45}|")
            print(f"{Fore.CYAN}|{Fore.YELLOW}URL: {current_url}")
            visited.add(current_url)  # Ziyaret edildiğini belirtmek için kümeye ekliyoruz
            links, images = get_links_and_images(current_url, include_images)
            for link in links:
                if link not in visited:  # Daha önce ziyaret edilmediyse sadece ekliyoruz
                    queue.append((link, current_depth + 1))
                    all_links.add(link)
                    link_count += 1
                    print(f"{Fore.CYAN}|{Fore.GREEN}Link: {link}")

                    # Kayıt kontrolü
                    if save_links_option == "E" and link_count % 50 == 0:
                        save_links_thread = Thread(target=save_links, args=(all_links, filename, keywords, images))
                        save_links_thread.start()

            response = requests.get(current_url)
            page_content = response.text.lower()
            if any(keyword.lower() in page_content or keyword.lower() in current_url.lower() or (BeautifulSoup(response.text, "html.parser").title and keyword.lower() in BeautifulSoup(response.text, "html.parser").title.string.lower()) for keyword in keywords):
                print(f"{Fore.CYAN}|{Fore.BLUE}[Özel Link] Özel kelime bulundu: {current_url}")

    if save_links_option == "E":
        save_links(all_links, filename, keywords, images)

    return all_links
    
def save_links(new_links, filename, keywords, images):
    try:
        filepath = os.path.join(os.getcwd(), filename)
        existing_links = set()
        if os.path.exists(filepath):
            with open(filepath, "r") as f:
                existing_links = set(f.read().splitlines())
                #Scripted By Ugur Turker Kebeci
        all_links = existing_links.union(new_links)

        with open(filepath, "w") as f:
            for link in all_links:
                #Scripted By Ugur Turker Kebeci
                if any(keyword in link for keyword in keywords):
                    f.write(f"[Ozel Kelime] {link}\n")
                elif link in images:
                    f.write(f"[Resim] {link}\n")
                else:
                    f.write(link + "\n")
        
        print(f"{Fore.GREEN}Bağlantılar başarıyla kaydedildi: {filename}")
    except Exception as ex:
        print(f"{Fore.RED}Bağlantıları kaydederken bir hata oluştu: {ex}")

while True:
    try:
        system("cls" if os.name == "nt" else "clear")
       
        print("""


'                                 $$\               $$$$$$\                                                   
'                                 $$ |            $$$ ___$$$\                                                 
'   $$$$$$\   $$$$$$\   $$$$$$\ $$$$$$\          $$ _/   \_$$\        $$\   $$\  $$$$$$\  $$\   $$\  $$$$$$\  
'  $$  __$$\ $$  __$$\ $$  __$$\\_$$  _|        $$ / $$$$$\ $$\       $$ |  $$ |$$  __$$\ $$ |  $$ |$$  __$$\ 
'  $$ |  \__|$$ /  $$ |$$ /  $$ | $$ |          $$ |$$  $$ |$$ |      $$ |  $$ |$$ /  $$ |$$ |  $$ |$$ |  \__|
'  $$ |      $$ |  $$ |$$ |  $$ | $$ |$$\       $$ |$$ /$$ |$$ |      $$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |      
'  $$ |      \$$$$$$  |\$$$$$$  | \$$$$  |      $$ |\$$$$$$$$  |      \$$$$$$  |\$$$$$$$ |\$$$$$$  |$$ |      
'  \__|       \______/  \______/   \____/       \$$\ \________/        \______/  \____$$ | \______/ \__|      
'                                                \$$$\   $$$\                   $$\   $$ |                    
'                                                 \_$$$$$$  _|                  \$$$$$$  |                    
'                                                   \______/                     \______/                     

""")
        print("********** Web Dizin Tarama Programı (By Uğur Türker Kebeci)**********\n")
        baslangic_url = input("Başlangıç URL'sini girin: ")
        #Scripted By Ugur Turker Kebeci
        derinlik = int(input("Tarama derinliğini girin: "))
        include_images = input("Görsel bağlantılarını da taramak istiyor musunuz? (E/H): ").upper() == "E"
        keywords_input = input("Aramak istediğiniz özel kelimeleri virgülle ayırarak girin (boş bırakabilirsiniz): ")
        keywords = [keyword.strip() for keyword in keywords_input.split(",") if keyword.strip()]
        save_links_option = input("Tüm bağlantıları kaydetmek istiyor musunuz? (E/H): ").upper()

        filename = "data.txt"
        #Scripted By Ugur Turker Kebeci
        all_links = crawl(baslangic_url, derinlik, include_images, keywords, save_links_option, filename)

    except ValueError:
        print("Geçersiz derinlik seviyesi. Lütfen bir sayı girin.")
    except Exception as ex:
        print(f"{Fore.RED}Bir hata oluştu: {ex}")

    input("\nDevam etmek için ENTER tuşuna basın...")
