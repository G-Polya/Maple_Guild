import sys
from selenium import webdriver
from PyQt5.QtWidgets import *


def Get_GuildIndex(guilds, server):
    for i in range(len(guilds)):
        server_container = guilds[i].find_element_by_css_selector("div.search-result__item")
        server_text = server_container.find_element_by_css_selector("b.font-size-14").text

        if server_text == server:
            return i


class MyApp(QWidget):
    number = 0
    def __init__(self):
        super().__init__()
        self.initUI()

    levels = []
    members = []
    dojangs = []
    jobs = []
    numberOfMembers = 0

    def Maple_Spec(guild_name, server):

        driver = webdriver.Chrome("chromedriver")
        driver.get("https://maple.gg/")
        search_box = driver.find_element_by_name("q")
        search_box.send_keys(guild_name)
        search_button = driver.find_element_by_css_selector("i.fa-search")
        search_button.click()

        driver.implicitly_wait(5)
        guilds = driver.find_elements_by_css_selector("div.col-12")

        index = Get_GuildIndex(guilds, server)
        guilds[index].click()
        driver.implicitly_wait(5)
        MyApp.numberOfMember = int(driver.find_elements_by_css_selector("div.col-lg-25 span")[3].text[-4:-1])
        guild_member = driver.find_elements_by_css_selector("div.col-lg-3")

        for i in range(MyApp.numberOfMember):
            try:
                guild_member_name = guild_member[i].find_element_by_css_selector("div.mb-2 a.font-size-14")
                guild_member_info = guild_member[i].find_element_by_css_selector(
                    "div.mb-2 span.font-size-12").text.split(
                    "/")

                MyApp.members.append(guild_member_name.text)

                guild_member_job = guild_member_info[0]
                guild_member_level = guild_member_info[1]
                MyApp.levels.append(int(guild_member_level[-3:]))
                MyApp.jobs.append(guild_member_job[:10])
                # print(guild_member_job, guild_member_level)
                # return MyApp.levels, MyApp.jobs
            except IndexError:
                break

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(QLabel("Guild Name"),0,0)
        grid.addWidget(QLabel("Server"),1,0)
        grid.addWidget(QLabel("Print"),2,0)

        self.le1 = QLineEdit()
        grid.addWidget(self.le1,0,1)
        self.le2 = QLineEdit()
        grid.addWidget(self.le2,1,1)

        self.le2.returnPressed.connect(self.append_text)



        self.tb = QTextBrowser()
        self.tb.setAcceptRichText(True)
        self.tb.setOpenExternalLinks(True)

        grid.addWidget(self.tb,2,1)

        self.setWindowTitle('QTextBrowser')
        self.setGeometry(500, 500, 500, 500)
        self.show()

    def append_text(self):
        self.Maple_Spec(self.le1.text(),self.le2.text())

        #for i in range(MyApp.numberOfMembers):

        # self.tb.append()
        self.le1.clear()
        self.le2.clear()

    def clear_text(self):
        self.tb.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

# http://codetorial.net/pyqt5/widget/qtextbrowser.html