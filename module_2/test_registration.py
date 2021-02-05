from selenium import webdriver
from selenium.webdriver.common.by import By

okRegFormURL = "http://suninjuly.github.io/registration1.html"
nokRegFormURL = "http://suninjuly.github.io/registration2.html"

fNameLocator = "//label[contains(text(),'First name*')]/following-sibling::input"
lNameLocator = "//label[contains(text(),'Last name*')]/following-sibling::input"
emailLocator = "//label[contains(text(),'Email*')]/following-sibling::input"
phoneLocator = "//label[contains(text(),'Phone:')]/following-sibling::input"
addressLocator = "//label[contains(text(),'Address:')]/following-sibling::input"
btnLocator = "//button[@type='submit']"

try:
    driver = webdriver.Chrome()
    driver.get(nokRegFormURL)

    fNameInput = driver.find_element(By.XPATH, fNameLocator)
    fNameInput.send_keys("Alex")
    lNameInput = driver.find_element(By.XPATH, lNameLocator)
    lNameInput.send_keys("Grey")
    emailInput = driver.find_element(By.XPATH, emailLocator)
    emailInput.send_keys("gg@gg.gg")
    phoneInput = driver.find_element(By.XPATH, phoneLocator)
    phoneInput.send_keys("+38063111223344")
    addressInput = driver.find_element(By.XPATH, addressLocator)
    addressInput.send_keys("Elk str")

    # Отправляем заполненную форму
    submitBtn = driver.find_element(By.XPATH, btnLocator)
    submitBtn.click()

    # Проверяем, что смогли зарегистрироваться

    # Нходим элемент, содержащий текст
    welcomeTextElem = driver.find_element(By.TAG_NAME, 'h1')
    # Записываем в переменную welcomeText текст из элемента welcomeTextElem
    welcomeText = welcomeTextElem.text

    # С помощью assert проверяем, что текст на сайте совпадает с ожидаемым текстом
    assert welcomeText == "Congratulations! You have successfully registered!"

finally:
    # Закрываем браузер после всех манипуляций
    driver.quit()
