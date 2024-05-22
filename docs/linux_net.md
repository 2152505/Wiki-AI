### Linux网络命令
默认的命令提示符如下：   
pi@raspberrypi:~ $   
表明你是在名为“raspberrypi”的主机上以用户“pi”的身份登录，并且正处在“pi”用户的主目录下面。你可以在后面输入各种Linux命令，然后按回车键即可执行。  

### 网络部分命令  
1、回到根目录cd /  
2、ifconfig 等价于windows ipconfig  
3、查看无线连接iwconfig   
4、设置IP地址 ifconfig wlan0 192.168.1.131    
5、route add default gw 192.168.1.1 dev wlan0   
6、修改wifi连接，最简单的使用拔卡修改文件方式。其次还可以这么修改。要用到sudo，touch、nano、cat命令   
-1、新建文件 /etc/mywifi.conf   
内容如下：  
ctrl_interface=/var/run/wpa_supplicant  
network={  
	ssid="abc"  
	psk="0987654321"  
}  
-2、连接wlan0到网络，并以daemon方式运行  
wpa_supplicant -B -i wlan0 -c /etc/mywifi.conf  
说明：  
-B Background 在后台以daemon 运行  
-i interface  
-c 配置文件  

7、网卡启动和关闭  ifconfig wlan0 up/down  