import os
from xlrd import open_workbook
from xml.etree import ElementTree
import readConfig as readConfig
import json
from common import configHttp
from common.Log import MyLog as Log
import requests

proDir = readConfig.proDir
localReadConfig = readConfig.ReadConfig()
localConfigHttp = configHttp.ConfigHttp()
log = Log.get_log()
logger = log.get_logger()


# 从excel中读取测试用例
def get_xls(xls_name, sheet_name):
    """
    get interface data from xls file
    :return:
    """
    cls = []
    # get xls files's path
    xlsPath = os.path.join(proDir, 'testFile', xls_name)
    file = open_workbook(xlsPath)
    sheet = file.sheet_by_name(sheet_name)
    # get one sheet's rows
    nrows = sheet.nrows
    for i in range(nrows):
        if sheet.row_values(i)[0] != u'case_name':
            cls.append(sheet.row_values(i))
    return cls


# 从xml中读取url
def get_url_from_xml(name):
    """
    By name get url from interfaceURL.xml
    :param name: interface's url name
    :return: url
    """
    url_list = []
    url_path = os.path.join(proDir, 'testFile', 'data.xml')
    tree = ElementTree.parse(url_path)
    for u in tree.findall('url'):
        url_name = u.get('title')
        if url_name == name:
            for c in u.getchildren():
                url_list.append(c.text)
    url = '/'.join(url_list)
    return url


# 从json中读取接口url
def get_url_from_json(name):
    '''

    :param name:
    :return:
    '''
    url_path = os.path.join(proDir, 'testfile', 'data.json')
    with open(url_path) as f:
        value = f.read()
        dictValue = json.loads(value)
        apiurl = dictValue[name]
        return apiurl


def get_value_from_return_json2(res, name1, name2):
    value = res[name1][name2]
    return value

def get_value_from_return_json1(res,name):
    value = res[name]
    return value


def show_return_msg(response):
    url = response.url
    msg = response.text
    print("\n请求地址： " + url)
    # print("\n请求返回值： " + '\n' + json.dumps(json.loads(msg), ensure_ascii=False, sort_keys=True, indent=4))
    print(msg)


def get_visitor_token():
    """
    create a token for visitor
    :return:
    """
    host = localReadConfig.get_http("BASEURL")
    response = requests.get(host + "/User/Token/generate")
    info = response.json()
    token = info.get("info")
    logger.debug("Create token:%s" % (token))
    return token


def set_visitor_token_to_config():
    """
    set token that created for visitor to config
    :return:
    """
    token_v = get_visitor_token()
    localReadConfig.set_headers("TOKEN_V", token_v)