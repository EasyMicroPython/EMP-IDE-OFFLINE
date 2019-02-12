# EMP-IDE 离线版本
这是EMP-IDE托管到Pypi上的一个python应用，他允许用户在本地开启EMP-IDE的Web服务，并且实现了数据在串口<-->Web浏览器之间的双向转发，这使得你可以通过串口连接或是无线wifi连接的方式，在浏览器能稳定高效的连接到你的MicroPython设备。



## 开始之前
在开始之前，你需要先明确以下的几点：
使用离线版本的EMP-IDE大致分为两步：

- 为MicroPython安装`emp-ext`扩展
- 获取离线版本的EMP-IDE

其中第一步，`emp-ext`是EMP项目中为MicroPython所封装的一套扩展指令，用于便捷的和EMP-IDE进行数据交互。**因此IDE的正常使用目前需要此项依赖的支持。**

该项依赖的安装和使用方法如下链接，本篇文章中便不再赘述：
<https://github.com/EasyMicroPython/EMP-EXT>

接下来我们在快速开始中着重介绍如何获取连线版本的EMP-IDE及其使用方法。



## 快速开始

### 安装
你可以在你的PC上使用pip安装EMP-IDE离线版本：
```sh
pip install emp-ide
```

pip在安装`emp-ide`包时，自动为系统添加了全局指令`empide`，你可以在Linux，Max或Windows下的命令行中轻易的运行这些指令。`empide`允许你使用有线和无线的方式进行连接，下面分别阐述。

### 有线串口连接
如果你使用串口连接你的MicroPython设备到PC，需要指明web服务的端口和串口设备的标识。
例如你有一个设备与你的PC进行了连接，在Linux下该设备标识为`/dev/ttyUSB0`,如果你想在5000的端口上运行EMP-IDE的Web服务，则需要在终端中使用如下指令：
```sh
empide --port=5000 --device=/dev/ttyUSB0
```
或者简写为：
```sh
empide 5000 /dev/ttyUSB0 
```
**注意： 请将 `/dev/ttyUSB0` 替换为你的串口设备标识。在Mac上可能类似于：`/dev/cu.SLAB_USBtoUART`，在Windows上类似于`COM1`**

**注意： 在Linux和Mac下，访问串口可能需要权限，因此建议在Linux和Mac下在指令前加入`sudo`，比如 `sudo empide /dev/ttyUSBO 5000`**


两个参数的含义分别为：
- device： 串口标识
- port： web服务的端口号, 默认为5000


执行完上述指令后，你将看到类似如下的输出：
```
==> Runing server...
 * Serving Flask app "emp_ide.ide" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
==> Launch browser...
 --> If the browser is not open as expected: ctrl + click the link below
 --> http://localhost:5000
==> Enable empwsb...
```

不出意外的话，你的默认浏览器将会自动打开 `http://127.0.0.1:5000`。如果你的默认浏览器不是Chrome的话，还是强烈建议使用Chrome浏览器，手动打开该网址。


### 无线连接
如果你想使用无线连接的方式，那么就无需指明`device`参数了。
如果你想在5000的端口上运行EMP-IDE的Web服务，则需要在终端中使用如下指令：
```sh
empide --port=5000
```
或者简写为：
```sh
empide 5000
```

同样不出意外的话，你的默认浏览器将会自动打开 `http://127.0.0.1:5000`。如果你的默认浏览器不是Chrome的话，还是强烈建议你使用Chrome浏览器，手动打开该网址。




## 支持的平台
- Windows
- Linux
- Mac

## PC上的依赖
- Python3
- Chrome浏览器（推荐Chrome，火狐也可以，但可能存在少许的兼容性问题）