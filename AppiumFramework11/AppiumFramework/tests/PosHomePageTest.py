import unittest
import pytest

from AppiumFramework.base.BasePage import BasePage
from AppiumFramework.pages.InitilaCashPage import InitialCashTest
from AppiumFramework.pages.InstallationPage import AppLaunchPermission
from AppiumFramework.pages.LoginPage import LoginPageTest
import AppiumFramework.utilities.customLogger as cl
from AppiumFramework.pages.PosHomePage import POSHomePageTest


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class POSHomeTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.gt = LoginPageTest(self.driver)
        self.bp = BasePage(self.driver)
        self.cf = AppLaunchPermission(self.driver)
        self.ip = InitialCashTest(self.driver)
        self.ph = POSHomePageTest(self.driver)

    @pytest.mark.run(order=5)
    def test_HomePage(self):
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
        self.ip.enterInitialCash()
        self.ip.clickICSubmitBtn()
        self.ph.clickOnPOS()
