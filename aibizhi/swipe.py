
from appium import webdriver

def swipeUp(driver, t=500, n=1):
    size = driver.get_window_size()
    x1 = size['width'] * 0.5  # x坐标
    y1 = size['height'] * 0.75  # 起始y坐标
    y2 = size['height'] * 0.25  # 终点y坐标
    for i in range(n):
        driver.swipe(x1, y1, x1, y2, t)

def swipeDown(driver, t=500, n=1):
    size = driver.get_window_size()
    x1 = size['width'] * 0.5  # x坐标
    y1 = size['height'] * 0.25  # 起始y坐标
    y2 = size['height'] * 0.75  # 终点y坐标
    for i in range(n):
        driver.swipe(x1, y1, x1, y2, t)

def swipLeft(driver, t=500, n=1):
    size = driver.get_window_size()  # {'width': 720, 'height': 1280}
    x1 = size['width'] * 0.75
    y1 = size['height'] * 0.5
    x2 = size['width'] * 0.05
    for i in range(n):
        driver.swipe(x1, y1, x2, y1, t)

def swipRight(driver, t=500, n=1):
    size = driver.get_window_size()
    x1 = size['width'] * 0.05
    y1 = size['height'] * 0.5
    x2 = size['width'] * 0.75
    for i in range(n):
        driver.swipe(x1, y1, x2, y1, t)