import requests
import codecs
import os
from bs4 import BeautifulSoup
import random

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
		#for th in th_list:
		#	str+=th.getText()+'\n'
		#print(td_list)
		#for td in td_list:
		#	str += label[i]+":"
		#	str += td.getText()+"\n"
		#	i+=1
		for i in range(2,10):
			str += label[i]+":"
			str += td_list[i].getText()+"\n"
	
		return str
		
def draw_weather(city,img_save_path,new_img_save_path):
	weather = get_weather(city)
	
	im = Image.open(img_save_path) # 打开文件
	#print(im.format, im.size, im.mode)
	draw = ImageDraw.Draw(im) #修改图片
	ft_1 = ImageFont.truetype("C:\Windows\Fonts\STXIHEI.TTF", 30)
	ft_2 = ImageFont.truetype("C:\Windows\Fonts\STXIHEI.TTF", 25)
	draw.text((250,50), "上海", font = ft_1, fill = (255, 255 ,255)) #利用ImageDraw的内置函数，在图片上写入文字
	draw.text((250,100), weather, font = ft_2, fill = (255, 255 ,255)) #利用ImageDraw的内置函数，在图片上写入文字
	draw.line((240, 95, 500, 95), '#FFFFFF')
	draw.line((500, 95, 760, 230), '#FFFFFF')
	draw.ellipse((755, 225, 765, 235), fill=(255, 255, 255), outline='#FFFFFF', width=1)
	#im.show()
	im.save(new_img_save_path)
	
	
	
if __name__ == '__main__':
	draw_weather()
