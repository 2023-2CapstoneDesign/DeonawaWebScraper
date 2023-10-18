#This prototype is made for Chrome only.
#Using the newest version of Selenium -- chromedriver executable is not needed.
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

#General Screenshot Function -- 테스트용
def getscreenshot(url):
    #initialise options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--start-maximized")

    #initialise driver
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    time.sleep(2)

    element = driver.find_element(By.CSS_SELECTOR, 'body')
    width = 1920
    height = 1080
    driver.set_window_size(width, height)
    time.sleep(2)
    driver.save_screenshot("screenshot.png")
    driver.quit()

#Testing
getscreenshot("https://dashingdon.com/play/respawntheory/sdip-private/mygame/")



#무신사 제품목록페이지 상품가격정보: <div class="article_info">
#무신사 제품상세페이지 상품가격정보: <div class="right_contents section_product_summary">
#쿠팡 제품목록페이지 상품가격정보: <dd class="descriptions">
#쿠팡 제품상세페이지 상품가격정보: <div class="prod-atf-main">

#To Do: Dynamic Dimensions, Dynamic Screenshot Name, PNG Filing System