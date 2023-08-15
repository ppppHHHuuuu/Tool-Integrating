import requests
import webbrowser
from bs4 import BeautifulSoup
from map import map_check_to_issue


class CrawlData: #url, param
    mapping_dict = {}
    
    def __init__(self, url = "https://github.com/crytic/slither/wiki/Detector-Documentation") -> None:
        self.url = url
        
    def crawl_issue(self):
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                h2_headings = soup.find_all('h2')
                
                #Exclude header and footer of page
                if len(h2_headings) >= 2:
                    h2_headings = h2_headings[1:-1]
                    
                for h2_heading in h2_headings:
                    check_key = h2_heading.find_next(string = "Check: ")
                    check_value = check_key.find_next().get_text()
                    h2_heading = h2_heading.getText().replace(' ', '-').lower()
                    CrawlData.mapping_dict[h2_heading] = check_value
            else:
                print("Failed to retrieve:", self.url)
        except Exception as e:
            print(e)
            
    def print_mapping(self):
        print('map_check_to_issue: dict[str, str] = {') 
        for key, value in CrawlData.mapping_dict.items():
            print (f"   '{value}': '{key}',")
        print('}')
        

webbrowser.open(url + "#" + map_check_to_issue["solc-version"])