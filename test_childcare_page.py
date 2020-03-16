from childcare_page import ChildcarePage
from provider_database import ProviderDatabase
from constants import CHILDCARE_PAGE_URL
import pytest


@pytest.fixture(scope="module")
def db():
    db = ProviderDatabase(memory=True)
    yield(db)
    db.commit_and_close()


def test_get_num_pages(db):
    childcare_page = ChildcarePage(db, CHILDCARE_PAGE_URL)
    assert childcare_page._get_num_pages() == 57


def test_add_all_size(db):
    childcare_page = ChildcarePage(db, CHILDCARE_PAGE_URL).add_all(num_pages=2)
    assert len(db.get_all_sorted()) == 50


def test_add_all_entries(db):
    childcare_page = ChildcarePage(db, CHILDCARE_PAGE_URL).add_all(num_pages=2)
    res = db.get_all_sorted()
    assert res[0] == ("ABC Child Care Village", None, "Child Care Center",
                      "40045 Village Road", "Temecula", "CA", "92591",
                      "9514910940", "ecollazo@abcvillage.com", None)
    assert res[1] == ("Action Day Learning Center", None, "Child Care Center",
                      "400 Stafford Street", "Folsom", "CA", "95630",
                      "9169850976", "Folsom@actiondaylearningcenter.com", None)
