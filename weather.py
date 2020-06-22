import requests
import codecs
import os
from bs4 import BeautifulSoup
import random

import math

from PIL import Image,ImageDraw,ImageFont

def get_weather(city):
	user_agent = [
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
		]
	headers = {'User-Agent': random.choice(user_agent)}
	urls = []
	a="https://tianqi.911cha.com/"
	url=a+city
	#print(url)
	urls.append(url)
	label=["1","2","天气","温度","湿度","风力","风级","降水量","体感温度","云量"]
	
	for url in urls:
		response = requests.get(url,headers=headers)
		#print(response)
		soup = BeautifulSoup(response.text, 'html.parser')
		weather_list = soup.select('div[class="mcon noi"] table')
		#for weather in weather_list:
		weather = weather_list[0]
		weather_date = weather.select('tr')[0].getText()
		tr_list = weather.select('tr')
		i=0
		#for tr in tr_list:
		tr=tr_list[3]
		#print(tr)
		td_list= tr.select('td')
		th_list=tr.select('th')
		str=""

		for i in range(2,10):
			str += label[i]+":"
			str += td_list[i].getText()+"\n"
	
	return str
		
def draw_weather(city_list,city_name,Lng_list,Lat_list,img_save_path):
	i=0
	for city in city_list:
		print("开始获取%s天气..."%(city_name[i]))
		weather = get_weather(city)
		
		factor_x = 1.0+(math.cos(math.radians(abs(Lng_list[i]-140))))/(6.617-math.cos(math.radians(abs(Lng_list[i]-140))))
		factor_y = 1.0+(math.cos(math.radians(abs(Lat_list[i]))))/(6.617-math.cos(math.radians(abs(Lat_list[i]))))
		print("投影校正系数:%f,%f"%(factor_x,factor_y))
		actual_lng = int(960.0+factor_x*550.0*math.cos(math.radians(Lat_list[i]))*math.sin(math.radians(Lng_list[i]-140.0)))
		actual_lat = int(540.0-factor_y*(550.0*math.sin(math.radians(Lat_list[i]))))
		print("开始叠加%s天气:%d,%d"%(city_name[i],actual_lng,actual_lat))
 		
		im = Image.open(img_save_path) 
		draw = ImageDraw.Draw(im)      
		ft_1 = ImageFont.truetype("C:\Windows\Fonts\STXIHEI.TTF", 30)
		ft_2 = ImageFont.truetype("C:\Windows\Fonts\STXIHEI.TTF", 25)
		
		offset_y= 335*(i%3)
		offset_x=1270*(i//3)

		if(offset_x==0):
			offset_xx=0
		else:
			offset_xx=offset_x-250
		
		draw.text((200+offset_x , 45+offset_y),city_name[i], font = ft_1, fill = (255, 255 ,255)) 
		draw.text((210+offset_x ,95+offset_y),weather, font = ft_2, fill = (255, 255 ,255)) 
		draw.line((200+offset_x , 90+offset_y ,450+offset_x, 90+offset_y), '#FFFFFF')
		draw.line((450+offset_xx, 90+offset_y ,actual_lng  , actual_lat ), '#FFFFFF')
		draw.ellipse((actual_lng-5,actual_lat-5, actual_lng+5, actual_lat+5), fill=(255, 255, 255), outline='#FFFFFF', width=1)
		#im.show()
		im.save(img_save_path)
		i+=1
	
	
	
if __name__ == '__main__':
	draw_weather("shanghai",".",".")
