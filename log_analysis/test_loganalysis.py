import pytest
import os
import urllib.parse
import datetime

from loganalysis import SimpleMethod

sim = SimpleMethod()

for line in sim.parse('cloudfront.log'):
    print(line)
    print(line["time-taken"])

    print(line["date"])


print(sim.dicttest())
