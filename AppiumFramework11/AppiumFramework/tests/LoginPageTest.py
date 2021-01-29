import unittest
import pytest

from AppiumFramework.base.BasePage import BasePage
from AppiumFramework.pages.InstallationPage import AppLaunchPermission
from AppiumFramework.pages.LoginPage import LoginPageTest
import AppiumFramework.utilities.customLogger as cl


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.gt = LoginPageTest(self.driver)
        self.bp = BasePage(self.driver)
        self.cf = AppLaunchPermission(self.driver)

    @pytest.mark.run(order=2)
    def test_loginInvalidPassword(self):
        # cl.allureLogs("App Opened")
        self.bp.keyCode(4)
        self.gt.verifyLoginScreen()
        self.gt.enterUsername()
        self.gt.enterPassword2()
        self.gt.clickLoginSubmitBtn()
        self.gt.verifyInitialcashTitle()

    @pytest.mark.run(order=1)
    def test_LoginValid(self):
        cl.allureLogs("App Opened")
        self.cf.clickAllowBtn1()
        self.cf.clickAllowBtn2()
        try:
            self.cf.clickCloudMode()
            self.cf.selectServer()
            self.cf.selectTestServer()
            self.cf.testServerSubmit()
        except Exception as e:
            print(e)
        self.cf.enterLicenseKey()
        self.driver.hide_keyboard()
        self.cf.LicenseSubmitBtn()
        self.gt.verifyLoginScreen()
        self.gt.enterUsername()
        self.gt.enterPassword()
        self.gt.clickLoginSubmitBtn()
        self.gt.verifyInitialcashTitle()
        self.driver.hide_keyboard()
        self.gt.clickInitialCashBtn()
