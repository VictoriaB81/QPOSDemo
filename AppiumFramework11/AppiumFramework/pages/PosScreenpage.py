from AppiumFramework.base.BasePage import BasePage
import AppiumFramework.utilities.customLogger as cl


class PosScreenPgTest(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators values in login page
    _item1 = "//android.widget.TextView[@text='A2 Cow Ghee 500ml1']"
    _item2 = "//android.widget.TextView[@text='Almonds Premium 250g']"
    _totalAmount = "com.quinta.qpos:id/textViewTotalAmount"

    def clickOnitem1(self):
        self.clickElement(self._item1, "xpath")
        cl.allureLogs("Clicked on item1")

    def clickOnitem2(self):
        self.clickElement(self._item2, "xpath")
        cl.allureLogs("Clicked on item2")

    def clickOnTotalAmount(self):
        self.clickElement(self._totalAmount, "id")
        cl.allureLogs("Clicked on totalAmount")


