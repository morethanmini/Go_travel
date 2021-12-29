#여행을 떠나요
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton,
                             QGridLayout, QLabel, QGroupBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class MainUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('여행을 떠나요')
        self.setGeometry(700, 300, 500, 500)
        self.setWindowIcon(QIcon('cow.png'))
        self.setStyleSheet("background-color: #FFFFFF")

        self.setCentralWidget(SubUI())

class SubUI(QWidget):
    def __init__(self):
        super().__init__()
        self.Popups = []
        self.initUI()

    def initUI(self):

        # travle Group
        self.travle_group = QGroupBox('')
        self.travle_group.setAlignment(Qt.AlignCenter)

        self.travle_label1 = QLabel('아시아나항공 스케줄 검색')
        font1 = self.travle_label1.font()
        font1.setFamily("KoPub돋움체 Bold")
        font1.setPointSize(15)
        self.travle_label1.setFont(font1)


        self.travle_label2 = QLabel('KTX 열차 검색')
        self.travle_label2.setFont(font1)

        self.travle_label3 = QLabel('SRT 열차 검색')
        self.travle_label3.setFont(font1)

        self.travle_label4 = QLabel('네이버 지도 검색')
        self.travle_label4.setFont(font1)

        self.travle_label5 = QLabel('네이버 지하철 검색')
        self.travle_label5.setFont(font1)

        self.travle_label6 = QLabel('시외버스터미널 검색')
        self.travle_label6.setFont(font1)

        self.travle_btn1 = QPushButton('검색')
        self.travle_btn1.setStyleSheet("background-color: #E6E6E6;")
        self.travle_btn1.clicked.connect(self.asiana)

        self.travle_btn2 = QPushButton('검색')
        self.travle_btn2.clicked.connect(self.ktx)
        self.travle_btn2.setStyleSheet("background-color: #E6E6E6;")

        self.travle_btn3 = QPushButton('검색')
        self.travle_btn3.clicked.connect(self.srt)
        self.travle_btn3.setStyleSheet("background-color: #E6E6E6;")

        self.travle_btn4 = QPushButton('검색')
        self.travle_btn4.clicked.connect(self.navermap)
        self.travle_btn4.setStyleSheet("background-color: #E6E6E6;")

        self.travle_btn5 = QPushButton('검색')
        self.travle_btn5.clicked.connect(self.naversubway)
        self.travle_btn5.setStyleSheet("background-color: #E6E6E6;")

        self.travle_btn6 = QPushButton('검색')
        self.travle_btn6.clicked.connect(self.txbus)
        self.travle_btn6.setStyleSheet("background-color: #E6E6E6;")

        self.travle_layout = QGridLayout()
        #self.travle_layout.setAlignment(Qt.AlignCenter)
        self.travle_layout.setSpacing(50)
        self.travle_layout.addWidget(self.travle_label1, 0, 0)
        self.travle_layout.addWidget(self.travle_btn1, 0, 1)
        self.travle_layout.addWidget(self.travle_label2, 0, 2)
        self.travle_layout.addWidget(self.travle_btn2, 0, 3)
        self.travle_layout.addWidget(self.travle_label3, 1, 0)
        self.travle_layout.addWidget(self.travle_btn3, 1, 1)
        self.travle_layout.addWidget(self.travle_label4, 1, 2)
        self.travle_layout.addWidget(self.travle_btn4, 1, 3)
        self.travle_layout.addWidget(self.travle_label5, 2, 0)
        self.travle_layout.addWidget(self.travle_btn5, 2, 1)
        self.travle_layout.addWidget(self.travle_label6, 2, 2)
        self.travle_layout.addWidget(self.travle_btn6, 2, 3)

        self.travle_group.setLayout(self.travle_layout)

        self.layout = QGridLayout()
        self.layout.addWidget(self.travle_group, 0, 0)
        self.setLayout(self.layout)

    def onActivated1(self, text):
        self.travle_value1.setText(text)

    def asiana(self):  # 이벤트 핸들러 만들기(새창)
        self.Popups.append(AisanaUI())

    def ktx(self):
        self.Popups.append(KTXUI())

    def srt(self):
        self.Popups.append(SRTUI())

    def navermap(self):
        self.Popups.append(NaverMapUI())

    def naversubway(self):
        self.Popups.append(NaverSubWayUI())

    def txbus(self):
        self.Popups.append(TxBusUI())

class AisanaUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        header = {"User-Agent": "Mozilla/5.0"}

        driver1 = webdriver.Chrome()
        driver1.get('https://flyasiana.com/I/KR/KO/RevenueRegistTravel.do')

        driver1.find_element_by_xpath('/html/body/div[1]/div[4]/div[2]/div[1]/ul/li[2]/a').click()

        driver1.find_element_by_xpath('/html/body/div[1]/div[4]/div[3]/div[1]/input[5]').click()
        driver1.find_element_by_xpath('/html/body/div[1]/div[4]/div[3]/div[1]/input[5]').send_keys(input('출발지 입력 : '))
        driver1.find_element_by_xpath('/html/body/div[1]/div[4]/div[3]/div[1]/input[5]').send_keys(Keys.ENTER)

        driver1.find_element_by_xpath('/html/body/div[1]/div[4]/div[3]/div[2]/input[6]').click()
        driver1.find_element_by_xpath('/html/body/div[1]/div[4]/div[3]/div[2]/input[6]').send_keys(input('도착지 입력 : '))
        driver1.find_element_by_xpath('/html/body/div[1]/div[4]/div[3]/div[2]/input[6]').send_keys(Keys.ENTER)

class KTXUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        driver = webdriver.Chrome()
        url = 'http://www.letskorail.com/ebizprd/EbizPrdTicketpr21100W_pr21110.do'
        driver.get(url)

        driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/div[2]/form/div/div[2]/div/dl[2]/dd/input').click()
        driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/div[2]/form/div/div[2]/div/dl[2]/dd/input').send_keys(Keys.BACK_SPACE)
        driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/div[2]/form/div/div[2]/div/dl[2]/dd/input').send_keys(Keys.BACK_SPACE)
        driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/div[2]/form/div/div[2]/div/dl[2]/dd/input').send_keys(input('출발지를 입력하세요 : '))
        driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/div[2]/form/div/div[2]/div/dl[2]/dd/input').send_keys(Keys.ARROW_DOWN)
        driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/div[2]/form/div/div[2]/div/dl[2]/dd/input').send_keys(Keys.ENTER)

        driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/div[2]/form/div/div[2]/div/dl[3]/dd/input[1]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/div[2]/form/div/div[2]/div/dl[3]/dd/input[1]').send_keys(Keys.BACK_SPACE)
        driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/div[2]/form/div/div[2]/div/dl[3]/dd/input[1]').send_keys(Keys.BACK_SPACE)
        driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/div[2]/form/div/div[2]/div/dl[3]/dd/input[1]').send_keys(input('도착지를 입력하세요 : '))
        driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/div[2]/form/div/div[2]/div/dl[3]/dd/input[1]').send_keys(Keys.ARROW_DOWN)
        driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/div[2]/form/div/div[2]/div/dl[3]/dd/input[1]').send_keys(Keys.ENTER)
        time.sleep(1)

        driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/div[2]/form/div/div[2]/div/dl[4]/dd/a/img').click()
        input('원하시는 날짜를 선택 후 엔터를 눌러주세요')

        driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/div[2]/form/div/p/a/img').click()

class SRTUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        driver = webdriver.Chrome()
        url = 'https://etk.srail.co.kr/hpg/hra/01/selectScheduleList.do?pageId=TK0101010000'
        driver.get(url)

        driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div[2]/form/fieldset/div[1]/div/div/div[1]/input').click()
        driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div[2]/form/fieldset/div[1]/div/div/div[1]/input').send_keys(Keys.BACK_SPACE)
        driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div[2]/form/fieldset/div[1]/div/div/div[1]/input').send_keys(Keys.BACK_SPACE)
        driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div[2]/form/fieldset/div[1]/div/div/div[1]/input').send_keys(input('출발지를 입력하세요 : '))

        driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div[2]/form/fieldset/div[1]/div/div/div[2]/input').click()
        driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div[2]/form/fieldset/div[1]/div/div/div[2]/input').send_keys(Keys.BACK_SPACE)
        driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div[2]/form/fieldset/div[1]/div/div/div[2]/input').send_keys(Keys.BACK_SPACE)
        driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div[2]/form/fieldset/div[1]/div/div/div[2]/input').send_keys(input('도착지를 입력하세요 : '))

        driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div[2]/form/fieldset/div[1]/div/div/div[3]/a/img').click()
        input('원하시는 날짜를 선택 후 엔터를 눌러주세요')

        driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div[2]/form/fieldset/div[2]/input').click()

class NaverMapUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}

        driver = webdriver.Chrome()
        url = 'https://map.naver.com/v5/?c='
        driver.get(url)

        time.sleep(2)
        driver.find_element_by_xpath('/html/body/app/layout/div[2]/div[1]/navbar/perfect-scrollbar/div/div[1]/div/ul/li[3]/a').click()
        time.sleep(2)

        driver.find_element_by_xpath('/html/body/app/layout/div[2]/div[2]/div[1]/shrinkable-layout/directions-layout/directions-result/div/ul/li[2]/a').click()
        time.sleep(2)

        driver.find_element_by_xpath('/html/body/app/layout/div[2]/div[2]/div[1]/shrinkable-layout/directions-layout/directions-result/div[1]/directions-search/div[1]/directions-search-box[1]/div/div/div[1]/input').click()
        driver.find_element_by_xpath('/html/body/app/layout/div[2]/div[2]/div[1]/shrinkable-layout/directions-layout/directions-result/div[1]/directions-search/div[1]/directions-search-box[1]/div/div/div[1]/input').send_keys(input('출발지 입력 : '))
        driver.find_element_by_xpath('/html/body/app/layout/div[2]/div[2]/div[1]/shrinkable-layout/directions-layout/directions-result/div[1]/directions-search/div[1]/directions-search-box[1]/div/div/div[1]/input').send_keys(Keys.ENTER)
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/app/layout/div[2]/div[2]/div[1]/shrinkable-layout/directions-layout/directions-result/div[1]/directions-search/div[1]/directions-search-box[1]/div/div/div[1]/input').send_keys(Keys.ENTER)

        driver.find_element_by_xpath('/html/body/app/layout/div[2]/div[2]/div[1]/shrinkable-layout/directions-layout/directions-result/div[1]/directions-search/div[1]/directions-search-box[2]/div/div/div[1]/input').click()
        driver.find_element_by_xpath('/html/body/app/layout/div[2]/div[2]/div[1]/shrinkable-layout/directions-layout/directions-result/div[1]/directions-search/div[1]/directions-search-box[2]/div/div/div[1]/input').send_keys(input('도착지 입력 : '))
        driver.find_element_by_xpath('/html/body/app/layout/div[2]/div[2]/div[1]/shrinkable-layout/directions-layout/directions-result/div[1]/directions-search/div[1]/directions-search-box[2]/div/div/div[1]/input').send_keys(Keys.ENTER)
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/app/layout/div[2]/div[2]/div[1]/shrinkable-layout/directions-layout/directions-result/div[1]/directions-search/div[1]/directions-search-box[2]/div/div/div[1]/input').send_keys(Keys.ENTER)
        time.sleep(2)

        driver.find_element_by_xpath('/html/body/app/layout/div[2]/div[2]/div[1]/shrinkable-layout/directions-layout/directions-result/div/directions-search/div[2]/button[2]').click()

class NaverSubWayUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}

        driver = webdriver.Chrome()
        url = 'https://map.naver.com/v5/?c='
        driver.get(url)

        time.sleep(2)
        driver.find_element_by_xpath('/html/body/app/layout/div[2]/div[1]/navbar/perfect-scrollbar/div/div[1]/div/ul/li[5]/a').click()
        time.sleep(2)

        driver.find_element_by_xpath('/html/body/app/layout/div[2]/div[2]/div[1]/shrinkable-layout/subway-layout/subway-home-layout/subway-control-panel/div/subway-input-control/div[1]/ul/li[1]/subway-input-control-item/div/div/div[1]/input').click()
        driver.find_element_by_xpath('/html/body/app/layout/div[2]/div[2]/div[1]/shrinkable-layout/subway-layout/subway-home-layout/subway-control-panel/div/subway-input-control/div[1]/ul/li[1]/subway-input-control-item/div/div/div[1]/input').send_keys(input('출발지 입력 : '))
        driver.find_element_by_xpath('/html/body/app/layout/div[2]/div[2]/div[1]/shrinkable-layout/subway-layout/subway-home-layout/subway-control-panel/div/subway-input-control/div[1]/ul/li[1]/subway-input-control-item/div/div/div[1]/input').send_keys(Keys.ENTER)
        time.sleep(2)

        driver.find_element_by_xpath('/html/body/app/layout/div[2]/div[2]/div[1]/shrinkable-layout/subway-layout/subway-home-layout/subway-control-panel/div/subway-input-control/div[1]/ul/li[2]/subway-input-control-item/div/div/div[1]/input').click()
        driver.find_element_by_xpath('/html/body/app/layout/div[2]/div[2]/div[1]/shrinkable-layout/subway-layout/subway-home-layout/subway-control-panel/div/subway-input-control/div[1]/ul/li[2]/subway-input-control-item/div/div/div[1]/input').send_keys(input('도착지 입력 : '))
        driver.find_element_by_xpath('/html/body/app/layout/div[2]/div[2]/div[1]/shrinkable-layout/subway-layout/subway-home-layout/subway-control-panel/div/subway-input-control/div[1]/ul/li[2]/subway-input-control-item/div/div/div[1]/input').send_keys(Keys.ENTER)

class TxBusUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        custom_header = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
        }

        driver = webdriver.Chrome()
        url = 'https://txbus.t-money.co.kr/otck/trmlInfEnty.do'
        driver.get(url)

        driver.find_element_by_xpath('/html/body/div[2]/article/section/div[2]/div/div[3]/div/div[2]/form/div/dl[1]/dd/div/label/input').click()
        driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[1]/div/dl[2]/dd/div/input').send_keys(input('출발지를 입력하세요 : '))
        driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[1]/div/dl[2]/dd/div/a').send_keys(Keys.ENTER)
        input('원하는 터미널을 골라주세요.(고른 후 엔터)')

        driver.find_element_by_xpath('/html/body/div[2]/article/section/div[2]/div/div[3]/div/div[2]/form/div/dl[2]/dd/div/label/input').click()
        driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[1]/div/dl[2]/dd/div/input').send_keys(input('도착지를 입력하세요 : '))
        driver.find_element_by_xpath('/html/body/div[2]/article/section/div[2]/div/div[3]/div/div[2]/form/div/dl[2]/dd/div/a').send_keys(Keys.ENTER)
        input('원하는 터미널을 골라주세요.(고른 후 엔터)')

        driver.find_element_by_xpath('/html/body/div[2]/article/section/div[2]/div/div[3]/div/div[2]/form/div/p[2]/a').click()
        time.sleep(2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainUI()
    ex.show()
    sys.exit(app.exec_())
