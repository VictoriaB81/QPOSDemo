# 1. Import the files
import  unittest

from AppiumFramework.tests.LoginPageTest import LoginTest
from AppiumFramework.tests.smokeTestcasesTest import SmokeTestcases
from AppiumFramework.tests.InitialCashPageTest import InitalCashTest
from AppiumFramework.tests.PosHomePageTest import POSHomeTest
from AppiumFramework.tests.PosScreenPageTest import PosScreenTest

# 2. Create the object of the class using unitTest
gt = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
pb = unittest.TestLoader().loadTestsFromTestCase(SmokeTestcases) #Has smokeTestcases
icp = unittest.TestLoader().loadTestsFromTestCase(InitalCashTest)
ph = unittest.TestLoader().loadTestsFromTestCase(POSHomeTest)
ps = unittest.TestLoader().loadTestsFromTestCase(PosScreenTest)



# 3. Create TestSuite
regressionTest = unittest.TestSuite([pb]) #pb will run only smoke testcases

# 4. Call the Test Runner method
unittest.TextTestRunner(verbosity=1).run(regressionTest)