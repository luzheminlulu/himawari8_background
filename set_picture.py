#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
#

import win32api, win32con, win32gui
import NICT_Download
import weather

name = ["上海","杭州","滁州"] #城市名
city = ["shanghai","hangzhou","chuzhou"] #城市拼音
Lng  = [121,120,118]        #经度(50~140~180)
Lat  = [ 31,30,32]         #纬度(-90~90)
wallpaper_path = "D:\himawari8_background-master\Wallpaper\Wallpaper.png"


def set_desktop_windows(imagepath):
	k = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
	win32api.RegSetValueEx(k, "WallpaperStyle", 0, win32con.REG_SZ, "2")  # 2拉伸适应桌面，0桌面居中
	win32api.RegSetValueEx(k, "TileWallpaper", 0, win32con.REG_SZ, "0")
	win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, imagepath, 1 + 2)


if __name__ == '__main__':
	try:
		img_save_path = NICT_Download.dl_main()
		weather.draw_weather(city,name,Lng,Lat,img_save_path)
		set_desktop_windows(img_save_path)
	except Exception as e:
		print(e)
