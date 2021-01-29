import time

from AppiumFramework.base.BasePage import BasePage
import AppiumFramework.utilities.customLogger as cl


class LoginPageTest(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators values in login page
    _username = "com.quinta.qpos:id/editTextUserName"
    _password = "com.quinta.qpos:id/editTextPassword"
    _submitLoginBtn = "com.quinta.qpos:id/buttonLogin"
    _wrongCredentials = "Wrong Credentials"
    _initialCashTitle = "A new shift is starting."
    _cancelInitialCash = "android:id/button2"

    _launchOK = "android:id/button1" #id

    # _loginbutton = "com.code2lead.kwad:id/Login"  # id
    # _enterEmail = "3"  # index
    # _enterPassword = "Enter Password"  # text
    # _clickloginButton = "com.code2lead.kwad:id/Btn3"  # id
    # _wrongCredentials = "Wrong Credentials"  # text
    # _pageTitle = "Enter Admin"  # text
    # _enterText = "com.code2lead.kwad:id/Edt_admin"  # id
    # _submitButton = "SUBMIT"  # text

    def enterUsername(self):
        self.sendText("admin90", self._username, "id")
        cl.allureLogs("Entered username")

    def enterPassword(self):
        self.sendText("1234", self._password, "id")
        cl.allureLogs("Entered password")

    def enterPassword2(self):
        self.sendText("admin12344", self._password, "id")
        cl.allureLogs("Entered Invalid Password")

    def clickLoginSubmitBtn(self):
        self.clickElement(self._submitLoginBtn, "id")
        cl.allureLogs("Click on Login Button")

    def verifyLoginScreen(self):
        loginScreen = self.isDisplayed(self._username, "id")
        assert loginScreen == True
        cl.allureLogs("Opened login Screen")

    def verifyInitialcashTitle(self):
        initialpageScreen = self.isDisplayed(self._initialCashTitle, "text")
        assert initialpageScreen == True
        cl.allureLogs("Opened Initial Cash Page")

    def clickInitialCashBtn(self):
        self.clickElement(self._cancelInitialCash, "id")
        cl.allureLogs("Click on cancel initial cash Button")

    def enterAuditUsername(self):
        self.sendText("audit96a", self._username, "id")
        cl.allureLogs("Entered audit username")

    def enterAuditPassword(self):
        self.sendText("1234", self._password, "id")
        cl.allureLogs("Entered audit user password")

    def launchOK(self):
        self.clickElement(self._launchOK, "id")
        time.sleep(1)
        cl.allureLogs("once app launch click on OK to continue with the users shift")