from flask import *
import os, json,requests,datetime
from News_scraper import Scraper_news

app = Flask(__name__)
Master_data = Scraper_news()

if os.path.exists("newsData.json"):
	with open("newsData.json") as file:
		read_data = file.read()
		top_news = json.loads(read_data)
else:
	with open("newsData.json","w") as file:
		read_data = json.dumps(Master_data, indent=4, sort_keys=True)
		file.write(read_data)
		file.close()
	with open("newsData.json") as content:
		read_data1 = content.read()
		top_news = json.loads(read_data1)

@app.route("/catboot/top_news/all_data",methods = ["GET"])
def get_all_data():
	return jsonify(top_news)

@app.route("/catboot/top_news/<catagry>",methods = ["GET"])
def get_catagreas(catagry):
	return jsonify(top_news[catagry])

if __name__ == "__main__" :
	app.run(debug = True)
