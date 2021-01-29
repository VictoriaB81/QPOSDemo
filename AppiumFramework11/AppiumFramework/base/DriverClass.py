from appium import webdriver


class Driver:
    def getDriverMethod(self):
        des_caps = {'platformName': 'Android', 'platformVersion': '7', 'deviceName': '0123456789ABCDEF',
                    'app': 'C:/Users/Victoria Baretto/Downloads/QPosV119.apk', 'appPackage': 'com.quinta.qpos',
                    'appActivity': 'com.quinta.qpos.activity.LoginPageActivity', 'noReset':'true', 'fullReset':'false'}
        # des_caps['deviceName'] = '0123456789ABCDEF'  # WT device
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", des_caps)
        return driver
