from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import pandas as pd

class MapleGuild:
    guild_name = "Alpha"
    server = "크로아"

    def __init__(self):

        levels = []
        members = []
        dojangs = []
        jobs = []

    def StartCrawiling(self):
        driver = webdriver.Chrome("chromedriver")
        driver.get("https://maple.gg/")
        search_box = driver.find_element_by_name("q")
        search_box.send_keys(self.guild_name)
        search_button = driver.find_element_by_css_selector("i.fa-search")
        search_button.click()

        guilds = driver.find_elements_by_css_selector("div.col-12")

        driver.implicitly_wait(10)

        finded_server = guilds[0].find_element_by_css_selector("div.search-result__item")
        guild_server = finded_server.find_element_by_css_selector("b.font-size-14").text

        if guild_server == self.server:
            guild_button = driver.find_element_by_css_selector("div.col-12")
            guild_button.click()

            driver.implicitly_wait(5)
            numberOfMember = driver.find_elements_by_css_selector("div.col-lg-25 span")
            numberOfMember = int(numberOfMember[3].text[-4:-1])

            # 길드원 container col-lg-3 col-md-6 col-sm-6 mt-4
            guild_member = driver.find_elements_by_css_selector("div.col-lg-3")

            for i in range(numberOfMember):
                try:
                    guild_member_name = guild_member[i].find_element_by_css_selector("div.mb-2 a.font-size-14")
                    guild_member_info = guild_member[i].find_element_by_css_selector("div.mb-2 span.font-size-12").text.split("/")

                    self.members.append(guild_member_name.text)

                    guild_member_job = guild_member_info[0]
                    guild_member_level = guild_member_info[1]
                    self.levels.append(int(guild_member_level[-3:]))
                    self.jobs.append(guild_member_job[:10])
                    print(guild_member_job, guild_member_level)
                except IndexError:
                    break

        for i in range(len(self.members)):
            try:
                search_box = driver.find_element_by_name("q")

                search_box.send_keys(self.members[i])

                search_button = driver.find_element_by_css_selector("i.fa-search")
                search_button.click()
                driver.implicitly_wait(1)

                member_button = driver.find_elements_by_css_selector("div.search-result__item")[0]
                member_button.click()

                dojang = int(driver.find_elements_by_css_selector("h1.user-summary-floor")[0].text[-4:-2])
                self.dojangs.append(dojang)

            # 검색시 바로 캐릭터로 이동하는 경우
            except IndexError:
                try:
                    dojang = int(driver.find_elements_by_css_selector("h1.user-summary-floor")[0].text[-4:-2])
                    self.dojangs.append(dojang)

                # 무릉이 없는데 예전 무릉기록은 있음
                except IndexError:
                    try:
                        dojang = int(driver.find_element_by_css_selector("div.old-dojang").text[-3:-1])
                        self.dojangs.append(dojang)

                    # 무릉자체가 없음
                    except NoSuchElementException:
                        dojang = 0
                        self.dojangs.append(dojang)

            except NoSuchElementException:
                dojang = 0
                self.dojangs.append(dojang)


    def GetLevels(self):
        return self.levels

    def GetMembers(self):
        return self.members

    def GetDojang(self):
        return self.dojangs

    def GetJobs(self):
        return self.jobs

    def GetGuildName(self):
        return self.guild_name



guild = MapleGuild()

guild.StartCrawiling()

df = pd.DataFrame({
    "member":guild.GetMembers(),
    "level":guild.GetLevels(),
    "job":guild.GetJobs(),
    "dojang" : guild.GetDojang()

})

df.to_excel(guild.guild_name+"_pycharm.xlsx")




