# VideoSave

[![Python Version](https://img.shields.io/badge/python-3.11+-green)](https://www.python.org)
[![star](https://gitee.com/shiya_liu/VideoSave/badge/star.svg?theme=white)](https://gitee.com/shiya_liu/VideoSave/stargazers)
[![fork](https://gitee.com/shiya_liu/VideoSave/badge/fork.svg?theme=white)](https://gitee.com/shiya_liu/VideoSave/members)

![Snipaste_2023-11-17_11-25-49](assets/Snipaste_2023-11-17_11-25-49.png)

# 开发初衷

#### 开发背景

当院线上新一部期待已久的电影时，每次度娘"xx免费在线观看"总能找出一堆参差不齐的资源，并且无法下载到本地观看。下班回到出租房网络情况较差，影响观看体验。 😱

#### 提供功能

- 节省寻找资源的时间 ⌚️
- 模糊搜索指定影片 🐴
- 查看影片下载日志 🦜
- 保证影片质量 🎬
- 每周上新,保证影片更新时间(等等党的福利) 🎦
- 本地保存反复观看 🌹

#### 适用人群

- 喜欢电影但休闲时间网络条件差，网络良好时条件不允许在线观看 💦
- 喜欢电影但独自在外拼搏，无心去影院吃狗粮 🫂
- 喜欢电影但处于奋斗阶段，需要“把钱花在刀刃上”💪

# 功能缺陷

> 说明：本项目存在一些已知的缺陷，但是并不影响正常状态下的使用。由于平时工作繁忙，这些缺陷会在空闲时间修复，时间不定。



- 不提供修改密码，如有需求请联系作者手动修改 ✋🏻
- 只能一部一部的下载 🐱
- 下载过程中关闭程序可能会导致崩溃(下载未开始或已经下载完毕不会出现此情况) 🐭
- 点击后无反应时请耐心等待，短时间内连续多次点击可能导致崩溃(网络带宽限制导致) 🐍
- ~~搜索电影只会反馈名称，没有图像以求减少非必要的请求压力~~  (已经取消此限制) 🐲

# 安装使用

#### 体验版地址(推荐)

- [MacOS](https://gitee.com/shiya_liu/VideoSave/releases/download/v0.1/VideoSave_macos.zip)
- [Windows](https://gitee.com/shiya_liu/VideoSave/releases/download/v0.1/VideoSave_windows.zip)



#### ~~下载地址~~

- ~~[MacOS](https://gitee.com/shiya_liu/VideoSave/releases/download/v1.0/VideoSave_macos.zip)~~
- ~~[Windows](https://gitee.com/shiya_liu/VideoSave/releases/download/v1.0/VideoSave_windows.zip)~~
- ~~[Source code](https://gitee.com/shiya_liu/VideoSave/archive/refs/tags/v1.0.tar.gz)~~

#### 安装过程

**Mac**

1、解压缩安装包得到程序

![image-20231119014457294](assets/image-20231119014457294.png)

**注意： 直接启动安装程序会闪退！！！**

2、点击“访达” ---> 应用程序，将VideoSave放到其中

![image-20231119014619192](assets/image-20231119014619192.png)

3、进入启动台

![image-20231119020357495](assets/image-20231119020357495.png)

4、启动程序

![image-20231119020521754](assets/image-20231119020521754.png)



**Windows**

1、解压安装包

![c7a0b6d949440833f2368d2cd14f9b28](assets/c7a0b6d949440833f2368d2cd14f9b28.png)

![d564c94b3f4846a1652cb20971534034](assets/d564c94b3f4846a1652cb20971534034.png)

![187770a312431f4e897b9b03da94336a](assets/187770a312431f4e897b9b03da94336a.png)

2、找到程序文件

![2d2d38fa97821e536c226350c4395008](assets/2d2d38fa97821e536c226350c4395008.png)

3、创建快捷方式

![e9b9acb268968bd0af93afb3b35f4734](assets/e9b9acb268968bd0af93afb3b35f4734.jpg)

4、点击运行

![3d1bb7c441c908ceab507ced55c437d8](assets/3d1bb7c441c908ceab507ced55c437d8.jpg)

![bcb8157db295a8c714510634dc91d3c7](assets/bcb8157db295a8c714510634dc91d3c7.jpg)

#### 如何使用

![imageonline-co-gifimage](assets/imageonline-co-gifimage.gif)

# 源码

> 说明：作者职业是运维，平时学习Python而写的此项目，代码能力有限。源码未经过pylint或sonarqube等质量检测工具扫描。后续空闲时将对代码质量进行把关，也请感兴趣的developer指点。

#### 本地构建

> ```python
> # 当你想要clone代码本地尝试时，请记得修改数据库连接地址并导入数据，数据库内的电影数据请自行寻找资源。release软件包中已经设置为有效连接地址，源码中是本地VMware虚拟机的地址，请不要尝试连接。
> conn = pymongo.MongoClient('mongodb://public123:Pub123.lic@10.0.0.18:27017/?authSource=video')
> ```

**Mac**

```shell
(venv) reqiqiu@reqiqiundiannao VideoSave % ./venv/bin/pyinstaller -w --name "VideoSave" --icon=icon.ico  --collect-datas=fake_useragent -D app.py
119 INFO: PyInstaller: 6.1.0
119 INFO: Python: 3.11.6
126 INFO: Platform: macOS-13.0-arm64-arm-64bit
......
7269 INFO: Building BUNDLE BUNDLE-00.toc completed successfully.
```

参数`--collect-datas=fake_useragent`源于 https://github.com/fake-useragent/fake-useragent/issues/155

**Windows**

```shell
(venv) PS E:\Users\Administrator\PycharmProjects\VideoSave> .\venv\Scripts\pyinstaller.exe -w --name "VideoSave" --icon=icon.ico  --collect-datas=fake_useragent 
-D app.py
263 INFO: PyInstaller: 6.1.0
263 INFO: Python: 3.11.0
272 INFO: Platform: Windows-10-10.0.19045-SP0
......
14405 INFO: Building COLLECT COLLECT-00.toc completed successfully.
```

# 问题反馈

#### 反馈渠道

请在下面两个Issue地址中二选一进行反馈，在反馈时请携带日志（程序安装路径下，名为VideoSave.log）

- [Gitee Issue](https://gitee.com/shiya_liu/VideoSave/issues)

- [GitHub Issue](https://github.com/LiuShiYa-github/VideoSave/issues)

# 视频来源

- 视频资源均来自互联网分享站点所提供的公开引用资源，本程序只是将视频网站中的m3u8地址获取并解析得到具体的TS地址并合成片段而得到视频。
- 请忽相信视频中的任何广告信息。
- 当视频来源的网站down掉后将无法使用本软件进行下载资源。

# 免责声明
VideoSave所有内容均来自互联网分享站点所提供的公开引用资源，该软件以及视频资源仅作为阅读交流使用，并无任何商业目的，其版权归作者或出版社所有，本软件不对所涉及的版权问题负法律责任。





