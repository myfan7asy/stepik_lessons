from selenium.webdriver.common.by import By

from final.pages.base_page import BasePage


class SearchResultsPage(BasePage):
    title_with_search_keyword_locator = (By.CSS_SELECTOR, "h1")
    found_results_number_locator = (By.CSS_SELECTOR, "form.form-horizontal strong")

    def is_search_keyword_in_title(self, search_keyword):
        title = self.driver.find_element(*self.title_with_search_keyword_locator)
        assert search_keyword in title.text, \
            "Title does not have relevant search keyword"

    def check_for_amount_of_results_found(self, results_expected=True):
        results_found = self.driver.find_element(*self.found_results_number_locator)
        if results_expected is True:
            assert int(results_found.text) > 0, \
                "Search keyword is relevant, but there are no search results.\n" \
                f"Actual amount: '{int(results_found.text)}', expected amount: '> 0'"
        elif results_expected is False:
            assert int(results_found.text) == 0, \
                "We do not expect search_results with the following search_keyword.\n" \
                f"Actual amount: '{int(results_found.text)}', expected amount: '0'"
        else:
            return False
