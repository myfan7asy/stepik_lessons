class BasePage:
    def __init__(self, driver, link):
        self.driver = driver
        self.link = link

    def open_page(self, driver, link):
        self.driver.get(link)
