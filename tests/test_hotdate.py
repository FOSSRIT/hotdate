import freezegun
from freezegun import freeze_time
from datetime import datetime
from hotdate import hotdate

class TestHotdate(object):

	@freeze_time('2014-01-01')
	def test_end_of(self):
		assert hotdate().end_of('year') == datetime(2014, 12, 31, 23, 59, 59)
		assert hotdate().end_of('month') == datetime(2014, 1, 31, 23, 59, 59)
		assert hotdate().end_of('day') ==  datetime(2014, 1, 1, 23, 59, 59)
		assert hotdate().end_of('hour') == datetime(2014, 1, 1, 0, 59, 59)
		assert hotdate().end_of('minute') == datetime(2014, 1, 1, 0, 0, 59)
		assert hotdate().end_of('second') == datetime(2014, 1, 1)

	@freeze_time('2014-12-31 23:59:59')
	def test_start_of(self):
		assert hotdate().start_of('year') == datetime(2014, 1, 1)
		assert hotdate().start_of('month') == datetime(2014, 12, 1)
		assert hotdate().start_of('day') ==  datetime(2014, 12, 31)
		assert hotdate().start_of('hour') == datetime(2014, 12, 31, 23, 0, 0)
		assert hotdate().start_of('minute') == datetime(2014, 12, 31, 23, 59, 0)
		assert hotdate().start_of('second') == datetime(2014, 12, 31, 23, 59, 59)

	@freeze_time('2014-01-01')
	def test_add(self):
		assert hotdate().add(year=1) == datetime(2015, 1, 1)
		assert hotdate().add(years=1) == datetime(2015, 1, 1)
		assert hotdate().add(month=1) == datetime(2014, 2, 1)
		assert hotdate().add(months=1) == datetime(2014, 2, 1)
		assert hotdate().add(day=1) == datetime(2014, 1, 2)
		assert hotdate().add(days=1) == datetime(2014, 1, 2)
		assert hotdate().add(hour=1) == datetime(2014, 1, 1, 1)
		assert hotdate().add(hours=1) == datetime(2014, 1, 1, 1)
		assert hotdate().add(minute=1) == datetime(2014, 1, 1, 0, 1)
		assert hotdate().add(minutes=1) == datetime(2014, 1, 1, 0, 1)
		assert hotdate().add(second=1) == datetime(2014, 1, 1, 0, 0, 1)
		assert hotdate().add(seconds=1) == datetime(2014, 1, 1, 0, 0, 1)
		assert hotdate(2014, 1, 31).add(month=1) == datetime(2014, 2, 28)
		assert hotdate(2014, 1, 31).add(day=1) == datetime(2014, 2, 1)
		assert hotdate(2014, 1, 31).add(months=13) == datetime(2015, 2, 28)

	@freeze_time('2014-01-01')
	def test_subtract(self):
		assert hotdate().subtract(year=1) == datetime(2013, 1, 1)
		assert hotdate().subtract(years=1) == datetime(2013, 1, 1)
		assert hotdate().subtract(month=1) == datetime(2013, 12, 1)
		assert hotdate().subtract(months=1) == datetime(2013, 12, 1)
		assert hotdate().subtract(day=1) == datetime(2013, 12, 31)
		assert hotdate().subtract(days=1) == datetime(2013, 12, 31)
		assert hotdate().subtract(hour=1) == datetime(2013, 12, 31, 23)
		assert hotdate().subtract(hours=1) == datetime(2013, 12, 31, 23)
		assert hotdate().subtract(minute=1) == datetime(2013, 12, 31, 23, 59)
		assert hotdate().subtract(minutes=1) == datetime(2013, 12, 31, 23, 59)
		assert hotdate().subtract(second=1) == datetime(2013, 12, 31, 23, 59, 59)
		assert hotdate().subtract(seconds=1) == datetime(2013, 12, 31, 23, 59, 59)
		assert hotdate(2014, 1, 31).subtract(month=1) == datetime(2013, 12, 31)
		assert hotdate(2014, 3, 1).subtract(day=1) == datetime(2014, 2, 28)
		assert hotdate(2014, 1, 31).subtract(months=13) == datetime(2012, 12, 31)
