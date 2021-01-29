from AppiumFramework.base.BasePage import BasePage
import AppiumFramework.utilities.customLogger as cl


class PosBillPgTest(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators values in login page
    _printBillBtn = "com.quinta.qpos:id/textViewPrint"
    _CategoryBtns = "android.widget.TextView"
    _Cat1Items = "android.widget.TextView"
    _SearchBar = "com.quinta.qpos:id/imageViewTaskBarSearch"
    _viewItemName = "com.quinta.qpos:id/textViewItemName"
    _SearchItem = "com.quinta.qpos:id/editTextKey"

    _cardOption = "com.quinta.qpos:id/textViewCard"
    _walletOption = "com.quinta.qpos:id/textViewWallet"
    _couponOption = "com.quinta.qpos:id/textViewCoupon"
    _TransactionEditBox = "com.quinta.qpos:id/editText"
    _TransSubmitBtn = "android:id/button1"

    _sidebar = "com.quinta.qpos:id/imageViewSubMenuDrawer"
    _holdIcon = "com.quinta.qpos:id/textViewHold"
    _HoldEditBox = "com.quinta.qpos:id/editTextHoldName"
    _holdSaveBtn = "com.quinta.qpos:id/textViewNew"
    _billInHoldList = "//android.widget.TextView[@index='0']"

    # void scenario locators
    _left_navigation_bar_icon = "com.quinta.qpos:id/imageViewMenuDrawer"
    _Sales_Report_button = "//android.widget.CheckedTextView[@text='Sales Report']"
    _Filter_icon = "com.quinta.qpos:id/imageViewFilter"
    _apply_button = "com.quinta.qpos:id/textViewApply"
    _void_Bill1 = "//android.widget.TextView[@text='Amt:']"
    _void_button = "com.quinta.qpos:id/floatingActionButtonVoid"
    _select_Reason = "com.quinta.qpos:id/spinnerReason"
    _void_reason_text = "//android.widget.TextView[@text='Test']"
    _Yes_btn = "android:id/button1"
    _OK_button = "android:id/button1"
    _Back_Arrow = "com.quinta.qpos:id/imageViewBackArrow"

    # Dumps Scenario
    _configuration = "//android.widget.CheckedTextView[@text='Configuration']"
    _Admin = "//android.widget.TextView[@text='ADMIN']"
    _Dumps_and_Damage = "//android.widget.TextView[@text='Dumps & Damages']"
    _Select = "//android.widget.TextView[@text='Select']"
    _item1 = "//android.widget.TextView[@text='A2 Cow Ghee 500ml1']"
    _dumps_qty = "com.quinta.qpos:id/editTextActualQty"
    _select_findings = "com.quinta.qpos:id/spinnerText"
    _Damage_option = "//android.widget.TextView[@text='Damage']"
    _Add_dumps = "com.quinta.qpos:id/buttonSubmit"
    _Dumps_submit = "com.quinta.qpos:id/buttonFinalSubmit"
    _Dumps_submit_yes = "android:id/button1"
    _Dumps_submit_ok = "android:id/button1"

    # Audit locators
    _dumps_logout_btn = "com.quinta.qpos:id/imageViewLogout"
    _shift_not_ended = "android:id/button2"
    _ending_shift = "android:id/button1"  # click on Yes
    _audit_item1 = "//android.widget.EditText[@bounds='[517,276][752,344]']"
    _audit_item2 = "//android.widget.EditText[@bounds='[517,393][752,461]']"
    _audit_item3 = "//android.widget.EditText[@bounds='[517,510][752,578]']"
    _audit_item4 = "//android.widget.EditText[@bounds='[517,627][752,695]']"
    _audit_item5 = "//android.widget.EditText[@bounds='[517,744][752,812]']"
    _audit_item6 = "//android.widget.EditText[@bounds='[517,861][752,929]']"
    _audit_item7 = "//android.widget.EditText[@bounds='[517,978][752,1046]']"
    _audit_item8 = "//android.widget.EditText[@bounds='[517,1094][752,1162]']"
    _submit_audit_data = "com.quinta.qpos:id/buttonFinalSubmit"
    _submit_audit_data_yes = "android:id/button1"
    _submit_audit_data_ok = "android:id/button1"
    _audit_logout = "com.quinta.qpos:id/imageViewLogout"




    # Reports locators
    _reports = "//android.widget.TextView[@text='Reports']"
    _Sales_report = "//android.widget.TextView[@text='Sales Report']"
    _sales_report_bill = "//android.widget.TextView[@bounds='[580,299][643,340]"
    _sales_report_print = "com.quinta.qpos:id/floatingActionButtonPrint"
    _back_arrow = "com.quinta.qpos:id/imageViewBackArrow"

    _Day_wise_sales_report = "//android.widget.TextView[@text='Day Wise Sales Report']"
    _daywise_print = "com.quinta.qpos:id/floatingActionButtonPrint"
    _consolidated_item_report = "//android.widget.TextView[@text='Consolidated Item Report']"
    _consolidate_print = "com.quinta.qpos:id/floatingActionButtonPrint"
    _Sales_vs_tax_report = "//android.widget.TextView[@text='Sales Vs Tax Report']"
    # _sales_print = "//android.widget.TextView[@text='Sales Vs Tax Report']"
    _mid_shift_report = "//android.widget.TextView[@text='Mid Shift Report']"
    _End_shift = "//android.widget.TextView[@text='End Shift Quick Sales Settlement']"
    _main_logout = "com.quinta.qpos:id/imageViewLogout"
    _shift_not_end = "android:id/button2"

    # Indent creation locators
    _indent = "//android.widget.TextView[@text='Indent']"
    _Indent_add_one = "com.quinta.qpos:id/floatingActionButtonAddIndent"
    _WarehouseOption = "//android.widget.RadioButton[@text='Warehouse']"
    _SelectWarehouse = "com.quinta.qpos:id/spinnerRaisedAgainst"
    _PumaWarehouse = "//android.widget.TextView[@text='Puma']"
    _enterComments = "com.quinta.qpos:id/editTextComments"
    # hide keyboard
    _addIndentSubmitBtn = "com.quinta.qpos:id/buttonSubmit"
    _addIndentSubmitBtnOK = "android:id/button1"
    _AddIndentItem = "com.quinta.qpos:id/floatingActionButtonAddIndentItem"
    _SelectItemName = "com.quinta.qpos:id/textViewItemName"
    _SelectItem1 = "//android.widget.TextView[@text='A2 Cow Ghee 500ml1']"
    _editTextQty = "com.quinta.qpos:id/editTextQty"
    # hide keyboard
    _addItemSubmit = "android:id/button1"
    _addItemSubmitOK = "android:id/button1"
    _backArrow = "com.quinta.qpos:id/imageViewBackArrow"
    _SubmitIndentOption = "com.quinta.qpos:id/imageViewOption"
    _SubmitIndent = "//android.widget.TextView[@text='Submit']"
    _SubmitIndentYes = "android:id/button1"
    _ErrorOk = "android:id/button1"
    _IndentFilter = "com.quinta.qpos:id/imageViewFilter"
    _IndentFilterApply = "com.quinta.qpos:id/textViewApply"

    # Indent creation methods
    def clickOnIndent(self):
        self.clickElement(self._indent, "xpath")
        cl.allureLogs("clicked on Indent link")

    def clickOnAddIndentOne(self):
        self.clickElement(self._Indent_add_one, "xpath")
        cl.allureLogs("clicked on Add Indent")

    def clickOnWarehouseOption(self):
        self.clickElement(self._WarehouseOption, "xpath")
        cl.allureLogs("clicked on Warehouse option")

    def clickOnSelectWarehouse(self):
        self.clickElement(self._SelectWarehouse, "id")
        cl.allureLogs("Selected a warehouse")

    def clickOnWarehouseOption1(self):
        self.clickElement(self._PumaWarehouse, "xpath")
        cl.allureLogs("clicked on Warehouse option 1")

    def enterIndentComments(self):
        self.sendText("items", self._enterComments, "id")
        cl.allureLogs("Entered indent comments")
    # hide keyboard

    def clickOnAddIndentSubmitBtn(self):
        self.clickElement(self._addIndentSubmitBtn, "id")
        cl.allureLogs("clicked on add Indent Submit Btn")

    def clickOnAddIndentSubmitBtnOK(self):
        self.clickElement(self._addIndentSubmitBtnOK, "id")
        cl.allureLogs("clicked on add Indent Submit Btn OK")

    def clickOnAddIndentItem(self):
        self.clickElement(self._AddIndentItem, "id")
        cl.allureLogs("clicked on add Indent item")

    def clickOnSelectItemName(self):
        self.clickElement(self._SelectItemName, "id")
        cl.allureLogs("Select a item name")

    def clickOnSelectItem1(self):
        self.clickElement(self._SelectItem1, "id")
        cl.allureLogs("Select a item 1")

    def enterItemQty(self):
        self.sendText("items", self._editTextQty, "id")
        cl.allureLogs("Entered item qty")

    def clickOnSubmitIndentOption(self):
        self.clickElement(self._SubmitIndentOption, "id")
        cl.allureLogs("clicked on add Indent Submit Option")

    def clickOnSubmitIndent(self):
        self.clickElement(self._SubmitIndent, "xpath")
        cl.allureLogs("clicked on Submit Indent")

    def clickOnSubmitIndentYes(self):
        self.clickElement(self._SubmitIndentYes, "id")
        cl.allureLogs("clicked on Submit Indent")

    def clickOnErrorOK(self): #will be using this method untill the issue is fixed
        self.clickElement(self._ErrorOk, "id")
        cl.allureLogs("clicked on error ok")

    def clickOnIndentFilter(self):
        self.clickElement(self._IndentFilter, "id")
        cl.allureLogs("clicked on Indent Filter")

    def clickOnIndentFilterApply(self):
        self.clickElement(self._IndentFilterApply, "id")
        cl.allureLogs("Applied indent filter")




    # reports methods
    def clickOnMainLogout(self):
        self.clickElement(self._main_logout, "id")
        cl.allureLogs("clicked on main logout")

    def clickOnNo_shiftnotend(self):
        self.clickElement(self._shift_not_end, "id")
        cl.allureLogs("Shift not ended")

    def clickOnReport(self):
        self.clickElement(self._reports, "xpath")
        cl.allureLogs("clicked on report")

    def clickOnSalesReport(self):
        self.clickElement(self._Sales_report, "xpath")
        cl.allureLogs("clicked on sales report")

    def clickOnSalesReportBill(self):
        self.clickElement(self._sales_report_bill, "xpath")
        cl.allureLogs("clicked on sales report bill")

    def Print(self):
        self.clickElement(self._sales_report_print, "id")
        cl.allureLogs("Prints the report")

    def backArrow(self):
        self.clickElement(self._back_arrow, "id")
        cl.allureLogs("Clicked on back arrow")

    def clickOnDayWiseSalesReport(self):
        self.clickElement(self._Day_wise_sales_report, "xpath")
        cl.allureLogs("Clicked on Day wise sales report")

    def clickOnConsolidatedItemReport(self):
        self.clickElement(self._consolidated_item_report, "xpath")
        cl.allureLogs("Clicked on Consolidated Item report")

    def clickOnSalesVsTaxReport(self):
        self.clickElement(self._Sales_vs_tax_report, "xpath")
        cl.allureLogs("Clicked on sales vs tax report")

    def clickOnMidShiftReport(self):
        self.clickElement(self._mid_shift_report, "xpath")
        cl.allureLogs("Clicked on mid shift report")

    def clickOnEndShiftReport(self):
        self.clickElement(self._End_shift, "xpath")
        cl.allureLogs("Clicked on end shift report")










    # audit methods
    def clickOnDumpsLogoutBtn(self):
        self.clickElement(self._dumps_logout_btn, "id")
        cl.allureLogs("logout from dumps and damage page")

    def ShiftNotEnd(self):
        self.clickElement(self._shift_not_ended, "id")
        cl.allureLogs("Shift not end, click on NO")

    def EndingShift(self):
        self.clickElement(self._ending_shift, "id")
        cl.allureLogs("Ending Previous shift")

    def auditItem1(self):
        self.sendText("450", self._audit_item1, "xpath")
        cl.allureLogs("Entered actual qty for item1")

    def auditItem2(self):
        self.sendText("620", self._audit_item2, "xpath")
        cl.allureLogs("Entered actual qty for item2")

    def auditItem3(self):
        self.sendText("300", self._audit_item3, "xpath")
        cl.allureLogs("Entered actual qty for item3")

    def auditItem4(self):
        self.sendText("870", self._audit_item4, "xpath")
        cl.allureLogs("Entered actual qty for item4")

    def auditItem5(self):
        self.sendText("390", self._audit_item5, "xpath")
        cl.allureLogs("Entered actual qty for item5")

    def auditItem6(self):
        self.sendText("99", self._audit_item6, "xpath")
        cl.allureLogs("Entered actual qty for item6")

    def auditItem7(self):
        self.sendText("999", self._audit_item7, "xpath")
        cl.allureLogs("Entered actual qty for item7")

    def auditItem8(self):
        self.sendText("888", self._audit_item8, "xpath")
        cl.allureLogs("Entered actual qty for item8")

    def clickOnSubmitAuditData(self):
        self.clickElement(self._submit_audit_data, "id")
        cl.allureLogs("Submitted audit data")

    def clickOnSubmitAuditYes(self):
        self.clickElement(self._submit_audit_data_yes, "id")
        cl.allureLogs("Clicked on submit audit yes")

    def clickOnSubmitAuditOK(self):
        self.clickElement(self._submit_audit_data_ok, "id")
        cl.allureLogs("Clicked on submit audit ok")

    def clickOnAuditLogout(self):
        self.clickElement(self._audit_logout, "id")
        cl.allureLogs("logout from audit page")

    # Dumps scenario methods
    def clickOnConfiguration(self):
        self.clickElement(self._configuration, "xpath")
        cl.allureLogs("Clicked on configuration")

    def clickOnAdmin(self):
        self.clickElement(self._Admin, "xpath")
        cl.allureLogs("Clicked on admin")

    def clickOnDumpsAndDamage(self):
        self.clickElement(self._Dumps_and_Damage, "xpath")
        cl.allureLogs("Clicked on dumps and damage")

    def clickOnSelect(self):
        self.clickElement(self._Select, "xpath")
        cl.allureLogs("Click on select")

    def clickOnItem1(self):
        self.clickElement(self._item1, "xpath")
        cl.allureLogs("Select an item")

    def enterDumpsQty(self):
        self.sendText("10", self._dumps_qty, "id")
        cl.allureLogs("Entered dumps qty")

    def clickSelectfindings(self):
        self.clickElement(self._select_findings, "id")
        cl.allureLogs("Click on select findings")

    def clickOnDamageOption(self):
        self.clickElement(self._Damage_option, "xpath")
        cl.allureLogs("Click on Damage option")

    def clickOnAddDumps(self):
        self.clickElement(self._Add_dumps, "id")
        cl.allureLogs("Click on add")

    def clickOnDumpsSubmit(self):
        self.clickElement(self._Dumps_submit, "id")
        cl.allureLogs("Click on submit")

    def clickOnDumpsSubmitYes(self):
        self.clickElement(self._Dumps_submit_yes, "id")
        cl.allureLogs("Click on yes")

    def clickOnDumpsSubmitOk(self):
        self.clickElement(self._Dumps_submit_ok, "id")
        cl.allureLogs("Click on OK")

    # void scenario methods
    def clickOnNavigationbar(self):
        self.clickElement(self._left_navigation_bar_icon, "id")
        cl.allureLogs("Clicked on left navigation bar")

    def clickOnSalesReportBtn(self):
        self.clickElement(self._Sales_Report_button, "xpath")
        cl.allureLogs("Clicked on sales report btn")

    def clickOnFilterIcon(self):
        self.clickElement(self._Filter_icon, "id")
        cl.allureLogs("Clicked on Filter Icon")

    def clickOnApplyBtn(self):
        self.clickElement(self._apply_button, "id")
        cl.allureLogs("Clicked on apply button")

    def clickOnBill(self):
        self.clickElement(self._void_Bill1, "xpath")
        cl.allureLogs("Clicked on a bill to do void")

    def clickOnVoidButton(self):
        self.clickElement(self._void_button, "id")
        cl.allureLogs("Clicked on void button")

    def clickOnSelectReason(self):
        self.clickElement(self._select_Reason, "id")
        cl.allureLogs("Clicked on select Reason")

    def clickOnVoidReasonText(self):
        self.clickElement(self._void_reason_text, "xpath")
        cl.allureLogs("selected a reason to do void")

    def clickOnYesBtn(self):
        self.clickElement(self._Yes_btn, "id")
        cl.allureLogs("Clicked on Yes")

    def clickOnOKBtn(self):
        self.clickElement(self._OK_button, "id")
        cl.allureLogs("Clicked on OK btn")

    def clickOnBackArrow(self):
        self.clickElement(self._Back_Arrow, "id")
        cl.allureLogs("Clicked on back button")

    # Ends void scenario here

    def clickOnPrintBill(self):
        self.clickElement(self._printBillBtn, "id")
        cl.allureLogs("Clicked on print bill button")

    def clickOnSearchBar(self):
        self.clickElement(self._SearchBar, "id")
        cl.allureLogs("Clicked on search bar button")

    def clickOnViewItemName(self):
        self.clickElement(self._viewItemName, "id")
        cl.allureLogs("Clicked on searched item name")

    def enterSearchItem1(self):
        self.sendText("A2 Cow Ghee 500ml1", self._SearchItem, "id")
        cl.allureLogs("Entered search item1")

    def enterSearchItem2(self):
        self.sendText("Almonds Premium 250g", self._SearchItem, "id")
        cl.allureLogs("Entered search item2")

    def enterSearchItem3(self):
        self.sendText("Almonds Premium 500g", self._SearchItem, "id")
        cl.allureLogs("Entered search item3")

    def clickCardOption(self):
        self.clickElement(self._cardOption, "id")
        cl.allureLogs("Clicked on card option")

    def clickWalletOption(self):
        self.clickElement(self._walletOption, "id")
        cl.allureLogs("clicked on wallet option")

    def clickCouponOption(self):
        self.clickElement(self._couponOption, "id")
        cl.allureLogs("Clicked on coupon opton")

    def enterTransactionId(self):
        self.sendText("1234", self._TransactionEditBox, "id")
        cl.allureLogs("Entered transaction id")

    def clickTransSubmitBtn(self):
        self.clickElement(self._TransSubmitBtn, "id")
        cl.allureLogs("Clicked on Transaction submit button")

    def clickOnSideBar(self):
        self.clickElement(self._sidebar, "id")
        cl.allureLogs("Clicked on side bar")

    def clickOnHoldIcon(self):
        self.clickElement(self._holdIcon, "id")
        cl.allureLogs("Clicked on Hold Icon")

    def clickHoldSaveBtn(self):
        self.clickElement(self._holdSaveBtn, "id")
        cl.allureLogs("Clicked on Hold save button")

    def clickBillInHoldList(self):
        self.clickElement(self._billInHoldList, "xpath")
        # bill[0].click()
        cl.allureLogs("Clicked bill in hold list")
