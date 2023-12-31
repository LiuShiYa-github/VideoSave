# This Python file uses the following encoding: utf-8
import shutil
import sys
import multiprocessing_win
import multiprocessing
from PySide6 import QtGui
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget, QStackedWidget, QFileDialog
from PySide6.QtCore import (QThread, Slot, Signal, QSize)
from utils.index import Ui_Form as Index_Ui_Form
from utils.form import Ui_Form as Home_Ui_Form
from utils.Log import Ui_Form as Log_Ui_Form
import utils.icon
import os
import time
import requests
from tqdm import tqdm
import glob
from fake_useragent import UserAgent
import logging
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED
import pymongo

logging.basicConfig(filename='{}/VideoSave.log'.format(os.path.split(os.path.realpath(__file__))[0]),
                    level=logging.INFO, filemode='w',
                    format='%(asctime)s - %(levelname)s - %(message)s', encoding='utf-8')
# 当你想要clone代码本地尝试时，请记得修改数据库连接地址并导入数据，数据库内的电影数据请自行寻找资源。
conn = pymongo.MongoClient('mongodb://public:Pub123.lic@10.0.0.18:27017/?authSource=video')
db = conn['video']
videoset = db['video']
userset = db['user']


class Login(QWidget):
    """
    登录注册页面
    """

    def __init__(self):
        super().__init__()
        self.index = Index_Ui_Form()
        self.index.setupUi(self)
        self.show()
        self.index.radioButton.hide()
        self.login_username = self.index.login_username
        self.login_password = self.index.login_password
        self.register_username = self.index.register_username
        self.register_password = self.index.register_password
        self.register_password_2 = self.index.register_password_2
        self.index.tabWidget.setCurrentIndex(0)

        self.index.label_Gitee.setText("<a href='https://gitee.com/shiya_liu/VideoSave'>源码</a>")
        self.index.label_GitHub.setText("<a href='https://gitee.com/shiya_liu/VideoSave/releases'>发版详情</a>")
        self.index.label_Gitee.setOpenExternalLinks(True)
        self.index.label_GitHub.setOpenExternalLinks(True)

    def login_submit(self):
        # 首选判断用户活动页面
        if self.index.tabWidget.currentIndex() == 0:
            # 登录页
            login_username = self.index.login_username.text().strip()
            login_password = self.index.login_password.text().strip()
            # 查询mongo用户名或密码
            result = userset.find_one({"user_name": login_username})

            # 用户没有输入账户密码
            if not login_username or not login_password:
                QMessageBox.warning(self, "错误", "登录页面用户名或密码不能为空")
                return False
            # 用户输入用户名密码 但是用户不存在
            elif result == None:
                # 用户不存在
                QMessageBox.warning(self, "错误", "用户不存在")
                self.index.login_username.clear()
                self.index.login_password.clear()
                return False
            else:
                # 获取用户密码
                mysql_password = result['password']
                # 密码不正确
                if login_password == mysql_password:
                    # 切换到主页
                    QMessageBox.information(self, "正确", "登录成功")
                    return True
                else:
                    QMessageBox.warning(self, "错误", "密码不正确")
                    self.index.login_username.clear()
                    self.index.login_password.clear()
                    return False

        else:
            # 注册页面
            register_username = self.index.register_username.text().strip()
            register_password = self.index.register_password.text().strip()
            register_password_2 = self.index.register_password_2.text().strip()
            # 校验用户输入的手机号
            # ret = re.match(r"^1[35678]\d{9}$", register_username)

            # if not ret:
            #     QMessageBox.warning(self, "错误", "请输入正确的手机号")
            #     self.index.register_username.clear()
            #     self.index.register_password.clear()
            #     self.index.register_password_2.clear()
            #     return False

            # 查询MySQL用户名或密码
            result = userset.find_one({"user_name": register_username})
            # 用户名密码不可以为空
            if not register_username or not register_password or not register_password_2:
                QMessageBox.warning(self, "错误", "注册页面用户名或密码不能为空")
                self.index.register_username.clear()
                self.index.register_password.clear()
                self.index.register_password_2.clear()
                return False
            # 两次密码是否一致
            if register_password != register_password_2:
                QMessageBox.warning(self, "错误", "两次密码不一致")
                self.index.register_username.clear()
                self.index.register_password.clear()
                self.index.register_password_2.clear()
                return False
            # 用户是否已经存在
            if result != None:
                # 用户已经存在
                QMessageBox.warning(self, "错误", "用户已经存在，请勿重复注册")
                self.index.register_username.clear()
                self.index.register_password.clear()
                self.index.register_password_2.clear()
                return False
            else:
                # 注册
                info = {"user_name": register_username, "password": register_password}
                userset.insert_one(info)
                QMessageBox.information(self, "正确", "注册成功")
                self.index.register_username.clear()
                self.index.register_password.clear()
                self.index.register_password_2.clear()
                # 注册成功后 将活动页设置为登录页 方便用户登录
                self.index.tabWidget.setCurrentIndex(0)
                # 只有当登录成功才返回true 注册成功仍然不能进入主页
                return False


