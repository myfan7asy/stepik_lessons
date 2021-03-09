class BasePage:
    def __init__(self, driver, link):
        self.driver = driver
        self.link = link

    def open(self, link):
        self.driver.get(link)
