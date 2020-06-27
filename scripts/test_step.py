import allure
class TestSetup:
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step("我是名称")
    def test_001(self):
        """添加测试步骤"""
        # 添加描述信息
        allure.attach("我是内容","附件名字")

    @allure.severity(allure.severity_level.CRITICAL)
    def test_002(self):
        assert False