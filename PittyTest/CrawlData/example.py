import requests
import webbrowser
from bs4 import BeautifulSoup
from map import map_check_to_issue
map_name_to_check: dict[str, str]   
url = 'https://github.com/crytic/slither/wiki/Detector-Documentation'
to_crawl = [url]
visited = set()
count: int = 0
mapping_dict = {}
while to_crawl: 
    current_url = to_crawl.pop(0)
    visited.add(current_url)
    try:
        response = requests.get(current_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            h2_headings = soup.find_all('h2')
            if len(h2_headings) >= 2:
                h2_headings = h2_headings[1:-1]

            count = count + 1    
            for h2_heading in h2_headings:
                check_key = h2_heading.find_next(string = "Check: ")
                check_value = check_key.find_next().get_text()
                
                h2_heading = h2_heading.getText().replace(' ', '-').lower()
                mapping_dict[h2_heading] = check_value
        else:
            print("Failed to retrieve:", current_url)
    except Exception as e:
        print(e)
# print('map_check_to_issue: dict[str, str] = {') 
# for key, value in mapping_dict.items():
#     print (f"   '{value}': '{key}',")
# print('}')

webbrowser.open(url + "#" + map_check_to_issue["solc-version"])