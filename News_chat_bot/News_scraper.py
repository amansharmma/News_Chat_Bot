from bs4 import BeautifulSoup
import requests,datetime

top_news = {"world":[],"business":[],"technology":[],"sports":[],"entertainment":[]}
def Scraper_news():
	new_dic = {}
	URLS_of_menu = {"world":"http://www.newzcone.com/world/","business":"http://www.newzcone.com/business/","technology":"http://www.newzcone.com/technology/networking-telecom/","sports":"http://www.newzcone.com/sports/","entertainment":"http://www.newzcone.com/entertainment/"}
	Today = datetime.date.today()
	today = ""
	for string in str(Today):
		if string == "-":
			today +="/"
		else:
			today+=string
	for key in URLS_of_menu:
		url = URLS_of_menu[key]
		html = requests.get(url)
		soup = BeautifulSoup(html.text,"html.parser")
		findingUrl = soup.findAll("div",class_="news-entry")
		for div in findingUrl:
			a_tags = div.findAll("a")
		count = 0
		for a in a_tags[1:15]:
			new_dic["Date"] = today
			new_dic["Discription"] = a.get_text().strip()
			new_dic["News_URL"] = a["href"]
			html = requests.get(a["href"])
			needsoup = BeautifulSoup(html.text,"html.parser")
			get_title = needsoup.title.get_text().strip()
			new_dic["Title"] = get_title
			count +=1	
			if count == 5:
				break
			top_news[key].append(new_dic.copy())
	return(top_news)

