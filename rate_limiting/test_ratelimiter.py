from ratelimiter import FixedWindow
import pytest


rl = FixedWindow(60, 1000)


def test_1000_requests():
    # test 1000 requests in a five minute block

    x = 0
    while(x < 1000):
        last = rl.can_make_request("you")
        x += 1

    assert last == True


def test_1500_requests():
    x = 0
    while(x < 3000):
        last = rl.can_make_request("me")
        x += 1

    assert last == False

# flawed test
# this CAN fail, if our test goes over the boundary of a five minute period
