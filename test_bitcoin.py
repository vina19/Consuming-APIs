import unittest
from unittest import TestCase
from unittest.mock import patch, call

import Bitcoin

class testBitcoin(TestCase):

    @patch('Bitcoin.convert_value_to_USD')
    def test_value_to_USD(self, mock_rates):
        mock_rate = 12.34567
        example_api_response = {'bpi': {'USD': {'code': 'USD', 'symbol': '&#36;', 'rate': {mock_rate}, 'description': 'United States Dollar', 'rate_float' : '8569.8667'}}}
        mock_rates.side_effect = [ example_api_response ]

        converted = Bitcoin.convert_value_to_USD(100, 'rate')
        self.assertEqual(8,569,866.700, converted)

if __name__ == '__main__':
    unittest.main()

    