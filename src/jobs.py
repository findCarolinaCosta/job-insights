from functools import lru_cache
import csv


@lru_cache
def read(path):
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    with open(path, encoding="utf-8") as file:
        file_reader = csv.reader(file, delimiter=",", quotechar='"')

        header, *data = file_reader

    return [dict(zip(header, row)) for row in data]
