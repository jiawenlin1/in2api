import allure
import pytest
import time
from common.parameters_util import read_testcase_file
from common.requests_util import RequestUtil
@allure.epic("CMS2.0")
@allure.feature("配方管理")
class TestCreat():
    @allure.story("接口名称：创建配方集")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/A1_Formula/create_formulary.yml'))
    def test_create_formulary(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：获取配方集信息")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/A1_Formula/info_formulary.yml'))
    def test_info_formulary(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：修改配方集名称")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/A1_Formula/rename_formulary.yml'))
    def test_rename_formulary(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：创建配方集副本")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/A1_Formula/copy_formulary.yml'))
    def test_copy_formulary(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：删除配方集")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/A1_Formula/delete_formulary.yml'))
    def test_delete_formulary(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：添加配方参数")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/A1_Formula/create_formula_parameter.yml'))
    def test_create_formula_parameter(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：获取配方参数")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/A1_Formula/info_formula_parameter.yml'))
    def test_info_formula_parameter(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：在开发版添加配方")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/A1_Formula/create_formula.yml'))
    def test_create_formula(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：在运行版添加配方")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/A1_Formula/create_formula_cms.yml'))
    def test_create_formula_cms(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：在运行版删除配方")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/A1_Formula/delete_formula_cms.yml'))
    def test_delete_formula_cms(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：在运行版添加配方2")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/A1_Formula/create_formula_cms.yml'))
    def test_create_formula_cms2(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：在运行版保存配方值")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/A1_Formula/save_formula_parameter_cms.yml'))
    def test_save_formula_parameter_cms(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：在运行版创建配方副本")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/A1_Formula/copy_formula_cms.yml'))
    def test_copy_formula_cms(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：在运行版刷新配方集")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/A1_Formula/refresh_formula_cms.yml'))
    def test_refresh_formula_cms(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：应用配方")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/A1_Formula/application_formula_cms.yml'))
    def test_application_formula_cms(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
        time.sleep(1)

    @allure.story("接口名称：应用配方后校验变量值")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/A1_Formula/read_cms_io_var.yml'))
    def test_read_cms_io_var(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
        time.sleep(1)

