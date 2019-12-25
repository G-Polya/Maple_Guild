from selenium import webdriver

guild_name = "Alpha"
server = "크로아"
level = []
member = []

driver = webdriver.Chrome("chromedriver")
driver.get("https://maple.gg/")

search_box = driver.find_element_by_name("q")

search_button = driver.find_element_by_css_selector("i.fa-search")
search_button.click()

guilds = driver.find_elements_by_css_selector("div.col-12")

# 이 부분 일반적이게 변경
driver.implicitly_wait(10)
finded_server = guilds[0].find_element_by_css_selector("div.search-result__item")   # 서버 검색부분. Alpha길드는 크로아에도 있고 유니온에도 있음.
guild_server = finded_server.find_element_by_css_selector("b.font-size-14").text

if guild_server == server:    #
    guild_button = driver.find_element_by_css_selector("div.col-12")
    guild_button.click()
    driver.implicitly_wait(5)
    # 길드원 container col-lg-3 col-md-6 col-sm-6 mt-4
    guild_member = driver.find_elements_by_css_selector("div.col-lg-3")
    # 이부분 길드원 전체에 대해서 변경
    guild_member_name = guild_member[0].find_element_by_css_selector("div.mb-2 a.font-size-14")
    print(guild_member_name.text)

