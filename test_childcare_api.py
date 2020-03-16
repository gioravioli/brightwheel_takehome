from childcare_api import ChildcareAPI
from provider_database import ProviderDatabase
from constants import API_URL
import pytest


@pytest.fixture(scope="module")
def db():
    db = ProviderDatabase(memory=True)
    yield(db)
    db.commit_and_close()


def test_add_all_size(db):
    childcare_api = ChildcareAPI(db, API_URL).add_all()
    assert len(db.get_all_sorted()) == 1500


def test_add_all_entries(db):
    childcare_api = ChildcareAPI(db, API_URL).add_all()
    res = db.get_all_sorted()
    assert res[0] == ("(DUP) Kidsbel", "prvdrs_LtHHE6UwDTBF292EjBmUvrcI", None,
                      None, None, None, None, "2137851158",
                      "kidsbelschool@gmail.com", "Kayla Milner")
    assert res[1] == ("4th R - Hollywood Park",
                      "prvdrs_tLYUGNzRqi8HlyK1qmZ2xS8j", None, None, None,
                      None, None, "9162776186",
                      "hpark4thr@cityofsacramento.org", "Sandy Campos")
