# _*_ coding : utf-8 _*_

#import selenium    # 用于获取网页elements
from selenium import webdriver  # 用于获取网页elements
import time         # 用于设定等待加载的时间
#import webbrowser  # 用于油猴方案

# 登录网址（村里宿舍应该都是这个）
schoolWebURL = 'http://124.16.81.61/srun_portal_success?ac_id=1&theme=pro'
#schoolWebURL = 'http://124.16.81.61'

# 用户信息（修改为你的帐号&密码）
username = 'xxxxxxxxxxxx'   # 登录邮箱
password = 'xxxxxxxxxxxx'   # 登录密码

# 打开登录页面
driver = webdriver.Chrome()
driver.get(schoolWebURL)
time.sleep(3)
#driver.refresh()
#time.sleep(3)

#while(True):
# 判断：页面是“尚未登录”还是“已经登录”
if driver.find_elements("id", "login-account"):
    ele = driver.find_element("id", "login-account")
    if ele.is_enabled():
        print("状态：尚未登录……")
        #webbrowser.open(schoolWebURL)   # 替代方式：使用Chrome打开登录页面（自动运行油猴脚本）
        ele_username = driver.find_element("id","username")
        ele_username.send_keys(username)
        ele_password = driver.find_element("id","password")
        ele_password.send_keys(password)
        ele.click()
        time.sleep(3)
        print("状态：已登录！")
elif driver.find_elements("id", "logout"):
    ele = driver.find_element("id", "logout")
    if ele.is_enabled():
        print("状态：已登录。")
else:
    print("超时！登录/登出页面加载失败！")

driver.quit()



