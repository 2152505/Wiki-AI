## Linux用户管理<br>
### Linux用户简介：<br>
Linux系统是一个多用户多任务的操作系统，任何一个要使用系统资源的用户，都必须首先向系统管理员申请一个账号，然后以这个账号的身份进入系统。root用户是系统默认创建的管理员账号。<br>
#### 添加用户wang5，创建其用户目录。记得sudo<br>
useradd -d /home/wang5  -m  wang5：创建一个账号叫wang5，并且给wang5指定主目录。<br>
passwd wang5：给wang5设置密码。<br>
chown wang5 -R /home/wang5 ；-R : 改为用户所属权限包括文件夹以下的目录<br>
#### id添加到root组<br>
usermod -g root wang5<br>
如果要wang5拥有sudo权限，还需要编辑 /etc/sudoers 文件。sudoers 文件的默认权限是 440，即默认无法修改；通过 visudo 可以在不更改 sudoers 文件权限的情况下，直接修改 sudoers 文件；默认编辑 /etc/sudoers 文件。在最root下加入一行，添加后的内容为：<br>
root    ALL=(ALL:ALL) ALL<br>
wang5 ALL=(ALL) ALL<br>
这条指令的解释为:<br>
wang5是要配置的用户名<br>
ALL=(ALL:ALL)：表示授予 wang5用户在任何主机上、使用任何用户身份（即以任何用户身份）执行任何命令的权限。<br>
ALL->表示允许在任何主机上执行命令。<br>
=(ALL:ALL) ->表示以任何用户身份（即以任何用户身份）执行命令。<br>
ALL->表示允许执行任何命令。<br>
我们画一个图来解释一下:<br>

Sudoers的权限必须是220否则会提示无法使用。<br>
万一sudoers权限或者内容坏了，用 pkexec visudo 修复，文件打开后直接保存即可修复。<br>

#### 删除用户：<br>
userdel wang5：删除用户wang5，保留wang5的主目录。<br>
userdel -r wang5：删除用户wang5，并且把wang5的主目录也删除。<br>
#### 查询用户信息：<br>
id 用户名<br>
id wang5：查看用户wang5的信息。<br>
切换用户：<br>
su 用户名<br>
su wang5：切换到wang5用户。<br>
注意：从高权限用户切换到低权限用户时，不需要输密码；否则，需要输密码。<br>
此外，还有命令：<br>
Logout退出登录<br>
exit命令可以回到原来的用户。
#### 实验：用wang5创建abc.txt，并用nano编辑；再用ls看nano的权限和所有者。试试能不能再pi用户下创建文件 touch abc.txt。因为pi目录其他用户没有写权限
切换到pi用户，然后企图nano前面的文件，看能存不？nano前面加上sudo呢？
用sudo创建一个文件，ls -l 看看创建的人是谁？
Ubuntu下设置/修改root密码
安装好ubuntu系统后，root密码是动态的。可以用这个方法给ubuntu更改root密码：sudo passwd root。比如：
osboxes@osboxes:/etc$ sudo passwd root<br>
[sudo] password for osboxes: <br>
New password: <br>
Retype new password: <br>
passwd: password updated successfully<br>
关键就是sudo passwd root，输入两次新密码后root就有固定密码了。<br>
## Linux组管理<br>
### Linux的组简介：<br>
Linux的组类似于角色，系统可以对有共性的多个用户进行统一的管理。每一个用户都至少属于一个组，创建用户时如果不指定组，会默认创建一个跟用户名相同的组，并且把新创建的用户分配到组中，root用户默认属于root组。<br>
cat /etc/group 查看所有分组，简单的用groups直接看<br>
#### 添加组：<br>
groupadd 组名<br>
groupadd devgroup：创建一个组devgroup。<br>
#### 删除组：<br>
groupdel 组名<br>
groupdel devgroup：删除组devgroup。<br>
#### 添加用户时指定组：<br>
useradd –g 组名 用户名<br>
useradd –g devgroup zhangsan：添加用户zhangsan，并且指定zhangsan属于组devgroup。<br>
#### 将用户添加到组／从组中移除：<br>
gpasswd –a／－d 用户名 组名<br>
gpasswd –a zhangsan test<br>
gpasswd –d zhangsan test<br>
