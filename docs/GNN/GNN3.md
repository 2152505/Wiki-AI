### 理解图神经网络和信息传递机制

聚合算子 max add lstm
gamma是一个更新函数，xi也就是中心节点，从而得到最终的节点表示
。
N(u)邻居
update更新函数

#### 安装torch_geometric库（pyg）

正常步骤：

1. 在安装前要检查电脑的上的torch和cuda版本

import torch; print(torch.__version__)检查torch版本；

import torch; print(torch.version.cuda)检查cuda版本；

2. 检查完后，可以按照官网上的步骤直接用pip或者conda的命令进行安装；

（Installation — pytorch_geometric documentation (pytorch-geometric.readthedocs.io)）

下面的步骤只是针对不能正常安装或者是在官网上下载不了whl的用户
首先是根据官网上的步骤安装不成功的用户，可以根据（<https://data.pyg.org/whl/）这个网址上找到自己对应的版本；>

Eg：

因为我电脑的python == 3.6 torch==1.9.1 cuda==1.11所以我在官网的路径下找到了上述的四个文件并且将其下载下来

其次就是对其进行安装，安装顺序为：

1.torch-scatter 2.torch-sparse 3.torch-cluster 4.torch-spline-conv 5.torch-geometric

其中1-4的步骤是利用离线的安装包在本地进行安装，命令为 pip install +本地的路径+文件名称，最后一个安装包是利用镜像源下载，命令为 pip install torch-geometric +镜像源；到此本次的安装就全部结束。

Ps：

1. 镜像源：

-i   <https://pypi.doubanio.com/simple>
<https://mirrors.aliyun.com/pypi/simple/>
<https://pypi.tuna.tsinghua.edu.cn/simple>
2. 在<https://data.pyg.org/whl/这个网站上下载的时候要用到‘梯子’>

3. 在安装完毕后可以用下面的这段代码进行测试一下，（这个代码就是调用gcn的一个代码）

```python
import torch
from torch_geometric.nn import MessagePassing 
from torch_geometric.utils import add_self_loops, degree 
 
class GCNConv(MessagePassing):
    def __init__(self, in_channels, out_channels):
        super(GCNConv, self).__init__(aggr='add')  
        self.lin = torch.nn.Linear(in_channels, out_channels) 
 
    def forward(self, x, edge_index):  
        edge_index, _ = add_self_loops(edge_index, num_nodes=x.size(0))
        x = self.lin(x)
        return self.propagate(edge_index, size=(x.size(0), x.size(0)), x=x)
 
    def message(self, x_j, edge_index, size):
        row, col = edge_index
        deg = degree(row, size[0], dtype=x_j.dtype)
        deg_inv_sqrt = deg.pow(-0.5)
        norm = deg_inv_sqrt[row] * deg_inv_sqrt[col]
        return norm.view(-1, 1) * x_j
 
    def update(self, aggr_out):
        return aggr_out
 
if __name__ == '__main__':
    # 假设图节点属性向量的维度为16，图卷积出来的节点特征表示向量维度为32
    conv = GCNConv(16, 32)
    x = torch.randn(5, 16)
    print(x.shape)
    edge_index = [
        [0, 1, 1, 2, 1, 3],
        [1, 0, 2, 1, 3, 1]
    ]
    edge_index = torch.tensor(edge_index, dtype=torch.long)
    output = conv(x, edge_index)
    print(output.shape)
    print(output.data)
```

0->1则中心节点是1
N表示的是相邻节点，最终使用的聚合算法是想加，正好对应相加
核心思想，用身边的人来代替你（k-N算法）
