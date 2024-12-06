import allure
import pytest
import time
from common.parameters_util import read_testcase_file
from common.requests_util import RequestUtil


@allure.epic("IN2.0")
@allure.feature("demo")
class TestCreat():
    @allure.story("接口名称：登录")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/1_EngineeringManagement/creat_folder.yml'))
    def test_login(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
        time.sleep(2)


    @allure.story("接口名称：重命名工程1")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/1_EngineeringManagement/data_backup.yml'))
    def test_getinfo(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
        time.sleep(2)

    @allure.story("接口名称：重命名工程1")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/1_EngineeringManagement/data_backup.yml'))
    def test_getinfo(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
        time.sleep(2)
