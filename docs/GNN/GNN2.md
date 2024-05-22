#### 1.用networkX可视化图

pyg可以和network相互转化
anaconda navigater is good

#### 2.如何知道Anaconda的安装位置

按【win+r】快捷键，在输入框中输入cmd，点击【确定】；
在命令行窗口执行 conda info --envs 命令即可。
如何指定Jupyter notebook使用某个环境的python?

如果您已经在特定的conda环境中安装了Jupyter Notebook，并且想要确保Jupyter Notebook使用该环境中的Python版本，可以按照以下步骤操作：

1. 打开终端或命令提示符窗口并激活要使用的conda环境。例如，如果要使用名为myenv的conda环境，请运行以下命令：

```python
conda activate myenv
```

2. 在该环境中安装`ipykernel`软件包。这个软件包将允许Jupyter Notebook使用特定环境的Python版本。运行以下命令：

!!!!!注意，此处更好的选择是使用anaconda navigator进行新环境的创建。

```python
conda install ipykernel
```

3. 将该环境添加到Jupyter Notebook中。运行以下命令：

```python
python -m ipykernel install --user --name=your_env_name --display-name="Python(env_name)"
```

上面的命令记得替换env_name

这将在Jupyter Notebook中创建一个新内核，其名称为`your_env_name`，显示名称为`Python(env_name)`。这个新的内核将使用你特定的conda环境中的Python版本。

4. 启动Jupyter Notebook。在终端或命令提示符窗口中运行以下命令：

```python
jupyter notebook
```

现在，当您在Jupyter Notebook中创建一个新的Notebook时，您可以从Kernel菜单中选择`Python (myenv)`内核，以确保Notebook使用特定环境的Python版本。

检查是否为指定环境的python:

运行以下命令来查看Python的位置：which python

运行以下命令来查看Python的版本：python --version

```python
[Jupyter]KernelRestarter: restarting kernel (1/5), keep random ports WARNING:root:kernel ...
```

#### 3.使用Jupyter调用OpenCV中imshow（）显示图像，提示内核正在重启，命令行报错KernelRestarter: restarting kernel (1/5), keep random ports WARNING:root:kernel

网上搜索添加一下代码可解决（失败）：

```python
import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
```

添加后，并没有解决。

解决方案：

在Anaconda文件夹中，自己使用的虚拟环境下搜索：libiomp5md.dll这个文件

将其删除，重启Jupyter即解决。
tmd, 自带的内核就是一坨狗屎，新建的内核yyds

系统：Windows11

不知道是什么原因，原本可以在jupyter notebook上运行的代码，在点击运行（或run）后代码块总是显示*号，并且内核一直显示挂掉了，就算重启也会一会儿就挂掉，让人十分郁闷

解决方案：
其实就是不知道为什么电脑缺了tornado，或者就是tornado有问题。此时可以通过运行下面的代码进行解决（两个中任选一个就行，一个不行的话就试试另外一个）

（一）conda重新安装jupyter tornado/mkl
conda uninstall jupyter tornado#此处如果显示已经没有tornado那就直接执行下一条代码就可以了

```python
conda install jupyter tornado
```

（二）pip安装
如果还不行直接指定版本：

```python
pip install "pyzmq==17.0.0" "ipykernel==4.8.2"
```

#### 扩大jupyter运行内存

要扩大Jupyter运行内存，你可以按照以下步骤操作：

打开终端或命令提示符窗口。<br/>
输入以下命令以生成Jupyter配置文件：<br/>
jupyter notebook --generate-config<br/>
找到生成的配置文件路径。在终端输出中，你会看到类似于以下内容的一行：<br/>
Writing default config to: /path/to/.jupyter/jupyter_notebook_config.py<br/>
其中/path/to/是配置文件的所在路径。<br/>
打开生成的配置文件，可以使用任何文本编辑器进行编辑。<br/>
搜索并找到以下行（如果找不到，可以手动添加）：<br/>

# c.NotebookApp.memory_limit = 0<br/>

将该行解除注释并修改为：<br/>
c.NotebookApp.memory_limit = <your_memory_limit><br/>
将<your_memory_limit>替换为你想要设置的内存限制，以字节为单位。例如，如果你想将内存限制设置为4GB（4 *1024* 1024 * 1024字节），可以写为：<br/>
c.NotebookApp.memory_limit = 4294967296<br/>
保存配置文件并关闭编辑器。<br/>
重新启动Jupyter Notebook服务器。在终端或命令提示符窗口中，输入以下命令：<br/>
jupyter notebook<br/>
Jupyter Notebook将使用你指定的内存限制重新启动。<br/>
请注意，增加Jupyter运行内存可能会影响系统性能，特别是当你将内存限制设置得非常高时。确保你的系统具有足够的可用内存，并根据你的需求和系统资源进行适当的配置。<br/>
