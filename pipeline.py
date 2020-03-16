from provider_database import ProviderDatabase
from childcare_page import ChildcarePage
from childcare_api import ChildcareAPI
from childcare_csv import ChildcareCSV
from constants import CHILDCARE_PAGE_URL, API_URL, CSV_FILENAME


def run(page=True, api=True, csv=True):
    db = ProviderDatabase()
    if page:
        childcare_page = ChildcarePage(db, CHILDCARE_PAGE_URL)
        childcare_page.add_all()
    if api:
        childcare_api = ChildcareAPI(db, API_URL)
        childcare_api.add_all()
    if csv:
        childcare_csv = ChildcareCSV(db, CSV_FILENAME)
        childcare_csv.add_all()
    db.commit_and_close()


if __name__ == '__main__':
    run(page=True, api=True, csv=True)
