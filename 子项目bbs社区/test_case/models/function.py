from selenium import  webdriver
import time
import os


# 截图函数
def inser_img(driver, file_name):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\','/')
    base = base_dir.split('/test_case')[0]
    file_path = base + '/report/image/' + file_name # 注意完整目录需要/结尾
    driver.get_screenshot_as_file(file_path)

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com')
    inser_img(driver, 'baidu.png')
    driver.quit()