import requests
import codecs
import os
from bs4 import BeautifulSoup
import random

from PIL import Image,ImageDraw,ImageFont
import urllib.request
import urllib.parse


def get_weather(city):
	user_agent = [
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
		]
	headers = {'User-Agent': random.choice(user_agent)}

	label=["1","2","天气","温度","湿度","风力","风级","降水量","体感温度","云量"]
	
	
	# 拼接url
	url = "http://www.baidu.com/s?wd=" + urllib.parse.quote("上海"+'天气')
	print(url)
	# 请求读取
	page_source = requests.get(url,headers=headers)
	print(page_source)
	soup = BeautifulSoup(page_source.text, 'html.parser')
	weather_list = soup.select('div[class="mcon noi"] table')
	print(weather_list)
	
	return str
		
	
	
if __name__ == '__main__':
	get_weather("shanghai")
