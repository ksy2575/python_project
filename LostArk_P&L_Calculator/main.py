from selenium import webdriver

# selenium에서 사용할 웹 드라이버 절대 경로 정보
chromedriver = '.\chromedriver\chromedriver.exe'
# selenum의 webdriver에 앞서 설치한 chromedirver를 연동한다.
driver = webdriver.Chrome(chromedriver)
# driver로 특정 페이지를 크롤링한다.
driver.get('https://lostark.game.onstove.com/Market')
def calculation():

driver.find_element_by_xpath('/html/body/div[2]/div/main/div/div[2]/div[2]/form/fieldset/div/div[1]/input').send_keys('asdfasdf')
results = driver.find_elements_
print("+" * 100)
print(driver.title)   # 크롤링한 페이지의 title 정보
print(driver.current_url)  # 현재 크롤링된 페이지의 url
print("바이크 브랜드 크롤링")
print("-" * 100)

<em data-grade="0">1</em>