from AppiumFramework.base.BasePage import BasePage
import AppiumFramework.utilities.customLogger as cl


class InitialCashTest(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators values in login page
    # _titleNewShiftStarting = "com.quinta.qpos:id/editTextUserName"
    _enterInitialCash = "com.quinta.qpos:id/editText"
    _submitInitialCashBtn = "android:id/button1"

    def enterInitialCash(self):
        self.sendText("100", self._enterInitialCash, "id")
        cl.allureLogs("Entered initial cash")

    def clickICSubmitBtn(self):
        self.clickElement(self._submitInitialCashBtn, "id")
        cl.allureLogs("Click on Initial cash submit Button")


    # def verifyLoginScreen(self):
    #     loginScreen = self.isDisplayed(self._username, "id")
    #     assert loginScreen == True
    #     cl.allureLogs("Opened login Screen")
