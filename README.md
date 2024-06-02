# python-被动式敏感信息扫描
效果图如下：
![image](https://github.com/M7-wacb/python--infoscan/assets/123800032/e2eefb0c-294a-47ba-862a-6399300cce3d)

使用python编写的被动敏感信息扫描脚本，使用mitmdump，安装教程和可能遇到的问题:
> https://www.cnblogs.com/yoyo1216/p/16165758.html

> https://blog.csdn.net/weixin_45438997/article/details/124261720

pip安装:  `pip install -r requirements.txt`

使用命令：

`mitmdump -s infoscan.py -p 8090 --ssl-insecure -q`

