Написать тест на проверку названия Issue в репозитории через Web-интерфейс.

Этот тест представить в трех вариантах:
1. Чистый Selene (без шагов)
2. Лямбда шаги через with allure.step
3. Шаги с декоратором @allure.step
4. Разметку тестов всеми аннотациями
В качестве ответа на задание приложите ссылку на свой репозиторий GitHub в поле ответа

---
pip install -r requirements.txt
pytest --alluredir=allure-results
allure.bat serve allure-results
