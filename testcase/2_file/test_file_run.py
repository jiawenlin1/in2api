import allure
import pytest
import time
from common.parameters_util import read_testcase_file
from common.requests_util import RequestUtil


@allure.epic("IN2.0")
@allure.feature("文件模块")
class TestCreat():
    @allure.story("接口名称：获取上传链接")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/2_file/upload_urls.yml'))
    def test_upload_urls(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
        time.sleep(0.1)

    @allure.story("接口名称：上传文件")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/2_file/file_upload.yml'))
    def test_file_upload(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
        time.sleep(0.1)

    @allure.story("接口名称：更新文件信息")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/2_file/update_file_information.yml'))
    def test_update_file_information(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
        time.sleep(0.1)



