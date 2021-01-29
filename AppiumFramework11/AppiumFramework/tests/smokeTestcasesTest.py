import time
import unittest
import pytest

from AppiumFramework.base.BasePage import BasePage
from AppiumFramework.pages.InitilaCashPage import InitialCashTest
from AppiumFramework.pages.InstallationPage import AppLaunchPermission
from AppiumFramework.pages.LoginPage import LoginPageTest
import AppiumFramework.utilities.customLogger as cl
from AppiumFramework.pages.PosBillPage import PosBillPgTest
from AppiumFramework.pages.PosHomePage import POSHomePageTest
from AppiumFramework.pages.PosScreenpage import PosScreenPgTest


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class SmokeTestCases(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self._CategoryBtns = "android.widget.TextView"
        self._Cat1Items = "android.widget.TextView"

        self.gt = LoginPageTest(self.driver)
        self.bp = BasePage(self.driver)
        self.cf = AppLaunchPermission(self.driver)
        self.ip = InitialCashTest(self.driver)
        self.ph = POSHomePageTest(self.driver)
        self.ps = PosScreenPgTest(self.driver)
        self.pb = PosBillPgTest(self.driver)
        self.validatetext = "Paper is not available."

    @pytest.mark.run(order=1)
    def test_PrintBills_TC1(self):
        cl.allureLogs("Testcase1 executing....App Opened")
        # self.cf.clickAllowBtn1()
        # self.cf.clickAllowBtn2()
        try:
            self.cf.clickCloudMode()
            self.cf.selectServer()
            self.cf.selectTestServer()
            self.cf.testServerSubmit()
        except Exception as e:
            print(e)
        # self.cf.enterLicenseKey()
        # self.driver.hide_keyboard()
        # self.cf.LicenseSubmitBtn()
        # time.sleep(20)
        # self.gt.verifyLoginScreen()
        # self.gt.enterUsername()
        # self.gt.enterPassword()
        # self.gt.clickLoginSubmitBtn()
        # self.ip.enterInitialCash()
        # self.ip.clickICSubmitBtn()
        self.gt.launchOK()
        self.ph.clickOnPOS()
        for i in range(0, 5000, 1):
            self.validatetext = "Paper is not available."
            self.ps.clickOnitem1()
            self.ps.clickOnitem2()
            time.sleep(1)
            self.ps.clickOnTotalAmount()
            self.pb.clickOnPrintBill()
            try:
                if self.validatetext in self.driver.find_element_by_id("android:id/message").text:
                    time.sleep(20)
                    el2 = self.driver.find_element_by_id("android:id/button1")  # click on ok btn
                    el2.click()
                    self.ps.clickOnTotalAmount()
                    self.pb.clickOnPrintBill()
            except Exception as e:
                print(e)
            time.sleep(7)
            print(i)
            cl.allureLogs(i)
        cl.allureLogs("Finished Printing 200 bills. Testcase1 completed")

    # @pytest.mark.run(order=2)
    # def test_TestCase2(self):
    #     cl.allureLogs("Testcase2 executing...!!")
    #     for i in range(0, 2, 1):
    #         print("******************************************************")
    #         element1 = self.driver.find_elements_by_class_name("android.widget.TextView")
    #         for x1 in element1:
    #             button1 = x1.text
    #             if button1 == "Nuts & Seeds":
    #                 x1.click()  # Click on Nuts & Seeds
    #                 print("clicked on nuts and seeds")
    #                 time.sleep(7)
    #                 Nuts_items = self.driver.find_elements_by_class_name("android.widget.TextView")
    #                 for y1 in Nuts_items:
    #                     # print(y1.text)
    #                     btn_Nuts_items = y1.text
    #                     if btn_Nuts_items == "Almonds Premium 250g":
    #                         y1.click()  # click on Item1
    #                     if btn_Nuts_items == "Almonds Premium 500g":
    #                         y1.click()  # click on Item1
    #                     if btn_Nuts_items == "Almonds Sonora 100g":
    #                         y1.click()  # click on Item1
    #                 break
    #         self.ps.clickOnTotalAmount()
    #         self.pb.clickOnPrintBill()
    #         try:
    #             if self.validatetext in self.driver.find_element_by_id("android:id/message").text:
    #                 time.sleep(20)
    #                 el2 = self.driver.find_element_by_id("android:id/button1")  # click on ok btn
    #                 el2.click()
    #                 self.ps.clickOnTotalAmount()
    #                 self.pb.clickOnPrintBill()
    #         except Exception as e:
    #             print(e)
    #         time.sleep(10)
    #         element2 = self.driver.find_elements_by_class_name("android.widget.TextView")
    #         for x2 in element2:
    #             button2 = x2.text
    #             if button2 == "Snacks":
    #                 x2.click()
    #                 time.sleep(7)
    #                 print("clicked on Snacks")
    #                 Snacks_items = self.driver.find_elements_by_class_name("android.widget.TextView")
    #                 for y2 in Snacks_items:
    #                     print(y2.text)
    #                     btn_Snacks_items = y2.text
    #                     if btn_Snacks_items == "Bajra Flakes HS 250g":
    #                         y2.click()  # click on Item1
    #                     if btn_Snacks_items == "Bake Lite Speciai Khari":
    #                         y2.click()  # click on Item1
    #                     if btn_Snacks_items == "Bake Munch Krunchy Khari 1 pkt":
    #                         y2.click()  # click on Item1
    #                 break
    #
    #         self.ps.clickOnTotalAmount()
    #         self.pb.clickOnPrintBill()
    #         try:
    #             if self.validatetext in self.driver.find_element_by_id("android:id/message").text:
    #                 time.sleep(20)
    #                 el2 = self.driver.find_element_by_id("android:id/button1")  # click on ok btn
    #                 el2.click()
    #                 self.ps.clickOnTotalAmount()
    #                 self.pb.clickOnPrintBill()
    #         except Exception as e:
    #             print(e)
    #         time.sleep(10)
    #
    #         element3 = self.driver.find_elements_by_class_name("android.widget.TextView")
    #         for x3 in element3:
    #             button3 = x3.text
    #             if button3 == "Staples":
    #                 x3.click()
    #                 time.sleep(7)
    #                 print("clicked on Staples")
    #                 Staples_items = self.driver.find_elements_by_class_name("android.widget.TextView")
    #                 for y3 in Staples_items:
    #                     print(y3.text)
    #                     btn_Staples_items = y3.text
    #                     if btn_Staples_items == "Betel Honeys 250g":
    #                         y3.click()  # click on Item1
    #                     if btn_Staples_items == "Black Gram (Uddalu) 500g":
    #                         y3.click()  # click on Item1
    #                     if btn_Staples_items == "Black Gram pieces 500g":
    #                         y3.click()  # click on Item1
    #                 break
    #         self.ps.clickOnTotalAmount()
    #         self.pb.clickOnPrintBill()
    #         try:
    #             if self.validatetext in self.driver.find_element_by_id("android:id/message").text:
    #                 time.sleep(20)
    #                 el2 = self.driver.find_element_by_id("android:id/button1")  # click on ok btn
    #                 el2.click()
    #                 self.ps.clickOnTotalAmount()
    #                 self.pb.clickOnPrintBill()
    #         except Exception as e:
    #             print(e)
    #         time.sleep(10)
    #         print("Sucessfull testcase1")
    #     cl.allureLogs("Testcase2 completed")
    #
    # @pytest.mark.run(order=3)
    # def test_TestCase3(self):
    #     cl.allureLogs("Testcase3 executing...!!")
    #     for i in range(0, 2, 1):
    #         validatetext = "Paper is not available."
    #         self.pb.clickOnSearchBar()
    #         time.sleep(3)
    #         self.pb.enterSearchItem1()
    #         self.pb.clickOnViewItemName()
    #         time.sleep(3)
    #
    #         self.pb.clickOnSearchBar()
    #         time.sleep(3)
    #         self.pb.enterSearchItem2()
    #         self.pb.clickOnViewItemName()
    #         time.sleep(3)
    #
    #         self.pb.clickOnSearchBar()
    #         time.sleep(3)
    #         self.pb.enterSearchItem3()
    #         self.pb.clickOnViewItemName()
    #
    #         self.ps.clickOnTotalAmount()
    #         self.pb.clickOnPrintBill()
    #         try:
    #             if validatetext in self.driver.find_element_by_id("android:id/message").text:
    #                 time.sleep(20)
    #                 el2 = self.driver.find_element_by_id("android:id/button1")  # click on ok btn
    #                 el2.click()
    #                 self.ps.clickOnTotalAmount()
    #                 self.pb.clickOnPrintBill()
    #         except Exception as e:
    #             print(e)
    #         print("Successful")
    #     cl.allureLogs("Testcase3 completed")
    #
    # @pytest.mark.run(order=4)
    # def test_Testcase4(self):
    #     cl.allureLogs("Testcase4 executing")
    #     for i in range(0, 2, 1):
    #         self.validatetext = "Paper is not available."
    #         # card
    #         self.ps.clickOnitem1()
    #         self.ps.clickOnitem2()
    #         self.ps.clickOnTotalAmount()
    #         self.pb.clickCardOption()
    #         self.pb.enterTransactionId()
    #         self.pb.clickTransSubmitBtn()
    #         try:
    #             if self.validatetext in self.driver.find_element_by_id("android:id/message").text:
    #                 time.sleep(20)
    #                 el2 = self.driver.find_element_by_id("android:id/button1")  # click on ok btn
    #                 el2.click()
    #                 self.ps.clickOnTotalAmount()
    #                 self.pb.clickCardOption()
    #                 self.pb.enterTransactionId()
    #                 self.pb.clickTransSubmitBtn()
    #                 # self.pb.clickOnPrintBill()
    #         except Exception as e:
    #             print(e)
    #         # Wallet
    #         self.ps.clickOnitem1()
    #         self.ps.clickOnitem2()
    #         self.ps.clickOnTotalAmount()
    #         self.pb.clickWalletOption()
    #         self.pb.enterTransactionId()
    #         self.pb.clickTransSubmitBtn()
    #         # Coupon
    #         self.ps.clickOnitem1()
    #         self.ps.clickOnitem2()
    #         self.ps.clickOnTotalAmount()
    #         self.pb.clickCouponOption()
    #         self.pb.enterTransactionId()
    #         self.pb.clickTransSubmitBtn()
    #         time.sleep(7)
    #         print(i)
    #         cl.allureLogs(i)
    #     cl.allureLogs("Testcase4 completed")
    #
    # @pytest.mark.run(order=5)
    # def test_Testcase5(self):
    #     cl.allureLogs("Testcase5 executing")
    #     for i in range(0, 10, 1):
    #         self.validatetext = "Paper is not available."
    #         self.ps.clickOnitem1()
    #         self.ps.clickOnitem2()
    #         self.pb.clickOnSideBar()
    #         self.pb.clickOnHoldIcon()
    #         self.pb.clickHoldSaveBtn()
    #         cl.allureLogs(i)
    #     cl.allureLogs("Bills added in Hold list")
    #     for j in range(0, 8, 1):
    #         self.pb.clickOnSideBar()
    #         self.pb.clickOnHoldIcon()
    #         time.sleep(5)
    #         self.pb.clickBillInHoldList()
    #         self.ps.clickOnTotalAmount()
    #         self.pb.clickOnPrintBill()
    #         try:
    #             if self.validatetext in self.driver.find_element_by_id("android:id/message").text:
    #                 time.sleep(20)
    #                 el2 = self.driver.find_element_by_id("android:id/button1")  # click on ok btn
    #                 el2.click()
    #                 self.ps.clickOnTotalAmount()
    #                 self.pb.clickOnPrintBill()
    #         except Exception as e:
    #             print(e)
    #         cl.allureLogs(j)
    #     cl.allureLogs("Printed Hold Bills")
    #
    # cl.allureLogs("Testcase5 completed")
    #
    # @pytest.mark.run(order=6)
    # def test_Testcase6(self):
    #     cl.allureLogs("Testcase6 executing")
    #     for i in range(0, 8, 1):
    #         self.validatetext = "Paper is not available."
    #         self.ps.clickOnitem1()
    #         self.ps.clickOnitem2()
    #         self.ps.clickOnTotalAmount()
    #         self.pb.clickOnPrintBill()
    #         try:
    #             if self.validatetext in self.driver.find_element_by_id("android:id/message").text:
    #                 time.sleep(20)
    #                 el2 = self.driver.find_element_by_id("android:id/button1")  # click on ok btn
    #                 el2.click()
    #                 self.ps.clickOnTotalAmount()
    #                 self.pb.clickOnPrintBill()
    #         except Exception as e:
    #             print(e)
    #     cl.allureLogs("Printed 15 bills")
    #     self.pb.clickOnNavigationbar()
    #     self.pb.clickOnSalesReportBtn()
    #     for j in range(0, 5, 1):
    #         time.sleep(4)
    #         # self.pb.clickOnNavigationbar()
    #         # self.pb.clickOnSalesReportBtn()
    #         self.pb.clickOnFilterIcon()
    #         self.pb.clickOnApplyBtn()
    #         self.pb.clickOnBill()
    #         self.pb.clickOnVoidButton()
    #         self.pb.clickOnSelectReason()
    #         self.pb.clickOnVoidReasonText()
    #         self.pb.clickOnYesBtn()
    #         self.pb.clickOnOKBtn()
    #         self.pb.clickOnBackArrow()
    #         cl.allureLogs(j)
    #
    #     cl.allureLogs("void bills successful")
    #     time.sleep(5)
    #     self.pb.clickOnBackArrow()
    #
    # cl.allureLogs("TestCase 6 void completed")
    #
    # @pytest.mark.run(order=7)
    # def test_Testcase7(self):
    #     cl.allureLogs("Testcase7 executing")
    #     for i in range(0, 1, 1):
    #         self.validatetext = "Paper is not available."
    #         self.pb.clickOnNavigationbar()
    #         self.pb.clickOnConfiguration()
    #         self.pb.clickOnAdmin()
    #         self.pb.clickOnDumpsAndDamage()
    #         for j in range(0, 2, 1):
    #             self.pb.clickOnSelect()
    #             self.pb.clickOnItem1()
    #             self.pb.enterDumpsQty()
    #             self.pb.clickSelectfindings()
    #             self.pb.clickOnDamageOption()
    #             self.pb.clickOnAddDumps()
    #             self.driver.hide_keyboard()
    #             self.pb.clickOnDumpsSubmit()
    #             self.pb.clickOnDumpsSubmitYes()
    #             self.pb.clickOnDumpsSubmitOk()
    #             cl.allureLogs(j)
    #     cl.allureLogs("Dumps and Damage completed")
    #     time.sleep(5)
    #     self.pb.clickOnBackArrow()
    #
    # cl.allureLogs("TestCase 7 completed")
    #
    # @pytest.mark.run(order=8)
    # def test_Testcase8(self):
    #     cl.allureLogs("Testcase 9 executing")
    #     for i in range(0, 1, 1):
    #         self.validatetext = "Paper is not available."
    #         self.pb.clickOnReport()
    #         self.pb.clickOnSalesReport()
    #         # self.pb.clickOnSalesReportBill()
    #         self.pb.Print()
    #         self.pb.backArrow()
    #         self.pb.clickOnDayWiseSalesReport()
    #         self.pb.Print()
    #         self.pb.backArrow()
    #         self.pb.clickOnConsolidatedItemReport()
    #         self.pb.Print()
    #         self.pb.backArrow()
    #         self.pb.clickOnSalesVsTaxReport()
    #         self.pb.Print()
    #         self.pb.backArrow()
    #         self.pb.clickOnMidShiftReport()
    #         self.pb.Print()
    #         self.pb.backArrow()
    #         self.pb.clickOnEndShiftReport()
    #         self.pb.Print()
    #         time.sleep(3)
    #         self.pb.backArrow()
    #         time.sleep(3)
    #         self.pb.backArrow()
    #         time.sleep(3)
    #         self.pb.backArrow()
    #         # time.sleep(3)
    #         # self.pb.clickOnMainLogout()
    #         # time.sleep(2)
    #         # self.pb.clickOnNo_shiftnotend()
    #
    #     cl.allureLogs("Reports completed")
    #
    # cl.allureLogs("TestCase 9 completed")
    #
    # @pytest.mark.run(order=9)
    # def test_Testcase9(self):
    #     cl.allureLogs("Testcase 9 executing")
    #     for i in range(0, 1, 1):
    #         self.validatetext = "Paper is not available."
    #         # self.pb.clickOnDumpsLogoutBtn()
    #         # self.pb.ShiftNotEnd()
    #         time.sleep(5)
    #         self.pb.clickOnMainLogout()
    #         time.sleep(10)
    #         self.pb.clickOnNo_shiftnotend()
    #         time.sleep(4)
    #         self.gt.enterAuditUsername()
    #         self.gt.enterAuditPassword()
    #         self.gt.clickLoginSubmitBtn()
    #         self.pb.EndingShift()
    #         for j in range(0, 2, 1):
    #             self.pb.auditItem1()
    #             self.pb.auditItem2()
    #             self.pb.auditItem3()
    #             self.pb.auditItem4()
    #             self.pb.auditItem5()
    #             self.pb.auditItem6()
    #             self.pb.auditItem7()
    #             self.pb.auditItem8()
    #             self.pb.clickOnSubmitAuditData()
    #             self.pb.clickOnSubmitAuditYes()
    #             self.pb.clickOnSubmitAuditOK()
    #             cl.allureLogs(j)
    #         self.pb.clickOnAuditLogout()
    #     cl.allureLogs("Audit completed")
    #
    # cl.allureLogs("TestCase 9 completed")
