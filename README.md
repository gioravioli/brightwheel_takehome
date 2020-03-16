# Usage Instructions

Uses Python 3 and requires these packages:

* BeautifulSoup
* Pandas

To run the pipeline to build the database from all three sources, run this command.

`python pipeline.py`

# Tests

To run the tests: `pytest`

# Design Decisions

The scripts are written in Python as it works well for manipulating datasets.
The database is sqlite for simplicity as it requires no additional installation.

# SQL queries

Run `sqlite brightwheel.db`

How many Family Child Care Home providers are there in the dataset?

```sql
SELECT COUNT(*)
FROM childcare_facilities
WHERE type='Family Child Care Home';
```

Which Zip code has the most providers?

```sql
SELECT zip, COUNT(*)
FROM childcare_facilities
GROUP BY 1
ORDER BY 2 DESC
LIMIT 1;
```

# Future Work

* Investigate the data more to find optimal rules for determining if two entries are the same daycare or not. For example there are two KinderCare Learning Centers with addresses 2415 S Centre City Pkwy and 2417 S Centre City Pkwy which are probably the same location with a typo in one address.
* Determine rules for overwriting data if new data differs (e.g. childcare facility has changed phone number or owner). Right now it will assume it's a new childcare facility.
* Determine what should be primary key or index in sql database
* Enable pipeline to restart without reprocessing the same data
* Add error handling (e.g. if file doesn't exist, or web request fails)
* Add tests for the ProviderDatabase class and utils
* Tests should use snapshots of the webpages as the page could change and break the tests
* Add tests to make sure entries from multiple sources are being added correctly (no duplicate entries or overwritten data)
* Protect against SQL injections and special characters in the data
