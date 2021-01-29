from AppiumFramework.base.BasePage import BasePage
import AppiumFramework.utilities.customLogger as cl


class POSHomePageTest(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators values in login page
    _POS = "com.quinta.qpos:id/imageView6"



    def clickOnPOS(self):
        self.clickElement(self._POS, "id")
        cl.allureLogs("Clicked on POS")


