import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime

#创建chrome driver
driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 15)

#访问repo的连接
driver.get('https://github.com/login')

#显示等待用户名输入框元素
username_field = wait.until(
    EC.presence_of_element_located((By.ID, "login_field"))
)
username_field.clear()
#输入用户名
username_field.send_keys("18611821761@163.com")

#显示等待密码输入框元素
password_field = wait.until(
    EC.presence_of_element_located((By.ID, "password"))
)
password_field.clear()
#输入密码
password_field.send_keys("Wang18611021761")

#显示等待登录按钮元素
sign_in_button = wait.until(
    EC.element_to_be_clickable((By.NAME, "commit"))
)
#点击登录按钮
sign_in_button.click()

user_login_success_icon = wait.until(
    EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Open user navigation menu']"))
)
