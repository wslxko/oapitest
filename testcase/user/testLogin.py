import readConfig as readconfig
from common.Log import MyLog
from common import configHttp
import unittest
import paramunittest
from common import comMon
from common import businessCommon

register_xls = comMon.get_xls('userCase.xls', 'loginUser')
localConfigHttp = configHttp.ConfigHttp()
localReadConfig = readconfig.ReadConfig()


@paramunittest.parametrized(*register_xls)
class RegisterCase(unittest.TestCase):
    def setParameters(self, case_name, method, name, passwd, result, code, message):
        """
        :param case_name:
        :param method:
        :param token:
        :param apikey:
        :param passwd:
        :param result:
        :param code:
        :param msg:
        :return:
        """

        self.case_name = case_name
        self.method = method
        self.name = name
        self.passwd = passwd
        self.result = result
        self.code = int(code)
        self.message = str(message)
        self.response = None
        self.info = None

    def description(self):
        print(self.case_name)

    def setUp(self):
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()
        self.login_apikey = businessCommon.login()

    def tearDown(self):
        pass

    def test_Register(self):
        # set url
        self.url = comMon.get_url_from_json('login')
        localConfigHttp.set_url(self.url)

        # set header
        # if self.apikey == '0':
        #     apiKey = self.login_apikey
        # elif self.apikey == '1':
        #     apiKey = localReadConfig.get_headers("token_v")
        # else:
        #     apiKey = self.apikey
        # header = {'token': apiKey}
        # localConfigHttp.set_headers(header)

        # set parama
        data = {'name': self.name,
                'apikey': self.login_apikey,
                'passwd': self.passwd
                }
        print(self.name, self.login_apikey, self.passwd)
        localConfigHttp.set_data(data)
        self.response = localConfigHttp.post()
        self.checkResult()

    def checkResult(self):
        """
        check test result
        :return:
        """
        self.info = self.response.json()
        # show return message
        comMon.show_return_msg(self.response)
        if self.result == '0':
            self.assertEqual(self.info['code'], self.code)
            self.assertEqual(self.info['message'], self.message)

    # if self.result == '1':
    # 	self.assertEqual(self.info['code'], self.code)
    # 	self.assertEqual(self.info['msg'], self.msg)
    # 	if self.case_name == 'register_EmailExist':
    # 		# delete register user from db
    # 		sql = comMon.get_sql('newsitetest', 'rs_member', 'delete_user')
    # 		localConfigDB.executeSQL(sql, self.email)
    # 		localConfigDB.closeDB()


if __name__ == "__main__":
    unittest.main()
