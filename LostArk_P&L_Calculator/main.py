from selenium import webdriver
import time
def gwangdae():
    lifeBtn = driver.find_element_by_xpath(
        "/html/body/div[2]/div/main/div/div[2]/div[2]/form/fieldset/div/div[1]/input").send_keys("광대버섯")
    time.sleep(1)
    searchBtn = driver.find_element_by_xpath('/html/body/div[2]/div/main/div/div[2]/div[2]/form/fieldset/div/div[4]/button[1]')
    searchBtn.click()

    time.sleep(2)
    table = driver.find_element_by_xpath('/html/body/div[2]/div/main/div/div[2]/div[2]/div/div/div[1]/table')
    # table = driver.find_element_by_class_name('itemList')
    tbody = table.find_element_by_tag_name("tbody")
    rows = tbody.find_elements_by_tag_name("tr")
    for row in enumerate(rows):
        index, value = row
        body = value.find_elements_by_tag_name("td")[0]
        cost = value.find_elements_by_tag_name("td")[3]
        if body.text.split('\n')[0] == '광대버섯':
        # if body.text == '광대버섯\n[10개 단위 판매]':
            print(index, body.text, cost.text)
        # print(index, body.text, cost.text)
        # body = value.find_elements_by_tag_name("td")[0]
        # print(body.text)


chromedriver = '.\chromedriver\chromedriver.exe'
driver = webdriver.Chrome(chromedriver)

driver.get('https://lostark.game.onstove.com/Market')

print("+" * 100)
print(driver.title)
print(driver.current_url)
print("로아 거래소")
print("-" * 100)

gwangdae()
# lifeBtn.click()

# <input type="text" id="txtItemName" class="input input--deal-name" placeholder="아이템 명을 입력해주세요." maxlength="20" value="">
# /html/body/div[2]/div/main/div/div[2]/div[2]/form/fieldset/div/div[1]/input

# 광대버섯 타이핑 - 검색 버튼 클릭 - 최근 거래가 확인, 최저가