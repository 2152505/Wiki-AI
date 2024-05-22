#### 相关问题以及解决方案

[Linux SSH登录服务器报ECDS for has changed and you have requested strict checking错误](./Linux/Linux%20SSH登录服务器报ECDSA%20host%20key%20_ip地址_%20for%20has%20changed%20and%20you%20have%20requested%20strict%20checking错误.html)
<br/>
<br/>
<br/>

**<big>1. 解决qt.qpa.xcb: could not connect to display问题</big>**
以服务器作为远程解释器，本地pycharm或vscode调试时出现如下错误：

```
qt.qpa.xcb: could not connect to display
qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "/home/xx/anaconda3/lib/python3.8/site-packages/cv2/qt/plugins" even though it was found.
This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.
 
Available platform plugins are: xcb, eglfs, minimal, minimalegl, offscreen, vnc
```

这和IDE不能直接回传图形界面相关，比如一份代码中添加cv.imshow()后报上述错误

#### 解决办法

可借助第三方ssh软件<br/>
以windows和pycharm为例，

#### 第一步：安装远程ssh软件MobaXterm（或其他支持图形回传的远程软件）<br/>

附上安装包链接：<https://pan.baidu.com/s/1ICNpYK-95tCoMjZMJRcZlg>

提取码：ohgp<br/>
输入下面命令

```
echo $DISPLAY
```

得到服务器的显示端口：

NOET<br/>
如果echo DISPLAY返回空，可以在mobaxterm启用终端处找到非本地DISPLAY端口

在vi /etc/profile内添加export DISPLAY=10.110.3.26:0.0

执行source /etc/profile

#### 第二步：然后ssh终端安装xorg并使用xclock测试能否回传图像

```
apt-get install xorg
xclock
```

执行后桌面会跳出一个时钟的图案

#### 第三步：点击PyCharm菜单栏pycharm-Run-Edit Configurations, 在Environment variable添加DISPLAY=localhost:10.0 或 DISPLAY=10.110.3.26:0.0

保证ssh软件和pycharm同时开启，重新运行程序，即可显示远端图像。

**<big>2.  解决Libqtgui4 is not available (Has no installation candidate)</big>**

I am trying to run this command:

```
sudo apt-get install libqtgui4 libqtwebkit4 libqt4-test python3-pyqt5
```

But I receive these errors:

Package libqtgui4 is not available, but is referred to by another package.

E: Package 'libqtgui4' has no installation candidate
E: Unable to locate package libqtwebit4
E: Unable to locate package libqt4-test

I was trying to follow this solution: <https://stackoverflow.com/questions/59080094/raspberry-pi-and-opencv-cant-install-libhdf5-100>

Try this command:

```
sudo apt-get install libqt5gui5 libqt5webkit5 libqt5test5
```

Instead of

```
sudo apt-get install libqtgui4 libqtwebkit4 libqt4-test
```

If you are trying to install opencv on a Raspberry Pi 3B

**<big>3.  树莓派上创建虚拟环境</big>**

在树莓派上创建虚拟环境是一种良好的实践，可以帮助您在不同项目之间隔离Python包的依赖关系。以下是在树莓派上使用virtualenv创建虚拟环境的一般步骤：

安装virtualenv：

在终端中运行以下命令安装virtualenv：

```
sudo apt-get update sudo apt-get install python3-venv 
```

如果您的树莓派上使用的是Python 2，请使用python-virtualenv而不是python3-venv。

创建虚拟环境：

在您的项目文件夹中，运行以下命令创建一个名为venv的虚拟环境：

```
python3 -m venv venv 
```

或者使用Python 2：

```
virtualenv venv 
```

激活虚拟环境：

激活虚拟环境以开始使用它。运行以下命令：

```
source venv/bin/activate 
```

或者如果您使用的是Python 2：

```
source venv/bin/activate
```

一旦虚拟环境被激活，您将看到终端提示符的前面有(venv)，表示您现在在虚拟环境中。

安装依赖：

在虚拟环境中，您可以使用pip安装项目所需的所有依赖：

```
pip install package_name
```

请替换package_name为您实际需要安装的包的名称。

退出虚拟环境：

在完成项目工作后，可以通过运行以下命令退出虚拟环境：

```
source deactivate
```

终端提示符将返回到正常状态。

使用虚拟环境可以有效地管理项目的依赖项，确保它们不会与系统级的Python包冲突
