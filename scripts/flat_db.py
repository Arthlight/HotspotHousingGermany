"""This module handles interacting with the flats_db sqlite3 database.

This module contains helper functions that query data
given a valid city (Berlin, Hamburg, München).

The following helper functions are contained within this module:

    function data_for           - accepts a city name in form of
                                  a string and queries the local
                                  sqlite3 database for the
                                  associated information.
"""
# Standard library
import sys
sys.path.append('/Users/arthred/Documents/Flat_Crawler_Django')
sys.path.append('/Users/arthred/Documents/Flat_Crawler_Django/scripts')
import _sqlite3


def data_for(city: str) -> tuple:
    """Queries flat data from a sqlite3 database for a specific city

    Given a string that represents a city, which is present in the
    database (München, Berlin, Hamburg), this generator returns
    one tuple of flat data at a time.

    Args:
        city: A string that represents a valid city

    Returns:
        row:  A tuple containing all the values from
              every column in one row of the database.
              The following order is guaranteed to be
              the same every time:
              0: price
              1: sqm
              2: street
              3: area
              4: city
              5: rooms
              6: detail_view_url
    """
    connection = _sqlite3.connect('flats_data.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM flats_data WHERE city=?""", (city,))

    for row in cursor.fetchall():
        yield row

