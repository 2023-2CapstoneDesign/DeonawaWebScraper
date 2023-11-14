#This prototype is made for Chrome only.
#Using Selenium 4 -- chromedriver executable is not needed.
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager 
from PIL import Image
import io

#Initialise Options: Don't auto-quit browser, Maximise browser.
options = Options()
options.add_experimental_option("detach", True)
options.add_argument("--start-maximized")

#Create Driver instance + pass service & options, set implicit wait time.
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.implicitly_wait(5)

#get 위메프
driver.get("https://front.wemakeprice.com/main")

#위메프 스크린샷 스크래퍼
def get_wemake_screenshot(product_name):
    #검색버튼 찾기, 상품명 입력, 검색
    search_bar = driver.find_element(By.XPATH, '//*[@id="_searchKeyword"]')
    search_btn = driver.find_element(By.XPATH, '//*[@id="_searchKeywordBtn"]')
    search_bar.send_keys(product_name)
    search_btn.click()
    #첫 상품 링크 클릭
    try:
        driver.find_element(By.CLASS_NAME, 'list_conts_wrap').click()
    except NoSuchElementException:
        return
    driver.switch_to.window(driver.window_handles[-1])
    #쿠폰버튼 클릭
    try:
        driver.find_element(By.XPATH, '//*[@id="_infoAreaCoupon"]/a').click()
    except NoSuchElementException:
        pass
    #스크린샷
    screenshot_area = driver.find_element(By.XPATH, '//*[@id="_contents"]/div[3]/div[1]')
    driver.execute_script("arguments[0].scrollIntoView();", screenshot_area)
    screenshot = screenshot_area.screenshot_as_png
    img = Image.open(io.BytesIO(screenshot))
    img.save(f"./Screenshots/{product_name}.png")
    #홈페이지로 복귀
    driver.switch_to.window(driver.window_handles[0])
    driver.back()
    driver.refresh()
 

#상품명 입력 function
def input_product_name():
    while True:
        product_name = input("상품명을 입력하세요 (끝내려면 quit 입력): ")
        if product_name == "quit":
            break
        else:
            get_wemake_screenshot(product_name)

#Testing
input_product_name()



""" 쿠팡 크롤러
#Open 쿠팡 in chrome
driver.get("https://www.coupang.com/")

#쿠팡 검색창
search_bar = driver.find_element(By.ID, 'headerSearchKeyword')
search_btn = driver.find_element(By.ID, 'headerSearchBtn')

#검색어 입력받고 제품 상세페이지 스크린샷 하는 function
def get_cupang_screenshot():
    #상품명 입력받기
    product_name = input("상품명을 입력하세요: ")
    #쿠팡 검색창 입력 및 검색
    search_bar.send_keys(product_name)
    search_btn.click() #ERROR: 페이지 접속 오류 뜸
    #검색결과 첫 제품 클릭
    #제품상세페이지 상품가격정보 스크린샷
"""