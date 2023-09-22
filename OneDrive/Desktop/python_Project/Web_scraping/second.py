import requests
from bs4 import BeautifulSoup


def Get_Page(url):
    try:
        response = requests.get(url)
    except:
        return None
    print(response.status_code) 
    return response    

def find_link(html_doc):
    soup = BeautifulSoup(html_doc)
    soup = soup.find("div", attrs={'class' :'grid grid-cols-12 sm:gap-6 xl:absolute top-2/4 xl:transform -translate-y-2/4 right-0'})
    return soup.find_all('a')    


if __name__ == "__main__":
    link = "https://roocket.ir"
    response = Get_Page(link)  
    links = find_link(response.text)    
    for i in links:
        ii = i.get('href')
        if "http" != ii[0:4:]:
            print(f"https://roocket.ir{i.get('href')}")

        else:    
            print(f"{i.get('href')}")