class ShowFilmImage(QThread):
    """
    显示电影名称和封面图
    """
    image = Signal(list)
    film = Signal(list)
    load = Signal(bool)

    def __init__(self, page, search_str):
        super().__init__()
        self.page_num = page
        self.search_str = search_str

    def run(self):
        if self.search_str == "":
            self.load.emit(False)
            result = videoset.find().skip((self.page_num - 1) * 10).limit(10)
            res_list = []
            film_list = []
            for doc in result:
                res_list.append(doc['film_image_url'])
                film_list.append(doc['film_name'])
            self.load.emit(True)
            self.image.emit(res_list)
            self.film.emit(film_list)
        else:
            self.load.emit(False)
            res = videoset.find({"film_name": {"$regex": self.search_str}})
            res_list = []
            film_list = []
            num = 0
            for doc in res:
                if num >= 10:
                    break
                else:
                    num += 1
                    res_list.append(doc['film_image_url'])
                    film_list.append(doc['film_name'])
            self.load.emit(True)
            self.image.emit(res_list)
            self.film.emit(film_list)

class DownloadProgress(QThread):
    """
    下载电影
    """
    progress = Signal(int, int)

    def __init__(self, download_path, film_name):
        super().__init__()
        self.home = Home_Ui_Form()
        self.download_path = download_path
        self.film_name = film_name
        self.headers = {'User-Agent': UserAgent().random}

    def get_m3u8(self, url):
        """
        获取m3u8
        返回ts个数列表以及列表
        """
        m3u8 = requests.get(url=url, headers=self.headers, timeout=60).text
        data = m3u8.split()
        ts_list = []
        for meta in data:
            if 'EXT' not in meta:
                ts_list.append(meta)
        return len(ts_list), ts_list

    def piecing_download_addr(self, ts_list, base_url):
        """
        拼凑完整的内容下载地址列表
        返回完整URL列表
        """
        url_list = []
        if 'http' not in ts_list[0]:
            for url in ts_list:
                ts_url = base_url + url
                url_list.append(ts_url)
            return url_list
        # https://s9.fsvod1.com/20231012/FAbqyeR4/2000kb/hls/
        elif '/2023' in ts_list[0]:
            base_url = base_url.split('2023')[0]
            for url in ts_list:
                ts_url = base_url + url
                url_list.append(ts_url)
            return url_list
        else:
            return ts_list

    def threadpool_download(self, url, fail_list, video_name, ts_count, download_num, download_path):
        """
        多线程下载视频内容
        """
        try:
            video_res = requests.get(url, headers=self.headers, timeout=60)
            if video_res.status_code == 200:
                video_data = video_res.content
                logging.info(
                    "视频:《{}》 一共有:{}个片段，正在下载第:{}个片段, 链接是:{}".format(video_name, ts_count,
                                                                                      download_num,
                                                                                      url))
                with open('{}/{}/{}'.format(download_path, video_name, '{:0>5d}.ts'.format(download_num)), 'ab') as f:
                    f.write(video_data)
                file_num = glob.glob(os.path.join(download_path + '/' + video_name, '*.ts'))
                self.progress.emit(int(ts_count), len(file_num))
            else:
                fail_list.append(url)
        except Exception as e:
            fail_list.append(url)
            logging.warning(e)

        return fail_list

    def retry_fail(self, fail_list, video_name, url_list, download_path, ts_count):
        """
        重试第一次下载失败的URL
        返回重试后仍然失败的URL个数
        """
        error_url = []
        num = 0
        for fail_url in fail_list:
            num += 1
            try:
                video_res = requests.get(fail_url, headers=self.headers, timeout=60)
                if video_res.status_code == 200:
                    video_data = video_res.content
                    number = url_list.index(fail_url) + 1
                    logging.info(
                        "重试第一次下载失败的视频： 视频:《{}》 共有 {}需要重试， 正在重试第 {} 个，编号为 {}".format(
                            video_name,
                            len(fail_list),
                            num,
                            number))
                    with open('{}/{}/{}'.format(download_path, video_name, '{:0>5d}.ts'.format(number)), 'ab') as f:
                        f.write(video_data)
                    file_num = glob.glob(os.path.join(download_path + '/' + video_name, '*.ts'))
                    self.progress.emit(int(ts_count), len(file_num))
                else:
                    error_url.append(fail_url)
                    logging.warning("下载失败:{}".format(fail_url))
            except Exception as e:
                logging.warning(e)
                error_url.append(fail_url)
        return len(error_url)

    def ts_to_mp4(self, video_name, path):
        """
        将ts视频片段合成mp4格式的视频
        """
        file_list = glob.glob(os.path.join(path + '/' + video_name, '*.ts'))
        file_list.sort()
        for file in tqdm(file_list, desc="正在转换视频格式："):
            if os.path.exists(file) and os.path.getsize(file) > 10000:
                with open(file, 'rb') as f1:
                    with open("{}/{}.mp4".format(path, video_name), 'ab') as f2:
                        f2.write(f1.read())
            else:
                logging.warning("文件 {} 不存在或小于10KB 跳过该文件的合并".format(file))
                continue
        # 清理存放目录
        if os.path.exists(path + '/' + video_name):
            shutil.rmtree(path + '/' + video_name)
            # os.system('rm -rf {}/{}'.format(path, video_name))

    def informations(self, video_name, ts_count, error_num, start_time, end_time, path):
        """
        汇总下载的信息 包括：
            视频名称
            目标文件数
            成功文件数
            失败文件数
            下载耗时
            视频大小
        """
        try:
            video_size = os.path.getsize('{}/{}.mp4'.format(path, video_name))
            logging.info("""
            ========================================
            || 视频名称     : 《{}》
            ----------------------------------------
            || 目标文件数   : {}
            ----------------------------------------
            || 失败文件数   : {}
            ----------------------------------------
            || 下载耗时     : {}分钟
            ----------------------------------------
            || 视频大小     : {}MB
            ========================================
            """.format(video_name, ts_count, error_num, (end_time - start_time) / 60, video_size / 1048576))
        except Exception as e:
            logging.warning(e)

    def mkdir(self, video_name, path):
        """
        创建ts视频片段存放路径
        """
        if os.path.exists(path + '/' + video_name):
            shutil.rmtree(path + '/' + video_name)
        os.makedirs(path + '/' + video_name)

    def run(self):
        """
        程序入口函数
        """
        res = videoset.find({"film_name": {"$regex": self.film_name}})
        for doc in res:
            video_name = doc['film_name']
            video_url = doc['film_url']
            start_time = time.time()
            self.mkdir(video_name=video_name, path=self.download_path)
            ts_count, ts_list = self.get_m3u8(url=video_url)
            if type(video_url) == bytes:
                video_url = video_url.decode('utf-8')
            base_url = video_url.replace(video_url.split('/')[-1], '')
            url_list = self.piecing_download_addr(ts_list=ts_list, base_url=base_url)
            fail_list = []
            executor = ThreadPoolExecutor(20)
            all_tasks = [
                executor.submit(self.threadpool_download, url, fail_list, video_name, ts_count, url_list.index(url),
                                self.download_path)
                for
                url in url_list]
            # 设置下载进度条
            for task in tqdm(all_tasks, desc="正在下载《{}》".format(video_name)):
                task.result()

            wait(all_tasks, return_when=ALL_COMPLETED)
            logging.info("第一次请求失败的URL列表:{}".format(fail_list))
            error_num = self.retry_fail(fail_list, video_name, url_list, self.download_path, ts_count)
            self.ts_to_mp4(video_name=video_name, path=self.download_path)
            end_time = time.time()
            self.informations(video_name, ts_count, error_num, start_time, end_time, path=self.download_path)
            return False


