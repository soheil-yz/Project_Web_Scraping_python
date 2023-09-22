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
    return soup.find_all('a')    


if __name__ == "__main__":
    link = "https://roocket.ir"
    response = Get_Page(link)  
    links = find_link(response.text)    
    for i in links:
        print(f"{i.get('href')}")