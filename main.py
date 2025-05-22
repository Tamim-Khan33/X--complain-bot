from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from dotenv import load_dotenv


chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)
load_dotenv()



PROMISED_DOWN=150
PROMISED_UP=10
YOUR_EMAIL = os.getenv("YOUR_EMAIL")
YOUR_PASSWORD = os.getenv("YOUR_PASSWORD")

# insert_email=driver.find_element(By.XPATH,value='//*[@id="loginForm"]/div[1]/div[1]/div/label/input')
# insert_password=driver.find_element(By.XPATH,value='//*[@id="loginForm"]/div[1]/div[2]/div/label/input')
# button=driver.find_element(By.XPATH,value='//*[@id="loginForm"]/div[1]/div[3]')
# insert_email.send_keys("dummy0172255@gmail.com")
# insert_password.send_keys("wxl2476o@@")
# button.click()
# time.sleep(10)




def check_speed():
    driver.get("https://www.speedtest.net/")
    time.sleep(3)
    click_go=driver.find_element(By.XPATH,value="//span[text()='Go']")
    click_go.click()

    time.sleep(60)

    dd = driver.find_elements(By.CLASS_NAME, value="result-data-value")
    speed = [value.text for value in dd][:3]
    download_speed_value = speed[0]
    upload_speed_speed_value = speed[1]

    return f"download_speed_value:{download_speed_value}\nupload_speed_value:{upload_speed_speed_value}"

message=check_speed()

def send_twit():
    time.sleep(3)
    driver.get("https://x.com/home")
    time.sleep(4)
    insert_email=driver.find_element(By.XPATH,value="//input[@name='text' and @type='text' and @autocomplete='username']")
    insert_email.send_keys(YOUR_EMAIL)
    next_button=driver.find_element(By.XPATH,value="//span[text()='Next']")
    next_button.click()
    time.sleep(5)
    user_name=driver.find_element(By.XPATH,value="//input[@data-testid='ocfEnterTextTextInput']")
    user_name.send_keys("dummy0172255",Keys.ENTER)
    time.sleep(5)
    insert_password=driver.find_element(By.XPATH,value="//input[@type='password' and @autocomplete='current-password']")
    insert_password.send_keys(YOUR_PASSWORD)
    login=driver.find_element(By.XPATH,value="//span[text()='Log in']")
    login.click()
    time.sleep(3)
    post=driver.find_element(By.XPATH,value="//a[@aria-label='Post' and @href='/compose/post']")
    post.click()
    time.sleep(2)
    text = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//div[@data-testid='tweetTextarea_0']"))
    )
    time.sleep(3)
    text.send_keys(f"{message}")
    post2=driver.find_element(By.XPATH,value="//span[text()='Post']")
    post2.click()



send_twit()
