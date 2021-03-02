import pytest
import psutil
import json

import datetime_tasks
import collections_tasks


class TestDatetimeTasksClass:
    @pytest.mark.parametrize("year, result", [(2019, 261), (2020, 262), (2021, 261)])
    def test_weekdays_finder(self, year, result):
        assert datetime_tasks.workdays_finder(year) == result

    def test_sundays_finder(self):
        assert type(datetime_tasks.sundays_finder(2019)) is list
        assert len(datetime_tasks.sundays_finder(2019)) == 52
        assert "7-2" in datetime_tasks.sundays_finder(2021)

    def test_difference(self):
        assert (
            str(datetime_tasks.difference("Europe/Kiev", "America/Chicago"))
            == "1 day, 14:00:00"
        )


class TestColectionsTasksClass:
    def test_operations(self):
        assert collections_tasks.operations(1, 2).sum == 3
        assert collections_tasks.operations("2", "1").concat == "21"
        assert collections_tasks.operations(1, 2).div == 0.5