## Copyright (c) 2013 Edward Weston Hunter
## See the file license.txt for copying permission.

import datetime


class StopWatch(object):
    def __init__(self):
        self.timestamps = []

    def record_time_stamp(self):
        self.timestamps.append(datetime.datetime.now())

    def get_last_gap(self):
        assert len(self.timestamps) > 1
        return (self.timestamps[-1] - self.timestamps[-2]).total_seconds() * 1000.0

    def get_num_timestamps(self):
        return len(self.timestamps)
