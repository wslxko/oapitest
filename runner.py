import os
import unittest
from common.Log import MyLog as Log
import readConfig as readConfig
from common import HTMLTestRunner
from common.configEmail import MyEmail

localReadconfig = readConfig.ReadConfig()


class AllTest:
	def __init__(self):
		global log, logger, resultPath, on_off
		log = Log.get_log()
		logger = log.get_logger()
		resultPath = log.get_report_path()
		on_off = localReadconfig.get_email("on_off")
		self.caseListFile = os.path.join(readConfig.proDir, "caselist.txt")
		self.caseFile = os.path.join(readConfig.proDir, "testcase")
		self.caseList = []
		self.email = MyEmail.get_email()

	def set_case_list(self):
		fb = open(self.caseListFile)
		for value in fb.readlines():
			data = str(value)
			if data != '' and not data.startswith("#"):
				self.caseList.append(data.replace("\n", " "))
			fb.close()

	def set_case_suite(self):
		self.set_case_list()
		test_suite = unittest.TestSuite()
		suite_module = []

		for case in self.caseList:
			case_name = case.split("/")[-1]
			print(case_name + ".py")
			discover = unittest.defaultTestLoader.discover(self.caseFile, pattern=case_name + ".py", top_level_dir=None)
			suite_module.append(discover)

		if len(suite_module) > 0:
			for suite in suite_module:
				for test_name in suite:
					test_suite.addTest(test_name)
		else:
			return None

		return test_suite

	def run(self):
		try:
			suit = self.set_case_suite()
			if suit is not None:
				logger.info('*********TEST START***********')
				fp = open(resultPath, 'wb')
				runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Test Report', description='Test Description')
				runner.run(suit)
			else:
				logger.info('Have no case to test.')
		except Exception as ex:
			logger.error(str(ex))
		finally:
			logger.info('********TEST END*********')

			if on_off == 'on':
				self.email.send_email()
			elif on_off == 'off':
				logger.info("Doesn't send report email to developer.")
			else:
				logger.info('UnKnow state')


if __name__ == "__main__":
	obj = AllTest()
	obj.run()
