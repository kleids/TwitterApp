from django.test import TestCase
import datetime
from django.utils import timezone
from twitter.models import Poll


class PollMethodTests(TestCase):
    def test_was_published_recently_with_future_poll(self):
        # was_published_recently() should return False for twitter whose pub_date
        # are in the future
        future_poll = Poll(pub_date=timezone.now() + datetime.timedelta(days=30))
        self.assertEqual(future_poll.was_published_recently(), False)

    def test_was_published_recently_with_old_poll(self):
        # was_published_recently() should return False for twitter whose pub_date
        # is older than 1 day
        old_poll = Poll(pub_date=timezone.now() - datetime.timedelta(days=30))
        self.assertEqual(old_poll.was_published_recently(), False)

    def test_was_published_recently_with_recent_poll(self):
        # was_published_recently() should return True for twitter whose pub_date
        # is within the last day
        recent_poll = Poll(pub_date=timezone.now() - datetime.timedelta(hours=1))
        self.assertEqual(recent_poll.was_published_recently(), True)


def create_poll(question, days):
    # Creates a poll with the given `question` published the given number of
    # `days` offset to now (negative for twitter published in the past,
    # positive for twitter that have yet to be published).
    return Poll.objects.create(question=question, pub_date=timezone.now() + datetime.timedelta(days=days))
