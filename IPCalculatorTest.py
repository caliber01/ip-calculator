import unittest
from BitVector import BitVector
from IPAddress import IPAddress
from IPCalculator import IPCalculator


class IPAddressTest(unittest.TestCase):
    def test_split_into_subnets(self):
        ip = IPAddress('193.1.1.0/24')
        self.assertEqual(IPCalculator().split_into_subnets(ip, 6), [
            IPAddress(bit_vector=BitVector(bitstring=bitstring), mask=27)
            for bitstring in [
                '11000001000000010000000100000000',
                '11000001000000010000000100100000',
                '11000001000000010000000101000000',
                '11000001000000010000000101100000',
                '11000001000000010000000110000000',
                '11000001000000010000000110100000'
            ]])


if __name__ == '__main__':
    unittest.main()
