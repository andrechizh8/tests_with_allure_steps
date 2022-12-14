import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from allure import attachment_type


@allure.tag('web')
@allure.label('owner', 'andrechizh8')
@allure.severity(Severity.NORMAL)
@allure.feature('Проверка наличия задачи в репозитории')
@allure.story('Шаги с декоратором @allure.step')
@allure.link('https://github.com', name='Тестирование')
def test_decorator_steps():
    open_main_page()
    find_repo('eroshenkoam/allure-example')
    open_repo('eroshenkoam/allure-example')
    open_issue()
    check_repo_with_number('#53')


@allure.step('Открыть главную страницу')
def open_main_page():
    browser.open('https://github.com/')


@allure.step('Найти репозиторий {repository}')
def find_repo(repository):
    browser.element('.header-search-input').click()
    browser.element('.header-search-input').type(repository)
    browser.element('.header-search-input').press_enter()


@allure.step('Открыть репозиторий {repository}')
def open_repo(repository):
    browser.element(by.link_text(repository)).click()


@allure.step('Открыть таб issues')
def open_issue():
    browser.element('#issues-tab').click()


@allure.step('Проверить наличие issue с номером {num}')
def check_repo_with_number(num):
    browser.element(by.partial_text(num)).should(be.visible)


browser.quit()
