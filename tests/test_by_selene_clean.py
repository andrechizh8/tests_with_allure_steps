import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser


@allure.tag('web')
@allure.label('owner', 'andrechizh8')
@allure.severity(Severity.CRITICAL)
@allure.feature('Проверка наличия задачи в репозитории')
@allure.story('Чистый Selene (без шагов)')
@allure.link('https://github.com', name='Тестирование')
def test_github_issue():
    browser.open('https://github.com/')
    browser.element('.header-search-input').click()
    browser.element('.header-search-input').type('eroshenkoam/allure-example')
    browser.element('.header-search-input').press_enter()
    browser.element(by.link_text('eroshenkoam/allure-example')).click()
    browser.element('#issues-tab').click()
    browser.element(by.partial_text('#53')).should(be.visible)

    browser.quit()
