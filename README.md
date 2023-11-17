# VideoSave

[![Python Version](https://img.shields.io/badge/python-3.11+-green)](https://www.python.org)
[![star](https://gitee.com/shiya_liu/VideoSave/badge/star.svg?theme=white)](https://gitee.com/shiya_liu/VideoSave/stargazers)
[![fork](https://gitee.com/shiya_liu/VideoSave/badge/fork.svg?theme=white)](https://gitee.com/shiya_liu/VideoSave/members)

![Snipaste_2023-11-17_11-25-49](assets/Snipaste_2023-11-17_11-25-49.png)

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

必须要注册登录

只能一部一部的下载



#### 适用人群

- 喜欢电影但休闲时间网络条件差，网络良好时条件不允许在线观看 💦
- 喜欢电影但独自在外拼搏，无心去影院吃狗粮 🫂
- 喜欢电影但处于奋斗阶段，需要“把钱花在刀刃上”💪

#### 下载地址



#### 如何使用

![imageonline-co-gifimage](assets/imageonline-co-gifimage.gif)

#### 本地构建

> ```python
> # 当你想要clone代码本地尝试时，请记得修改数据库连接地址并导入数据，数据库内的电影数据请自行寻找资源。
> db = pymysql.connect(host='10.0.0.18', user='root', password='123456', database='video', charset='utf8')
> cursor = db.cursor()
> ```

**Mac**

```shell
(venv) reqiqiu@reqiqiundiannao VideoSave % ./venv/bin/pyinstaller -w -D  --name "VideoSave" --icon=icon.ico  --collect-datas=fake_useragent  app.py 
119 INFO: PyInstaller: 6.1.0
119 INFO: Python: 3.11.6
126 INFO: Platform: macOS-13.0-arm64-arm-64bit
127 INFO: wrote /Users/reqiqiu/代码/VideoSave/VideoSave.spec
129 INFO: Extending PYTHONPATH with paths
['/Users/reqiqiu/代码/VideoSave']
187 INFO: checking Analysis
187 INFO: Building Analysis because Analysis-00.toc is non existent
187 INFO: Initializing module dependency graph...
188 INFO: Caching module graph hooks...
195 INFO: Analyzing base_library.zip ...
603 INFO: Loading module hook 'hook-heapq.py' from '/Users/reqiqiu/代码/VideoSave/venv/lib/python3.11/site-packages/PyInstaller/hooks'...
644 INFO: Loading module hook 'hook-encodings.py' from '/Users/reqiqiu/代码/VideoSave/venv/lib/python3.11/site-packages/PyInstaller/hooks'...
1412 INFO: Loading module hook 'hook-pickle.py' from '/Users/reqiqiu/代码/VideoSave/venv/lib/python3.11/site-packages/PyInstaller/hooks'...
2099 INFO: Caching module dependency graph...
2133 INFO: Running Analysis Analysis-00.toc
2133 INFO: Looking for Python shared library...
2135 INFO: Using Python shared library: /opt/homebrew/Cellar/python@3.11/3.11.6/Frameworks/Python.framework/Versions/3.11/Python
2135 INFO: Analyzing /Users/reqiqiu/代码/VideoSave/app.py
2150 INFO: Loading module hook 'hook-PySide6.py' from '/Users/reqiqiu/代码/VideoSave/venv/lib/python3.11/site-packages/PyInstaller/hooks'...
2774 INFO: Loading module hook 'hook-charset_normalizer.py' from '/Users/reqiqiu/代码/VideoSave/venv/lib/python3.11/site-packages/_pyinstaller_hooks_contrib/hookstdhooks'...
2942 INFO: Loading module hook 'hook-certifi.py' from '/Users/reqiqiu/代码/VideoSave/venv/lib/python3.11/site-packages/_pyinstaller_hooks_contrib/hooks/stdhooks'...
3048 INFO: Loading module hook 'hook-multiprocessing.util.py' from '/Users/reqiqiu/代码/VideoSave/venv/lib/python3.11/site-packages/PyInstaller/hooks'...
3085 INFO: Loading module hook 'hook-xml.py' from '/Users/reqiqiu/代码/VideoSave/venv/lib/python3.11/site-packages/PyInstaller/hooks'...
3281 INFO: Loading module hook 'hook-pkg_resources.py' from '/Users/reqiqiu/代码/VideoSave/venv/lib/python3.11/site-packages/PyInstaller/hooks'...
3623 INFO: Loading module hook 'hook-platform.py' from '/Users/reqiqiu/代码/VideoSave/venv/lib/python3.11/site-packages/PyInstaller/hooks'...
3653 INFO: Loading module hook 'hook-sysconfig.py' from '/Users/reqiqiu/代码/VideoSave/venv/lib/python3.11/site-packages/PyInstaller/hooks'...
3686 INFO: Processing module hooks...
3693 INFO: Processing pre-safe import module hook win32com from '/Users/reqiqiu/代码/VideoSave/venv/lib/python3.11/site-packages/_pyinstaller_hooks_contrib/hooks/e_safe_import_module/hook-win32com.py'.
4055 INFO: Loading module hook 'hook-packaging.py' from '/Users/reqiqiu/代码/VideoSave/venv/lib/python3.11/site-packages/PyInstaller/hooks'...
4112 INFO: Loading module hook 'hook-PySide6.QtWidgets.py' from '/Users/reqiqiu/代码/VideoSave/venv/lib/python3.11/site-packages/PyInstaller/hooks'...
4187 INFO: Loading module hook 'hook-PySide6.QtCore.py' from '/Users/reqiqiu/代码/VideoSave/venv/lib/python3.11/site-packages/PyInstaller/hooks'...
4296 INFO: Loading module hook 'hook-PySide6.QtGui.py' from '/Users/reqiqiu/代码/VideoSave/venv/lib/python3.11/site-packages/PyInstaller/hooks'...
4367 INFO: Loading module hook 'hook-PySide6.QtDBus.py' from '/Users/reqiqiu/代码/VideoSave/venv/lib/python3.11/site-packages/PyInstaller/hooks'...
4430 INFO: Loading module hook 'hook-PySide6.QtNetwork.py' from '/Users/reqiqiu/代码/VideoSave/venv/lib/python3.11/site-packages/PyInstaller/hooks'...
4557 INFO: Looking for ctypes DLLs
4574 INFO: Analyzing run-time hooks ...
4576 INFO: Including run-time hook '/Users/reqiqiu/代码/VideoSave/venv/lib/python3.11/site-packages/PyInstaller/hooks/rthooks/pyi_rth_inspect.py'
4577 INFO: Including run-time hook '/Users/reqiqiu/代码/VideoSave/venv/lib/python3.11/site-packages/PyInstaller/hooks/rthooks/pyi_rth_pkgutil.py'
4578 INFO: Including run-time hook '/Users/reqiqiu/代码/VideoSave/venv/lib/python3.11/site-packages/PyInstaller/hooks/rthooks/pyi_rth_multiprocessing.py'
4580 INFO: Including run-time hook '/Users/reqiqiu/代码/VideoSave/venv/lib/python3.11/site-packages/PyInstaller/hooks/rthooks/pyi_rth_pkgres.py'
4582 INFO: Including run-time hook '/Users/reqiqiu/代码/VideoSave/venv/lib/python3.11/site-packages/PyInstaller/hooks/rthooks/pyi_rth_pyside6.py'
4587 INFO: Looking for dynamic libraries
4793 INFO: Warnings written to /Users/reqiqiu/代码/VideoSave/build/VideoSave/warn-VideoSave.txt
4805 INFO: Graph cross-reference written to /Users/reqiqiu/代码/VideoSave/build/VideoSave/xref-VideoSave.html
4816 INFO: checking PYZ
4816 INFO: Building PYZ because PYZ-00.toc is non existent
4816 INFO: Building PYZ (ZlibArchive) /Users/reqiqiu/代码/VideoSave/build/VideoSave/PYZ-00.pyz
5141 INFO: Building PYZ (ZlibArchive) /Users/reqiqiu/代码/VideoSave/build/VideoSave/PYZ-00.pyz completed successfully.
5145 INFO: EXE target arch: arm64
5145 INFO: Code signing identity: None
5146 INFO: checking PKG
5146 INFO: Building PKG because PKG-00.toc is non existent
5146 INFO: Building PKG (CArchive) VideoSave.pkg
5162 INFO: Building PKG (CArchive) VideoSave.pkg completed successfully.
5162 INFO: Bootloader /Users/reqiqiu/代码/VideoSave/venv/lib/python3.11/site-packages/PyInstaller/bootloader/Darwin-64bit/runw
5162 INFO: checking EXE
5163 INFO: Building EXE because EXE-00.toc is non existent
5163 INFO: Building EXE from EXE-00.toc
5163 INFO: Copying bootloader EXE to /Users/reqiqiu/代码/VideoSave/build/VideoSave/VideoSave
5165 INFO: Converting EXE to target arch (arm64)
5176 INFO: Removing signature(s) from EXE
5186 INFO: Appending PKG archive to EXE
5187 INFO: Fixing EXE headers for code signing
5190 INFO: Re-signing the EXE
5205 INFO: Building EXE from EXE-00.toc completed successfully.
5207 INFO: checking COLLECT
5207 INFO: Building COLLECT because COLLECT-00.toc is non existent
5207 INFO: Building COLLECT COLLECT-00.toc
6041 INFO: Building COLLECT COLLECT-00.toc completed successfully.
6044 INFO: checking BUNDLE
6045 INFO: Building BUNDLE because BUNDLE-00.toc is non existent
6045 INFO: Building BUNDLE BUNDLE-00.toc
7046 INFO: Signing the BUNDLE...
7269 INFO: Building BUNDLE BUNDLE-00.toc completed successfully.

```

参数`--collect-datas=fake_useragent`源于 https://github.com/fake-useragent/fake-useragent/issues/155

**Windows**

```shell
```



#### 反馈问题

请在下面两个Issue地址中二选一进行反馈，在反馈时请携带日志（程序安装路径下，名为VideoSave.log）

- [Gitee Issue](https://gitee.com/shiya_liu/VideoSave/issues)

- [GitHub Issue](https://github.com/LiuShiYa-github/VideoSave/issues)



#### 免责声明
VideoSave所有内容均来自互联网分享站点所提供的公开引用资源，该软件以及视频资源仅作为阅读交流使用，并无任何商业目的，其版权归作者或出版社所有，本软件不对所涉及的版权问题负法律责任。







