import unittest
from unittest import TestCase
from unittest.mock import patch, call

import Bitcoin

class testBitcoin(TestCase):

    @patch('Bitcoin.get_API_rate_data')
    def test_value_to_USD(self, mock_rates):
        mock_rate = 123456
        example_api_response = {'rate': mock_rate}
        mock_rates.side_effect = [ example_api_response ]
        value = Bitcoin.get_value_bitcoin()
        expected = Bitcoin.convert_value_to_USD(value, mock_rate)

        converted = Bitcoin.convert_value_to_USD(mock_rate, value)
        self.assertEqual(expected, converted)

if __name__ == '__main__':
    unittest.main()