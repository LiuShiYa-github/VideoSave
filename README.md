# VideoSave

[![Python Version](https://img.shields.io/badge/python-3.11+-green)](https://www.python.org)
[![star](https://gitee.com/shiya_liu/VideoSave/badge/star.svg?theme=white)](https://gitee.com/shiya_liu/VideoSave/stargazers)
[![fork](https://gitee.com/shiya_liu/VideoSave/badge/fork.svg?theme=white)](https://gitee.com/shiya_liu/VideoSave/members)

![Snipaste_2023-11-17_11-25-49](assets/Snipaste_2023-11-17_11-25-49.png)

#### 仓库详情

[![shiya.liu/VideoSave](https://gitee.com/shiya_liu/VideoSave/widgets/widget_card.svg?colors=393222,ebdfc1,fffae5,d8ca9f,393222,a28b40)](https://gitee.com/shiya_liu/VideoSave)

#### 开发背景

当院线上新一部期待已久的电影时，每次度娘"xx免费在线观看"总能找出一堆参差不齐的资源，并且无法下载到本地观看。下班回到出租房网络情况较差，影响观看体验。 😱

#### 提供功能

- 节省寻找资源的时间 ⌚️
- 模糊搜索指定影片 🐴
- 查看影片下载日志 🦜
- 保证影片质量 🎬
- 每周上新,保证影片更新时间(等等党的福利) 🎦
- 本地保存反复观看 🌹

#### 条件限制

- 必须要注册登录 🐶
- 只能一部一部的下载 🐱
- 在下载过程关闭窗口程序进程仍然存在 🐭



#### 适用人群

- 喜欢电影但休闲时间网络条件差，网络良好时条件不允许在线观看 💦
- 喜欢电影但独自在外拼搏，无心去影院吃狗粮 🫂
- 喜欢电影但处于奋斗阶段，需要“把钱花在刀刃上”💪

#### 下载地址



#### 如何使用

![imageonline-co-gifimage](assets/imageonline-co-gifimage.gif)

#### 本地构建

> ```python
> # 当你想要clone代码本地尝试时，请记得修改数据库连接地址并导入数据，数据库内的电影数据请自行寻找资源。release软件包中已经设置为有效连接地址，源码中是本地VMware虚拟机的地址，请不要尝试连接。
> db = pymysql.connect(host='10.0.0.18', user='root', password='123456', database='video', charset='utf8')
> cursor = db.cursor()
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
必须在Windows机器上编译exe，暂时没有机器。
```



#### 反馈问题

请在下面两个Issue地址中二选一进行反馈，在反馈时请携带日志（程序安装路径下，名为VideoSave.log）

- [Gitee Issue](https://gitee.com/shiya_liu/VideoSave/issues)

- [GitHub Issue](https://github.com/LiuShiYa-github/VideoSave/issues)



#### 免责声明
VideoSave所有内容均来自互联网分享站点所提供的公开引用资源，该软件以及视频资源仅作为阅读交流使用，并无任何商业目的，其版权归作者或出版社所有，本软件不对所涉及的版权问题负法律责任。





