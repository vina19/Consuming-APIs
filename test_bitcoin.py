import unittest
from unittest import TestCase
from unittest.mock import patch, call

import Bitcoin

class testBitcoin(TestCase):

    @patch('Bitcoin.convert_value_to_USD')
    def test_value_to_USD(self, mock_rates):
        mock_rate = 12.3456
        example_api_response = {'rate': mock_rate}
        mock_rates.side_effect = [ example_api_response ]

        converted = Bitcoin.convert_value_to_USD(2, mock_rate)
        self.assertEquals(246.912, converted)

if __name__ == '__main__':
    unittest.main()