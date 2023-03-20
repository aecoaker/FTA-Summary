#read in data
import requests
from bs4 import BeautifulSoup
#pull free trade agreement links into a list
url = "https://www.gov.uk/government/collections/free-trade-agreement-between-the-united-kingdom-of-great-britain-and-northern-ireland-and-australia"
page = requests.get(url)
results = BeautifulSoup(page.content, "html.parser").find_all(class_ = "gem-c-document-list__item-title")

#filter to only look at chapters
chapters = [r for r in results if 'Chapter' in r.string]
print(results)