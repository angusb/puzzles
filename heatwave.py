"""
A solution to: https://gist.github.com/3080200
"""

import sys
import time
import requests
import json

from math import floor

URL = 'http://dl.dropbox.com/u/274/readings_formatted.json'

def location_filter(loc):
    return lambda x: True if x['location'] == loc else False


def location_data(loc_list):
    """
    Takes an list of dicts formatted like {"location": "NRT",
                                            "temperature": 36,
                                            "timestamp": "2012-06-14 13:09:00"}

    And returns data in the format of {'date': {hour: [temperatures]}}
    """
    loc_data = {}
    for loc_day in loc_list:
        input_date, input_time = loc_day['timestamp'].split()
        day = loc_data.setdefault(input_date, {})
        hour = time.strptime(input_time, "%H:%M:%S").tm_hour
        temperatures = day.setdefault(hour, [])
        temperatures.append(loc_day['temperature'])

    return loc_data


def main(argv=None):
    if argv is None:
        argv = sys.argv

    r = requests.get(URL)
    raw_data = json.loads(r.text)

    sfo_list = filter(location_filter('SFO'), raw_data)
    nrt_list = filter(location_filter('NRT'), raw_data)
    iad_list = filter(location_filter('IAD'), raw_data)

    sfo_data = location_data(sfo_list)
    nrt_data = location_data(nrt_list)
    iad_data = location_data(iad_list)

    avg = lambda l: sum(l)/float(len(l))

    a = avg(nrt_data['2012-06-15'][13])
    b = avg(iad_data['2012-06-16'][14])
    c = avg(sfo_data['2012-06-17'][13])

    sol = int(floor(c**(b-a-7)))
    print "Solution: %s" % sol

    r = requests.get('http://priceonomics.com/static/%s.html' % sol)

    print 'Success? %s' % r.ok


if __name__ == "__main__":
    main()
