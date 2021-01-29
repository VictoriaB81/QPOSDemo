import unittest
import pytest

from AppiumFramework.pages.InstallationPage import AppLaunchPermission
import AppiumFramework.utilities.customLogger as cl


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class InstallationTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.cf = AppLaunchPermission(self.driver)


    @pytest.mark.run(order=1)
    def test_allowPermission(self):
        cl.allureLogs("App Launched")
        self.cf.clickAllowBtn1()
        self.cf.clickAllowBtn2()

    @pytest.mark.run(order=2)
    def test_enterLicenseDetails(self):
        # cl.allureLogs("App Launched")
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



