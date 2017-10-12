1 nn.Sequential()
这个表示将一个有序的模块写在一起，也就相当于将神经网络的层按顺序放在一起，这样可以方便结构显示
2 nn.Conv2d()

这个是卷积层，里面常用的参数有四个，in_channels, out_channels, kernel_size, stride, padding
in_channels表示的是输入卷积层的图片厚度
out_channels表示的是要输出的厚度
kernel_size表示的是卷积核的大小，可以用一个数字表示长宽相等的卷积核，比如kernel_size=3，也可以用不同的数字表示长宽不同的卷积核，比如kernel_size=(3, 2)
stride表示卷积核滑动的步长
padding表示的是在图片周围填充0的多少，padding=0表示不填充，padding=1四周都填充1维

3 nn.ReLU()
这个表示使用ReLU激活函数，里面有一个参数inplace，默认设置为False，表示新创建一个对象对其修改，也可以设置为True，表示直接对这个对象进行修改

4 nn.MaxPool2d()
这个是最大池化层，当然也有平均池化层，里面的参数有kernel_size, stride, padding
kernel_size表示池化的窗口大小，和卷积层里面的kernel_size是一样的
stride也和卷积层里面一样，需要自己设置滑动步长
padding也和卷积层里面的参数是一样的，默认是0
模型需要传入的参数是输入的图片维数以及输出的种类数
