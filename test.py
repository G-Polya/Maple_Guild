from selenium import webdriver

def Get_GuildIndex(guilds,server):
    for i in range(len(guilds)):
        server_container = guilds[i].find_element_by_css_selector("div.search-result__item")
        server_text = server_container.find_element_by_css_selector("b.font-size-14").text

        if server_text == server:
            return i

def Maple_Spec(guild_name,server):
    levels = []
    members = []
    dojangs = []
    jobs = []

    driver = webdriver.Chrome("chromedriver")
    driver.get("https://maple.gg/")
    search_box = driver.find_element_by_name("q")
    search_box.send_keys(guild_name)
    search_button = driver.find_element_by_css_selector("i.fa-search")
    search_button.click()

    driver.implicitly_wait(5)
    guilds = driver.find_elements_by_css_selector("div.col-12")

    index = Get_GuildIndex(guilds,server)
    guilds[index].click()
    driver.implicitly_wait(5)
    numberOfMember = int(driver.find_elements_by_css_selector("div.col-lg-25 span")[3].text[-4:-1])
    guild_member = driver.find_elements_by_css_selector("div.col-lg-3")

    for i in range(numberOfMember):
        try:
            guild_member_name = guild_member[i].find_element_by_css_selector("div.mb-2 a.font-size-14")
            guild_member_info = guild_member[i].find_element_by_css_selector("div.mb-2 span.font-size-12").text.split(
                "/")

            members.append(guild_member_name.text)

            guild_member_job = guild_member_info[0]
            guild_member_level = guild_member_info[1]
            levels.append(int(guild_member_level[-3:]))
            jobs.append(guild_member_job[:10])
            # print(guild_member_job, guild_member_level)
            return levels,jobs
        except IndexError:
            break


