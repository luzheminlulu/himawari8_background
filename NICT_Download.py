#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  

from PIL import Image
import requests
import re
import datetime
import os

def clear_dir(path):
	print("正在删除%s下的文件"%(path))
	dir_list = os.listdir(path)
	for my_file in dir_list:
		try:
			os.remove(path+my_file)
		except:
			print("删除%s错误!"%(my_file))

			
def download_img(url, img_save_path):
	img = requests.get(url)
	with open(img_save_path, "wb") as fwi:
		fwi.write(img.content)
		print(img_save_path + "图片下载成功")


def fill_img(img_0,img_1,img_2,img_3, img_save_path):
	width, height = 1920, 1080      # 电脑屏幕大小
	#new_img = Image.new(img_1.mode, (width, height), color='black')
	new_img = Image.open("D:/himawari8_background-master/images/background.png")
	new_img = new_img.convert("RGBA")
	img_0=img_0.crop((0,10,550,550))
	img_1=img_1.crop((0,0 ,550,540))
	img_2=img_2.crop((0,10,550,550))
	img_3=img_3.crop((0,0 ,550,540))
	r,g,b,a = img_0.split()
	new_img.paste(img_0, (410,  0),mask = a)
	r,g,b,a = img_1.split()
	new_img.paste(img_1, (410,540),mask = a)
	r,g,b,a = img_2.split()
	new_img.paste(img_2, (960,  0),mask = a)
	r,g,b,a = img_3.split()
	new_img.paste(img_3, (960,540),mask = a)
	new_img.save(img_save_path)
	print(img_save_path + "图片合成成功")


def dl_main():
	clear_dir("D:/himawari8_background-master/Download_Picture/")
	clear_dir("D:/himawari8_background-master/Wallpaper/")
	print("开始下载图片")
	# 获取当前系统时间
	utc_today = datetime.datetime.utcnow() - datetime.timedelta(minutes=20)  # 获取GMT时间并减去20分钟
	delat_utc_today = utc_today.strftime("%Y/%m/%d/%H%M")  # 时间格式化
	# 分钟向下取整
	delat_utc_today_list = list(delat_utc_today)
	delat_utc_today_list[-1] = "0"
	delat_utc_today = "".join(delat_utc_today_list)
	
	# 整合为链接 格式为：http://himawari8-dl.nict.go.jp/himawari8/img/D531106/1d/550/2018/09/25/065000_0_0.png
	
	i=0
	for row in range(2):
		for col in range(2):
			img_url = "http://himawari8-dl.nict.go.jp/himawari8/img/D531106/2d/550/%s00_%d_%d.png"%(delat_utc_today,row,col)
			name = delat_utc_today.replace("/", "_") + "00_%d_%d.png"%(row,col)  # 获取图片名字
			# 图片保存路径
			img_save_path = "D:/himawari8_background-master/Download_Picture/" + name
			# 下载图片
			download_img(img_url, img_save_path)
			# 合成图片
						
			img = Image.open(img_save_path)
			#print(img.mode)
			img = img.convert("RGBA")
			datas = img.getdata()
			newData = list()
			for item in datas:
				if item[0]<3 and item[1]<3  and item[2]<3 :
					newData.append(( 0, 0, 0, 0))
				else:
					newData.append(item)
			img.putdata(newData)

			#print(img.mode)
			if i==0:
				img_0 = img
			elif i==1:
				img_1 = img
			elif i==2:
				img_2 = img
			elif i==3:
				img_3 = img
			
			i=i+1
	

	new_img_save_path = "D:/himawari8_background-master/Wallpaper/" + delat_utc_today.replace("/", "_")+".png"
	#print(new_img_save_path)
	fill_img(img_0,img_1,img_2,img_3, new_img_save_path)
	return new_img_save_path


if __name__ == '__main__':
	dl_main()
