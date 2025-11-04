import time
from collections import defaultdict

class FixedWindow:
    """
    Uses a fixed-window method to rate limit requests.
    We essentially divide up the epoch into slices based on our window size/period,
    and get the start second for the latest using a modulo operator
    """
    def __init__(self, period: int, max_reqs: int):
        """_summary_

        Args:
            period (int): block of time in which x reqs are allowed. Our time window
            max_reqs (int): how many requests we can make in the window
        """
        self.max_reqs = max_reqs
        self.period = period
        # a dictionary to store our request counts per period.
        # using defaultdict so it automatically assigns a default value
        self.request_tracking = defaultdict(int)
        # a dictionary to store our times by user id
        self.timestamps = {}


    def can_make_request(self, uid: str) -> bool:
        """_summary_

        Args:
            uid (str): user ID (api key or whatever)

        Returns:
            bool: _description_
        """

        now = int(time.time()) # now from epoch in seconds
        window_started = now - (now % self.period) # the timestamp when THIS window started

        # do we have an entry for this user with this timestamp?
        # i.e. have we started tracking the user in this block of time?
        # if not, start them at zero
        if self.timestamps.get(uid) != window_started:
            self.timestamps[uid] = window_started
            self.request_tracking[uid] = 0

        # are we under threshold in this period?
        if self.request_tracking[uid] < self.max_reqs:
            self.request_tracking[uid] += 1
            return True

        return False
