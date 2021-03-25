import pytest

from final.pages.home_page import HomePage
from final.pages.search_results_page import SearchResultsPage


class TestProductSearch:
    # DATA
    search_page_path = "search/?q="
    existing_search_keyword = "test"
    non_existing_search_keyword = "123123"

    @pytest.mark.parametrize("search_keyword, results_expected",
                             [(existing_search_keyword, True), (non_existing_search_keyword, False)])
    def test_search_for_a_product(self, driver, search_keyword, results_expected):
        # ARRANGE
        home_page = HomePage(driver)
        home_page.open()

        # ACT
        home_page.search_for_a_product(search_keyword)

        # ASSERT
        search_results_page = SearchResultsPage(driver)
        search_results_page.verify_url(self.search_page_path + search_keyword)
        search_results_page.is_search_keyword_in_title(search_keyword)
        search_results_page.check_for_amount_of_results_found(results_expected)
