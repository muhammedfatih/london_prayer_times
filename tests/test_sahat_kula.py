import unittest
from datetime import datetime, timedelta
from src.utils.sahat_kula import SahatKula

class TestSahatKula(unittest.TestCase):

    def setUp(self):
        self.sahat_kula = SahatKula()

    def test_get_current_time(self):
        current_time = self.sahat_kula.getCurrentTime()
        expected_format = "%H:%M"
        self.assertTrue(datetime.strptime(current_time, expected_format))

    def test_compare_times(self):
        time1 = "12:30"
        time2 = "14:45"
        result = self.sahat_kula.compareTimes(time1, time2)
        self.assertEqual(result, 1)  # time1 is smaller than time2

    def test_get_smaller(self):
        time1 = "12:30"
        time2 = "14:45"
        result = self.sahat_kula.getSmaller(time1, time2)
        self.assertEqual(result, time1)  # time1 is smaller

    def test_get_bigger(self):
        time1 = "12:30"
        time2 = "14:45"
        result = self.sahat_kula.getBigger(time1, time2)
        self.assertEqual(result, time2)  # time2 is bigger

    def tearDown(self):
        # Add any cleanup code if needed
        pass

if __name__ == '__main__':
    unittest.main()
