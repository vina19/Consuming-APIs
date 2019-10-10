import unittest
from unittest import TestCase
from unittest.mock import patch, call

import Bitcoin

class testBitcoin(TestCase):

    @pactch('builtins.input', side_effect=)