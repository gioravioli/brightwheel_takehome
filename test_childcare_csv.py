from childcare_csv import ChildcareCSV
from provider_database import ProviderDatabase
from constants import CSV_FILENAME
import pytest


@pytest.fixture(scope="module")
def db():
    db = ProviderDatabase(memory=True)
    yield(db)
    db.commit_and_close()


def test_add_all_size(db):
    childcare_csv = ChildcareCSV(db, CSV_FILENAME).add_all()
    assert len(db.get_all_sorted()) == 1459


def test_add_all_entries(db):
    childcare_csv = ChildcareCSV(db, CSV_FILENAME).add_all()
    res = db.get_all_sorted()
    assert res[0] == ("(DUP) Kidsbel", None, "Child Care Center",
                      "609 S. Westmoreland Ave.", "Los Angeles", "CA", "90005",
                      "2137851158", None, None)
    assert res[1] == ("4th R - Hollywood Park", None, "Child Care Center",
                      "4915 Harte Way", "Sacramento", "CA", "95822",
                      "9162776186", None, None)
