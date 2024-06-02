# python-被动式敏感信息扫描
效果图如下：
![image](https://github.com/M7-wacb/python--infoscan/assets/123800032/e2eefb0c-294a-47ba-862a-6399300cce3d)

使用python编写的被动敏感信息扫描脚本，使用mitmdump，安装教程和可能遇到的问题:
> https://www.cnblogs.com/yoyo1216/p/16165758.html

> https://blog.csdn.net/weixin_45438997/article/details/124261720

pip安装:  `pip install -r requirements.txt`

使用命令：

`mitmdump -s infoscan.py -p 8090 --ssl-insecure -q`

建议联动burpsuite，具体操作：
![image](https://github.com/M7-wacb/python--infoscan/assets/123800032/914019a2-299c-449a-b71a-eab9d1c52330)
设置burpsuite上层代理，ip写127.0.0.1，端口就是命令mitmdump -p 监听的端口：
![image](https://github.com/M7-wacb/python--infoscan/assets/123800032/37f8cea8-7e0a-4423-b504-cb831e76bc97)

### 注意事项
使用时cmd界面可能卡住，在属性中关闭快速编辑模式即可。
