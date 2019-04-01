from common import comMon
from common import configHttp
import readConfig as readConfig
import json

localReadConfig = readConfig.ReadConfig()
localConfigHttp = configHttp.ConfigHttp()
localLogin_xls = comMon.get_xls("userCase.xls", "devLogin")


# localAddAddress_xls = comMon.get_xls("userCase.xls", "addAddress")


# login
def login():
    """
    login
    :return: token
    """
    # set url
    url = comMon.get_url_from_json('devLogin')
    localConfigHttp.set_url(url)

    # set header
    # token = localReadConfig.get_headers("token_v")
    # header = {"token": token}
    # localConfigHttp.set_headers(header)

    # set param
    data = {"name": localLogin_xls[0][2],
            "passwd": localLogin_xls[0][3]}
    localConfigHttp.set_data(data)
    # login
    response = localConfigHttp.post()
    dict = json.loads(response.text)
    token = comMon.get_value_from_return_json2(dict, "result", "apikey")
    return token


# logout
def logout(token):
    """
    logout
    :param token: login token
    :return:
    """
    # set url
    url = comMon.get_url_from_xml('logout')
    localConfigHttp.set_url(url)

    # set header
    header = {'token': token}
    localConfigHttp.set_headers(header)

    # logout
    localConfigHttp.get()