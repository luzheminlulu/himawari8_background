向日葵8号卫星实时更新windows壁纸

脚本运行路径会自动识别，无需手动修改

现已支持背景图修改，背景图片为\images\background.png,可以根据需要自行替换

已添加天气功能，可以在set_picure.py中修改城市
```
name = ["滁州"     ,     "杭州" , "" ,     "上海",   ] #城市名(建议少于等于6个)
city = ["chuzhou"  , "hangzhou" , "" , "shanghai",   ] #城市拼音
Lng  = [       118 ,        120 , 0  ,        121,   ] #经度  (建议60~140~180)
Lat  = [        32 ,         30 , 0  ,         31,   ] #纬度  (建议-80~80)
```

windows任务计划程序设置如下：

创建任务:

![image](https://github.com/luzheminlulu/himawari8_background/blob/master/images/1.png)

新建触发器，卫星每10分钟更新一次数据，所以刷新频率不必设的太高:

![image](https://github.com/luzheminlulu/himawari8_background/blob/master/images/2.png)

新建操作，参数根据你的路径修改：

![image](https://github.com/luzheminlulu/himawari8_background/blob/master/images/3.png)

进行一些行为设置，不设置也可以，灵活参考：

![image](https://github.com/luzheminlulu/himawari8_background/blob/master/images/4.png)

效果图：

![image](https://github.com/luzheminlulu/himawari8_background/blob/master/images/5.png)

参考资料:

https://blog.csdn.net/Q_QuanTing/article/details/82854444
