from selenium import webdriver
from selenium.webdriver.common.by import By

ok_regform_url = "http://suninjuly.github.io/registration1.html"
nok_regform_url = "http://suninjuly.github.io/registration2.html"

fname_locator = "//label[contains(text(),'First name*')]/following-sibling::input"
lname_locator = "//label[contains(text(),'Last name*')]/following-sibling::input"
email_locator = "//label[contains(text(),'Email*')]/following-sibling::input"
phone_locator = "//label[contains(text(),'Phone:')]/following-sibling::input"
address_locator = "//label[contains(text(),'Address:')]/following-sibling::input"
submit_btn_locator = "//button[@type='submit']"

try:
    # Инициализация драйвера
    driver = webdriver.Chrome()

    # Открывает нужную страницу
    driver.get(nok_regform_url)

    # Заполняем поля формы
    fname_input = driver.find_element(By.XPATH, fname_locator)
    fname_input.send_keys("Alex")
    lname_input = driver.find_element(By.XPATH, lname_locator)
    lname_input.send_keys("Grey")
    email_input = driver.find_element(By.XPATH, email_locator)
    email_input.send_keys("gg@gg.gg")
    phone_input = driver.find_element(By.XPATH, phone_locator)
    phone_input.send_keys("+38063111223344")
    address_input = driver.find_element(By.XPATH, address_locator)
    address_input.send_keys("Elk str")

    # Отправляем заполненную форму
    submit_btn = driver.find_element(By.XPATH, submit_btn_locator)
    submit_btn.click()

    # Проверяем, что смогли зарегистрироваться
    # Нходим элемент, содержащий текст
    welcome_text_elem = driver.find_element(By.TAG_NAME, 'h1')
    # Записываем в переменную welcomeText текст из элемента welcome_text_elem
    welcome_text = welcome_text_elem.text

    # С помощью assert проверяем, что текст на сайте совпадает с ожидаемым текстом
    assert welcome_text == "Congratulations! You have successfully registered!"

finally:
    # Закрываем браузер после всех манипуляций
    driver.quit()
