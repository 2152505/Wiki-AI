![vf1](./images/variinfer.png)
![vf1](./images/varinfer2.png)

### 个人理解：

实际上，变分推理的核心就是在于如何模拟一个贝叶斯后验分布，因为其本身难以求得
因此需要进行近似地变换，例如利用神经网络做一个近似，因为神经网络最终的输出可
以看作是一个概率分布，因此不断地学习就可以尽可能地模拟所求的分布。
而损失函数则是用来进行学习的标准。