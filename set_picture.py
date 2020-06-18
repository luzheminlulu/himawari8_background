#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
#

import win32api, win32con, win32gui
import NICT_Download


def set_desktop_windows(imagepath):
    k = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(k, "WallpaperStyle", 0, win32con.REG_SZ, "2")  # 2拉伸适应桌面，0桌面居中
    win32api.RegSetValueEx(k, "TileWallpaper", 0, win32con.REG_SZ, "0")
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, imagepath, 1 + 2)


if __name__ == '__main__':
    try:
        new_img_save_path = NICT_Download.dl_main()
    except Exception as e:
        print(e)
    # 这里的路径必须为绝对路径
    wallpaper_path = new_img_save_path
    set_desktop_windows(wallpaper_path)
