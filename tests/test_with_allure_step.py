import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser


@allure.tag('web')
@allure.label('owner', 'andrechizh8')
@allure.severity(Severity.NORMAL)
@allure.feature('Проверка наличия задачи в репозитории')
@allure.story('Лямбда шаги через with allure.step')
@allure.link('https://github.com', name='Тестирование')
def test_github_issue():
    with allure.step('Открыть главную страницу'):
        browser.open('https://github.com/').driver.maximize_window()
    with allure.step('Найти репозиторий'):
        browser.element('.header-search-input').click()
        browser.element('.header-search-input').type('eroshenkoam/allure-example')
        browser.element('.header-search-input').press_enter()
    with allure.step('Открыть репозиторий'):
        browser.element(by.link_text('eroshenkoam/allure-example')).click()
    with allure.step('Открыть таб issues'):
        browser.element('#issues-tab').click()
    with allure.step('Проверить наличие issue с номером 53'):
        browser.element(by.partial_text('#53')).should(be.visible)

    browser.quit()