class Home(QWidget):
    """
    主页
    """

    def __init__(self):
        super().__init__()
        self.home = Home_Ui_Form()
        self.home.setupUi(self)
        # 默认关闭提示
        self.home.label_11.hide()
        # 点击下一页的次数
        self.num = 0
        if self.num == 0:
            self.home.pushButton_page_2.hide()
        # 正常情况下隐藏下载进度条
        self.home.label.hide()
        self.home.progressBar.hide()
        self.show()
        # 搜索
        self.search = self.home.lineEdit.text().strip()
        self.home.pushButton.clicked.connect(self.search_fun)
        # 页码总量
        self.pageCount = 0
        # 翻页
        self.page = 1
        self.home.pushButton_1.clicked.connect(self.switchpage_1)
        self.home.pushButton_2.clicked.connect(self.switchpage_2)
        self.home.pushButton_3.clicked.connect(self.switchpage_3)
        self.home.pushButton_4.clicked.connect(self.switchpage_4)
        self.home.pushButton_5.clicked.connect(self.switchpage_5)
        self.home.pushButton_6.clicked.connect(self.switchpage_6)
        self.home.pushButton_7.clicked.connect(self.switchpage_7)
        self.home.pushButton_8.clicked.connect(self.switchpage_8)
        self.home.pushButton_9.clicked.connect(self.switchpage_9)
        self.home.pushButton_10.clicked.connect(self.switchpage_10)
        # 点击下一页
        self.home.pushButton_page.clicked.connect(self.down_pushButton)

        # 点击上一页
        self.home.pushButton_page_2.clicked.connect(self.up_pushButton)
        # 设置存放路径
        self.path = ''
        self.home.toolButtonSeting.clicked.connect(self.download_path)
        # 触发下载
        self.home.toolButtonDownload.clicked.connect(self.download)

    def down_pushButton(self):
        """
        下一页按钮函数
        """
        self.num += 1
        self.page = 10
        # 更新当前页码
        # self.home.lineEdit_showpage.setText("{}/{}页".format(self.page * self.num + 1, str(self.pageCount)))
        self.home.lineEdit_showpage.setText("{}页".format(self.page * self.num + 1))
        self.home.lineEdit_showpage.setReadOnly(True)
        self.home.pushButton_1.setText(str(self.num * 10 + 1))
        self.home.pushButton_2.setText(str(self.num * 10 + 2))
        self.home.pushButton_3.setText(str(self.num * 10 + 3))
        self.home.pushButton_4.setText(str(self.num * 10 + 4))
        self.home.pushButton_5.setText(str(self.num * 10 + 5))
        self.home.pushButton_6.setText(str(self.num * 10 + 6))
        self.home.pushButton_7.setText(str(self.num * 10 + 7))
        self.home.pushButton_8.setText(str(self.num * 10 + 8))
        self.home.pushButton_9.setText(str(self.num * 10 + 9))
        self.home.pushButton_10.setText(str(self.num * 10 + 10))
        self.home.label_11.show()
        self.ShowFilmImage = ShowFilmImage(page=self.page * self.num + 1, search_str=self.search)
        self.ShowFilmImage.image.connect(self.showimage)
        self.ShowFilmImage.film.connect(self.showname)
        self.ShowFilmImage.load.connect(self.load)
        self.ShowFilmImage.start()
        self.home.label_11.hide()
        if self.num >= 1:
            self.home.pushButton_page_2.show()

    def up_pushButton(self):
        """
        上页按钮
        """
        self.num -= 1
        self.page = 10
        # 更新当前页码
        # self.home.lineEdit_showpage.setText("{}/{}页".format(self.page * self.num + 1, str(self.pageCount)))
        self.home.lineEdit_showpage.setText("{}页".format(self.page * self.num + 1))
        self.home.lineEdit_showpage.setReadOnly(True)
        self.home.pushButton_1.setText(str(self.num * 10 + 1))
        self.home.pushButton_2.setText(str(self.num * 10 + 2))
        self.home.pushButton_3.setText(str(self.num * 10 + 3))
        self.home.pushButton_4.setText(str(self.num * 10 + 4))
        self.home.pushButton_5.setText(str(self.num * 10 + 5))
        self.home.pushButton_6.setText(str(self.num * 10 + 6))
        self.home.pushButton_7.setText(str(self.num * 10 + 7))
        self.home.pushButton_8.setText(str(self.num * 10 + 8))
        self.home.pushButton_9.setText(str(self.num * 10 + 9))
        self.home.pushButton_10.setText(str(self.num * 10 + 10))
        self.ShowFilmImage = ShowFilmImage(page=self.page * self.num + 1, search_str=self.search)
        self.ShowFilmImage.image.connect(self.showimage)
        self.ShowFilmImage.film.connect(self.showname)
        self.ShowFilmImage.load.connect(self.load)
        self.ShowFilmImage.start()
        if self.num <= 0:
            self.home.pushButton_page_2.hide()

    def download(self):
        """
        下载按钮
        """
        # 判断是否已经设置了下载路径
        if self.path == '':
            QMessageBox.warning(self, "错误", "请设置视频存放地址")
            return False
        # 优化
        checkBox_dict = {
            self.home.checkBox_1.text().strip(): self.home.checkBox_1.isChecked(),
            self.home.checkBox_2.text().strip(): self.home.checkBox_2.isChecked(),
            self.home.checkBox_3.text().strip(): self.home.checkBox_3.isChecked(),
            self.home.checkBox_4.text().strip(): self.home.checkBox_4.isChecked(),
            self.home.checkBox_5.text().strip(): self.home.checkBox_5.isChecked(),
            self.home.checkBox_6.text().strip(): self.home.checkBox_6.isChecked(),
            self.home.checkBox_7.text().strip(): self.home.checkBox_7.isChecked(),
            self.home.checkBox_8.text().strip(): self.home.checkBox_8.isChecked(),
            self.home.checkBox_9.text().strip(): self.home.checkBox_9.isChecked(),
            self.home.checkBox_10.text().strip(): self.home.checkBox_10.isChecked()
        }
        # 只每次允许下载一个视频
        num = 0
        for selected in checkBox_dict:
            if checkBox_dict[selected]:
                num += 1
        if num >= 2:
            QMessageBox.warning(self, "错误", "每次只能下载一个视频")
            self.home.checkBox_1.setChecked(False)
            self.home.checkBox_2.setChecked(False)
            self.home.checkBox_3.setChecked(False)
            self.home.checkBox_4.setChecked(False)
            self.home.checkBox_5.setChecked(False)
            self.home.checkBox_6.setChecked(False)
            self.home.checkBox_7.setChecked(False)
            self.home.checkBox_8.setChecked(False)
            self.home.checkBox_9.setChecked(False)
            self.home.checkBox_10.setChecked(False)
            return
        for film_name in checkBox_dict:
            if checkBox_dict[film_name]:
                # 触发线程进行下载
                self.home.label.show()
                self.home.progressBar.show()
                # 开始下载线程
                self.DownloadProgress = DownloadProgress(download_path=self.path, film_name=film_name)
                self.DownloadProgress.progress.connect(self.updateprogress)
                self.DownloadProgress.start()
        self.home.checkBox_1.setChecked(False)
        self.home.checkBox_2.setChecked(False)
        self.home.checkBox_3.setChecked(False)
        self.home.checkBox_4.setChecked(False)
        self.home.checkBox_5.setChecked(False)
        self.home.checkBox_6.setChecked(False)
        self.home.checkBox_7.setChecked(False)
        self.home.checkBox_8.setChecked(False)
        self.home.checkBox_9.setChecked(False)
        self.home.checkBox_10.setChecked(False)

    def updateprogress(self, total, progress):
        """
        更新下载进度
        """
        self.home.progressBar.setRange(0, total)
        self.home.progressBar.valueChanged.connect(self.home.progressBar.setValue(progress))
        # 下载按钮置灰
        if (total - 100) > progress > 0:
            self.home.toolButtonDownload.setEnabled(False)
        else:
            self.home.toolButtonDownload.setEnabled(True)
        #     QMessageBox.information(self, '正确', '下载成功')

        # if progress == total:
        #     QMessageBox.warning(self, "成功", "下载成功")
        #     self.home.toolButtonDownload.setEnabled(True)
        #     return False
        # elif 0 < total - progress < 100:
        #     QMessageBox.warning(self, "成功", "下载成功但是有{}个片段失败，详情请见日志".format(total - progress))
        #     self.home.toolButtonDownload.setEnabled(True)
        #     return False
        # # 下载失败的情况有两种 一种是没有下载TS 二种是失败数超过100个TS
        # elif progress == 0:
        #     QMessageBox.warning(self, "失败", "下载失败详细信息请见日志")
        #     self.home.toolButtonDownload.setEnabled(True)
        #     return False
        # # 下载过程中
        # elif (total - 100) > progress > 0:
        #     self.home.toolButtonDownload.setEnabled(False)

    def download_path(self):
        """
        设置下载路径
        """
        film_path = QFileDialog.getExistingDirectory(window, "选择存放电影的文件路径")
        self.path = film_path

    def search_fun(self):
        """
        搜索函数
        """
        search = self.home.lineEdit.text().strip()
        if search == "":
            QMessageBox.warning(self, "错误", "请输入搜索名称")
        else:
            self.ShowFilmImage = ShowFilmImage(page=self.page * self.num + 1, search_str=search)
            self.ShowFilmImage.image.connect(self.showimage)
            self.ShowFilmImage.film.connect(self.showname)
            self.ShowFilmImage.load.connect(self.load)
            self.ShowFilmImage.start()

        # if search == "":
        #     QMessageBox.warning(self, "错误", "请输入搜索名称")
        # else:
        #     print("后台数据加载中 请稍后")
        #     self.home.label_11.show()
        #     # self.load.emit(False)
        #     res = videoset.find({"film_name": {"$regex": search}})
        #     res_list = []
        #     film_list = []
        #     num = 0
        #     for doc in res:
        #         if num > 10:
        #             break
        #         else:
        #             num += 1
        #             # 进行展示
        #             res_list.append(doc['film_image_url'])
        #             film_list.append(doc['film_name'])
        #     if num == 0:
        #         QMessageBox.warning(self, "错误", "没有找到该资源")
        #         self.home.lineEdit.clear()
        #     else:
        #         self.home.label_11.hide()
        #         # self.load.emit(True)
        #         self.showimage(res_list)
        #         self.showname(film_list)
        #         self.home.lineEdit.clear()

    def switchpage_1(self):
        """
        翻页按钮1
        """
        self.ShowFilmImage = ShowFilmImage(page=self.page * self.num + 1, search_str=self.search)
        self.ShowFilmImage.image.connect(self.showimage)
        self.ShowFilmImage.film.connect(self.showname)
        self.ShowFilmImage.load.connect(self.load)
        self.ShowFilmImage.start()
        # 更新当前页码
        # self.home.lineEdit_showpage.setText("{}/{}页".format(str(self.page * self.num + 1), str(self.pageCount)))
        self.home.lineEdit_showpage.setText("{}页".format(str(self.page * self.num + 1)))
        self.home.lineEdit_showpage.setReadOnly(True)

    def switchpage_2(self):
        """
        翻页按钮2
        """
        self.ShowFilmImage = ShowFilmImage(page=self.page * self.num + 2, search_str=self.search)
        self.ShowFilmImage.image.connect(self.showimage)
        self.ShowFilmImage.film.connect(self.showname)
        self.ShowFilmImage.load.connect(self.load)
        self.ShowFilmImage.start()
        # 更新当前页码
        # self.home.lineEdit_showpage.setText("{}/{}页".format(self.page * self.num + 2, str(self.pageCount)))
        self.home.lineEdit_showpage.setText("{}页".format(self.page * self.num + 2))
        self.home.lineEdit_showpage.setReadOnly(True)

    def switchpage_3(self):
        """
        翻页按钮3
        """
        self.ShowFilmImage = ShowFilmImage(page=self.page * self.num + 3, search_str=self.search)
        self.ShowFilmImage.image.connect(self.showimage)
        self.ShowFilmImage.film.connect(self.showname)
        self.ShowFilmImage.load.connect(self.load)
        self.ShowFilmImage.start()
        # 更新当前页码
        # self.home.lineEdit_showpage.setText("{}/{}页".format(self.page * self.num + 3, str(self.pageCount)))
        self.home.lineEdit_showpage.setText("{}页".format(self.page * self.num + 3))
        self.home.lineEdit_showpage.setReadOnly(True)

    def switchpage_4(self):
        """
        翻页按钮4
        """
        self.ShowFilmImage = ShowFilmImage(page=self.page * self.num + 4, search_str=self.search)
        self.ShowFilmImage.image.connect(self.showimage)
        self.ShowFilmImage.film.connect(self.showname)
        self.ShowFilmImage.load.connect(self.load)
        self.ShowFilmImage.start()
        # 更新当前页码
        # self.home.lineEdit_showpage.setText("{}/{}页".format(self.page * self.num + 4, str(self.pageCount)))
        self.home.lineEdit_showpage.setText("{}页".format(self.page * self.num + 4))
        self.home.lineEdit_showpage.setReadOnly(True)

    def switchpage_5(self):
        """
        翻页按钮5
        """
        self.ShowFilmImage = ShowFilmImage(page=self.page * self.num + 5, search_str=self.search)
        self.ShowFilmImage.image.connect(self.showimage)
        self.ShowFilmImage.film.connect(self.showname)
        self.ShowFilmImage.load.connect(self.load)
        self.ShowFilmImage.start()
        # 更新当前页码
        # self.home.lineEdit_showpage.setText("{}/{}页".format(self.page * self.num + 5, str(self.pageCount)))
        self.home.lineEdit_showpage.setText("{}页".format(self.page * self.num + 5))
        self.home.lineEdit_showpage.setReadOnly(True)

    def switchpage_6(self):
        """
        翻页按钮6
        """
        self.ShowFilmImage = ShowFilmImage(page=self.page * self.num + 6, search_str=self.search)
        self.ShowFilmImage.image.connect(self.showimage)
        self.ShowFilmImage.film.connect(self.showname)
        self.ShowFilmImage.load.connect(self.load)
        self.ShowFilmImage.start()
        # 更新当前页码
        self.home.lineEdit_showpage.setText("{}页".format(self.page * self.num + 6))
        self.home.lineEdit_showpage.setReadOnly(True)

    def switchpage_7(self):
        """
        翻页按钮7
        """
        self.ShowFilmImage = ShowFilmImage(page=self.page * self.num + 7, search_str=self.search)
        self.ShowFilmImage.image.connect(self.showimage)
        self.ShowFilmImage.film.connect(self.showname)
        self.ShowFilmImage.load.connect(self.load)
        self.ShowFilmImage.start()
        # 更新当前页码
        # self.home.lineEdit_showpage.setText("{}/{}页".format(self.page * self.num + 7, str(self.pageCount)))
        self.home.lineEdit_showpage.setText("{}页".format(self.page * self.num + 7))
        self.home.lineEdit_showpage.setReadOnly(True)

    def switchpage_8(self):
        """
        翻页按钮8
        """
        self.ShowFilmImage = ShowFilmImage(page=self.page * self.num + 8, search_str=self.search)
        self.ShowFilmImage.image.connect(self.showimage)
        self.ShowFilmImage.film.connect(self.showname)
        self.ShowFilmImage.load.connect(self.load)
        self.ShowFilmImage.start()
        # 更新当前页码
        # self.home.lineEdit_showpage.setText("{}/{}页".format(self.page * self.num + 8, str(self.pageCount)))
        self.home.lineEdit_showpage.setText("{}页".format(self.page * self.num + 8))
        self.home.lineEdit_showpage.setReadOnly(True)

    def switchpage_9(self):
        """
        翻页按钮9
        """
        self.ShowFilmImage = ShowFilmImage(page=self.page * self.num + 9, search_str=self.search)
        self.ShowFilmImage.image.connect(self.showimage)
        self.ShowFilmImage.film.connect(self.showname)
        self.ShowFilmImage.load.connect(self.load)
        self.ShowFilmImage.start()
        # 更新当前页码
        # self.home.lineEdit_showpage.setText("{}/{}页".format(self.page * self.num + 9, str(self.pageCount)))
        self.home.lineEdit_showpage.setText("{}页".format(self.page * self.num + 9))
        self.home.lineEdit_showpage.setReadOnly(True)

    def switchpage_10(self):
        """
        翻页按钮10
        """
        self.ShowFilmImage = ShowFilmImage(page=self.page * self.num + 10, search_str=self.search)
        self.ShowFilmImage.image.connect(self.showimage)
        self.ShowFilmImage.film.connect(self.showname)
        self.ShowFilmImage.load.connect(self.load)
        self.ShowFilmImage.start()
        # 更新当前页码
        # self.home.lineEdit_showpage.setText("{}/{}页".format(self.page * self.num + 10, str(self.pageCount)))
        self.home.lineEdit_showpage.setText("{}页".format(self.page * self.num + 10))
        self.home.lineEdit_showpage.setReadOnly(True)

    @Slot()
    def fun(self):
        """
        登录主页时显示内容
        """
        # 获取总页码
        # result = videoset.count_documents({})
        # if result % 10 == 0:
        #     pageCount = result // 10
        # else:
        #     pageCount = result // 10 + 1
        # self.pageCount = pageCount
        # self.home.lineEdit_showpage.setText("{}/{}页".format(1, pageCount))
        self.home.lineEdit_showpage.setText("{}页".format(1))
        self.home.lineEdit_showpage.setReadOnly(True)

        self.ShowFilmImage = ShowFilmImage(page=1, search_str=self.search)
        self.ShowFilmImage.image.connect(self.showimage)
        self.ShowFilmImage.film.connect(self.showname)
        self.ShowFilmImage.load.connect(self.load)
        self.ShowFilmImage.start()

    @Slot()
    def showimage(self, res_list):
        """
        显示图片
        """
        for res in range(0, len(res_list)):
            if res == 0:
                self.home.label_1.setScaledContents(True)
                pixmap = QPixmap.fromImage(QImage.fromData(res_list[res]))
                self.home.label_1.setPixmap(pixmap)
            elif res == 1:
                self.home.label_2.setScaledContents(True)
                pixmap = QPixmap.fromImage(QImage.fromData(res_list[res]))
                self.home.label_2.setPixmap(pixmap)
            elif res == 2:
                self.home.label_3.setScaledContents(True)
                pixmap = QPixmap.fromImage(QImage.fromData(res_list[res]))
                self.home.label_3.setPixmap(pixmap)
            elif res == 3:
                self.home.label_4.setScaledContents(True)
                pixmap = QPixmap.fromImage(QImage.fromData(res_list[res]))
                self.home.label_4.setPixmap(pixmap)
            elif res == 4:
                self.home.label_5.setScaledContents(True)
                pixmap = QPixmap.fromImage(QImage.fromData(res_list[res]))
                self.home.label_5.setPixmap(pixmap)
            elif res == 5:
                self.home.label_6.setScaledContents(True)
                pixmap = QPixmap.fromImage(QImage.fromData(res_list[res]))
                self.home.label_6.setPixmap(pixmap)
            elif res == 6:
                self.home.label_7.setScaledContents(True)
                pixmap = QPixmap.fromImage(QImage.fromData(res_list[res]))
                self.home.label_7.setPixmap(pixmap)
            elif res == 7:
                self.home.label_8.setScaledContents(True)
                pixmap = QPixmap.fromImage(QImage.fromData(res_list[res]))
                self.home.label_8.setPixmap(pixmap)
            elif res == 8:
                self.home.label_9.setScaledContents(True)
                pixmap = QPixmap.fromImage(QImage.fromData(res_list[res]))
                self.home.label_9.setPixmap(pixmap)
            elif res == 9:
                self.home.label_10.setScaledContents(True)
                pixmap = QPixmap.fromImage(QImage.fromData(res_list[res]))
                self.home.label_10.setPixmap(pixmap)



    @Slot()
    def showname(self, film_list):
        """
        显示电影名称
        """
        for film in film_list:
            if film is not None and film_list.index(film) == 0:
                self.home.checkBox_1.setText(film)
            if film is not None and film_list.index(film) == 1:
                self.home.checkBox_2.setText(film)
            if film is not None and film_list.index(film) == 2:
                self.home.checkBox_3.setText(film)
            if film is not None and film_list.index(film) == 3:
                self.home.checkBox_4.setText(film)
            if film is not None and film_list.index(film) == 4:
                self.home.checkBox_5.setText(film)
            if film is not None and film_list.index(film) == 5:
                self.home.checkBox_6.setText(film)
            if film is not None and film_list.index(film) == 6:
                self.home.checkBox_7.setText(film)
            if film is not None and film_list.index(film) == 7:
                self.home.checkBox_8.setText(film)
            if film is not None and film_list.index(film) == 8:
                self.home.checkBox_9.setText(film)
            if film is not None and film_list.index(film) == 9:
                self.home.checkBox_10.setText(film)

    @Slot()
    def load(self, bol):
        """
        显示正在加载中
        """
        if bol:
            self.home.label_11.hide()
        else:
            self.home.label_11.show()


