#@title <b><center>Enter Rocklink/gtlink/shortingly Link Below</center></b>
print("Downloading Cloud-Scraper...")
!pip install cloudscraper
print("Setting Up!")
print("Performing Check...")
import time
import cloudscraper
from bs4 import BeautifulSoup 
print("Everything Looks Good! Lets Continue.")

url = "https://shortingly.me/qaXpNHm"  #@param {type:"string"}


'''
NOTE: 
SUPPORTED DOMAINS:
 - rocklinks.net
 - gtlinks.me
 - shortingly.me
 
 
'''
# ---------------------------------------------------------------------------------------------------------------------

def bypass(url):
    client = cloudscraper.create_scraper(allow_brotli=False)
    if 'rocklinks.net' in url:
        DOMAIN = "https://blog.disheye.com"
    elif 'gtlinks.me' in url:
        DOMAIN = "https://go.kinemaster.cc"
    elif 'shortingly.me' in url:
        DOMAIN = "https://go.gyanitheme.com"
    else:
        DOMAIN = "https://rocklinks.net"

    url = url[:-1] if url[-1] == '/' else url

    code = url.split("/")[-1]
    if 'rocklinks.net' in url:
        final_url = f"{DOMAIN}/{code}?quelle=" 
    else:
        final_url = f"{DOMAIN}/{code}"

    resp = client.get(final_url)
    soup = BeautifulSoup(resp.content, "html.parser")
    
    try: inputs = soup.find(id="go-link").find_all(name="input")
    except: return "Incorrect Link"
    
    data = { input.get('name'): input.get('value') for input in inputs }

    h = { "x-requested-with": "XMLHttpRequest" }
    
    time.sleep(10)
    r = client.post(f"{DOMAIN}/links/go", data=data, headers=h)
    try:
        return r.json()['url']
    except: return "Something went wrong :("

# ---------------------------------------------------------------------------------------------------------------------

print(bypass(url))
