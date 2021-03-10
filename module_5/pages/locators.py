from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.ID, "login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators:
    add_to_basket_button = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    product_name = (By.CSS_SELECTOR, "#content_inner h1")
    product_price = (By.CSS_SELECTOR, "p.price_color")
    success_message_with_product_name = (By.CSS_SELECTOR, "div.alertinner > strong")
    basket_message_with_product_price = (By.CSS_SELECTOR, "div.alertinner > p > strong")