class Log(QWidget):
    """
    查看日志
    """

    def __init__(self):
        super().__init__()
        self.log = Log_Ui_Form()
        self.log.setupUi(self)
        self.show()


class Main(QMainWindow):
    """
    控制页面显示
    """

    def __init__(self):
        super().__init__()
        self.show()
        self.stack = QStackedWidget()

        self.setCentralWidget(self.stack)

        self.login_page = Login()
        Login.resize(self, QSize(640, 530))
        Login.setMinimumSize(self, QSize(640, 530))
        Login.setMaximumSize(self, QSize(640, 530))
        self.stack.addWidget(self.login_page)

        self.home_page = Home()
        Home.resize(self, QSize(640, 530))
        Home.setMinimumSize(self, QSize(640, 530))
        Home.setMaximumSize(self, QSize(640, 530))
        self.stack.addWidget(self.home_page)

        self.login_page.index.pushButtonSubmit.clicked.connect(self.validate)

        self.log_page = Log()
        Log.resize(self, QSize(640, 530))
        Log.setMinimumSize(self, QSize(640, 530))
        Log.setMaximumSize(self, QSize(640, 530))
        self.stack.addWidget(self.log_page)

        self.home_page.home.toolButtonSeting_2.clicked.connect(self.logshow)

        self.log_page.log.pushButton.clicked.connect(self.goindex)



    def goindex(self):
        self.stack.setCurrentIndex(1)

    def logshow(self):
        self.stack.setCurrentIndex(2)
        with open('{}/VideoSave.log'.format(os.path.split(os.path.realpath(__file__))[0]), 'r', encoding='utf-8') as f:
            logcontent = f.read()
        self.log_page.log.textEdit.setText(logcontent)

    def validate(self):
        if self.login_page.login_submit():
            # 登录成功进入主页
            self.stack.setCurrentIndex(1)
            # 启动主页的电影显示
            self.home_page.fun()
        else:
            # 登录失败继续停留在登录页
            self.stack.setCurrentIndex(0)


if __name__ == "__main__":
    multiprocessing.freeze_support()
    # QGuiApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.Ceil)
    """
    参考：Pyinstaller 多进程代码打包 出现多个进程解决方案
    https://github.com/pyinstaller/pyinstaller/wiki/Recipe-Multiprocessing
    https://blog.csdn.net/wm9028/article/details/101208869
    """
    app = QApplication(sys.argv)
    # icon = QtGui.QIcon("./design/icon.png")
    # pixmap = icon.pixmap(icon.availableSizes()[0])
    # resized_pixmap = pixmap.scaled(22, 50)
    # app.setWindowIcon(QtGui.QIcon(resized_pixmap))
    app.setWindowIcon(QtGui.QIcon(':/icon.png'))
    window = Main()
    sys.exit(app.exec())
