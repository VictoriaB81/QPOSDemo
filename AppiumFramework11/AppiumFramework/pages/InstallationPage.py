from AppiumFramework.base.BasePage import BasePage
import AppiumFramework.utilities.customLogger as cl

class AppLaunchPermission(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators values in app launch permission page
    _allowBtn1 = "com.android.packageinstaller:id/permission_allow_button"
    _allowBtn2 = "com.android.packageinstaller:id/permission_allow_button"

    _cloudMode = "com.quinta.qpos:id/imageView6"
    _SelectServer = "com.quinta.qpos:id/spinnerUrls"
    _SelectTestServer = "//android.widget.TextView[@text='Test Server']"
    _TestServerSubmit = "com.quinta.qpos:id/buttonSubmit"

    _LicenseKey = "com.quinta.qpos:id/editTextLicenseKey"
    _LicenseSubmitBtn = "com.quinta.qpos:id/buttonSubmit"

    def clickAllowBtn1(self):
        self.clickElement(self._allowBtn1, "id")
        cl.allureLogs("Clicked on allow button 1")

    def clickAllowBtn2(self):
        self.clickElement(self._allowBtn2, "id")
        cl.allureLogs("Clicked on allow button 1")

    def enterLicenseKey(self):
        self.sendText("KXJJETT3", self._LicenseKey, "id")
        cl.allureLogs("Entered License Key")

    def LicenseSubmitBtn(self):
        self.clickElement(self._LicenseSubmitBtn, "id")
        cl.allureLogs("Submitted License Key")

    def clickCloudMode(self):
        self.clickElement(self._cloudMode, "id")
        cl.allureLogs("Clicked on cloud mode")

    def selectServer(self):
        self.clickElement(self._SelectServer, "id")
        cl.allureLogs("Click on select server to select a server")

    def selectTestServer(self):
        self.clickElement(self._SelectTestServer, "xpath")
        cl.allureLogs("Selected Test Server option")

    def testServerSubmit(self):
        self.clickElement(self._TestServerSubmit, "id")
        cl.allureLogs("Clicked on Test server submit button")

