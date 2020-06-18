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


def fill_img(img_1,img_2,img_3,img_4, img_save_path):
	width, height = 1920, 1080      # 电脑屏幕大小
	new_img = Image.new(img_1.mode, (width, height), color='black')
	img_1=img_1.crop((0,10,550,550))
	img_2=img_2.crop((0,10,550,550))
	img_3=img_3.crop((0,0 ,550,540))
	img_4=img_4.crop((0,0 ,550,540))
	new_img.paste(img_1, (410, 0))
	new_img.paste(img_2, (960, 0))
	new_img.paste(img_3, (410, 540))
	new_img.paste(img_4, (960, 540))
	new_img.save(img_save_path)
	print(img_save_path + "图片合成成功")


def dl_main():
	clear_dir("D:/background/Download_Picture/")
	#clear_dir("D:/background/Wallpaper/")
	print("开始下载图片")
	# 获取当前系统时间
	utc_today = datetime.datetime.utcnow() - datetime.timedelta(minutes=20)  # 获取GMT时间并减去30分钟
	delat_utc_today = utc_today.strftime("%Y/%m/%d/%H%M")  # 时间格式化
	# 分钟向下取整
	delat_utc_today_list = list(delat_utc_today)
	delat_utc_today_list[-1] = "0"
	delat_utc_today = "".join(delat_utc_today_list)
	
	# 整合为链接 格式为：http://himawari8-dl.nict.go.jp/himawari8/img/D531106/1d/550/2018/09/25/065000_0_0.png
	img_url = "http://himawari8-dl.nict.go.jp/himawari8/img/D531106/2d/550/" + delat_utc_today + "00_0_0.png"
	name = delat_utc_today.replace("/", "_") + "00_0_0.png"  # 获取图片名字
	# 图片保存路径
	img_save_path = "D:/background/Download_Picture/" + name
	# 下载图片
	download_img(img_url, img_save_path)
	# 合成图片
	img_1 = Image.open(img_save_path)
	
	img_url = "http://himawari8-dl.nict.go.jp/himawari8/img/D531106/2d/550/" + delat_utc_today + "00_1_0.png"
	name = delat_utc_today.replace("/", "_") + "00_1_0.png"  # 获取图片名字
	# 图片保存路径
	img_save_path = "D:/background/Download_Picture/" + name
	# 下载图片
	download_img(img_url, img_save_path)
	# 合成图片
	img_2 = Image.open(img_save_path)
	
	img_url = "http://himawari8-dl.nict.go.jp/himawari8/img/D531106/2d/550/" + delat_utc_today + "00_0_1.png"
	name = delat_utc_today.replace("/", "_") + "00_0_1.png"  # 获取图片名字
	# 图片保存路径
	img_save_path = "D:/background/Download_Picture/" + name
	# 下载图片
	download_img(img_url, img_save_path)
	# 合成图片
	img_3 = Image.open(img_save_path)
	
	img_url = "http://himawari8-dl.nict.go.jp/himawari8/img/D531106/2d/550/" + delat_utc_today + "00_1_1.png"
	name = delat_utc_today.replace("/", "_") + "00_1_1.png"  # 获取图片名字
	# 图片保存路径
	img_save_path = "D:/background/Download_Picture/" + name
	# 下载图片
	download_img(img_url, img_save_path)
	# 合成图片
	img_4 = Image.open(img_save_path)
	
	new_img_save_path = "D:/background/Wallpaper/" + delat_utc_today.replace("/", "_")+".png"
	print(new_img_save_path)
	fill_img(img_1,img_2,img_3,img_4, new_img_save_path)
	return new_img_save_path


if __name__ == '__main__':
	dl_main()
