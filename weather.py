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
	
	weather_url="https://tianqi.911cha.com/"
	url=weather_url+city+"/"
	#print(url)
	label=["1","2","天气","温度","湿度","风力","风级","降水量","体感温度","云量"]
		
	response = requests.get(url,headers=headers)
	#print(response)
	soup = BeautifulSoup(response.text, 'html.parser')
	weather_list = soup.select('div[class="mcon noi"] table')
	weather = weather_list[0]
	weather_date = weather.select('tr')[0].getText()
	tr_list = weather.select('tr')
	#print(tr_list)
	tr=tr_list[3]
	td_list= tr.select('td')
	str=""

	for i in range(2,10):
		str += label[i]+":"
		str += td_list[i].getText()+"\n"
	
	print(str[:-1])
	return str
	
	
def draw_weather(city_list,city_name,Lng_list,Lat_list,img_save_path):
	i=0
	for city in city_list:
		try:
			print("\n开始获取%s天气..."%(city_name[i]))
			weather = get_weather(city)
			
			factor_x = 1.0+(math.cos(math.radians(abs(Lng_list[i]-140))))/(6.617014597-math.cos(math.radians(abs(Lng_list[i]-140.0))))
			factor_y = 1.0+(math.cos(math.radians(abs(Lat_list[i]))))/(6.617014597-math.cos(math.radians(abs(Lat_list[i]))))
			print("投影校正系数:%f,%f"%(factor_x,factor_y))
			actual_lng = int(960.0+factor_x*540.0*math.cos(math.radians(Lat_list[i]))*math.sin(math.radians(Lng_list[i]-140.0)))
			actual_lat = int(540.0-factor_y*(540.0*math.sin(math.radians(Lat_list[i]))))
			print("开始叠加%s天气:%d,%d"%(city_name[i],actual_lng,actual_lat))
			
			im = Image.open(img_save_path) 
			draw = ImageDraw.Draw(im)      
			ft_1 = ImageFont.truetype("C:\Windows\Fonts\STXIHEI.TTF", 30)
			ft_2 = ImageFont.truetype("C:\Windows\Fonts\STXIHEI.TTF", 25)
			
			offset_y= 335*(i%3)
			offset_x=1340*(i//3)
	
			if(offset_x==0):
				offset_xx=0
			else:
				offset_xx=offset_x-250
			
			draw.text((200+offset_x , 45+offset_y),city_name[i], font = ft_1, fill = (255, 255 ,255)) 
			draw.text((210+offset_x , 95+offset_y),weather     , font = ft_2, fill = (255, 255 ,255)) 
			draw.line((200+offset_x , 90+offset_y ,450+offset_x, 90+offset_y), '#FFFFFF')
			draw.line((450+offset_xx, 90+offset_y ,actual_lng  , actual_lat ), '#FFFFFF')
			draw.ellipse((actual_lng-5,actual_lat-5, actual_lng+5, actual_lat+5), fill=(255, 255, 255), outline='#FFFFFF', width=1)
			#im.show()
			im.save(img_save_path)
		except Exception as e:
			print(e)
		i+=1
	
	
	
if __name__ == '__main__':
	get_weather("shanghai")
