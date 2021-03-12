from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    login_input = (By.ID, "id_registration-email")
    password_input = (By.ID, "id_registration-password1")
    confirm_password_input = (By.ID, "id_registration-password2")
    register_button = (By.CSS_SELECTOR, "button[name='login_submit']")


class ProductPageLocators:
    add_to_basket_button = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    product_name = (By.CSS_SELECTOR, "#content_inner h1")
    product_price = (By.CSS_SELECTOR, "p.price_color")
    success_message = (By.CSS_SELECTOR, "div.alert-success")
    success_message_with_product_name = (By.CSS_SELECTOR, "div.alertinner > strong")
    basket_message_with_product_price = (By.CSS_SELECTOR, "div.alertinner > p > strong")


class BasePageLocators:
    LOGIN_LINK = (By.ID, "login_link")
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    EMPTY_BASKET_NOTE = (By.XPATH, "//p[normalize-space(text()) = 'Your basket is empty.']")
    BASKET_ITEMS_LIST = (By.CSS_SELECTOR, "div.basket-items")
