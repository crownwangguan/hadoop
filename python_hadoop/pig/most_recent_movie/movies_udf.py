#!/usr/bin/env python

from pig_util import outputSchema
from datetime import datetime
import re

@outputSchema('title:chararray')
def parse_title(title):
    """
    Return the title without the year
    """
    return re.sub(r'\(\d{4}\)', '', title)

@outputSchema('days_since_release:int')
def days_since_release(title):
    """
    Calculate the number of days since the titles release
    """
    date= re.match('\(\d{4}\)', title)
    if date is None:
        return None
    release_date = datetime.strptime(date, '%Y')
    delta = 2017 - release_date
    print delta
    return delta
