import unittest
from BitVector import BitVector
from IPAddress import IPAddress


class IPAddressTest(unittest.TestCase):

    def test_init(self):
        ip1 = IPAddress('192.168.0.1/24')
        ip2 = IPAddress(bit_vector=BitVector(bitstring='11000000101010000000000000000001'), mask=24)
        self.assertEqual(ip1, ip2)

    def test_network_address(self):
        ip = IPAddress('192.168.0.1/24')
        self.assertEqual(str(ip.network_address()), '11000000101010000000000000000000')

    def test_bin(self):
        ip = IPAddress('192.168.0.1/24')
        self.assertEqual(str(ip.ip_bin), '11000000101010000000000000000001')

    def test_host_address(self):
        ip = IPAddress('192.168.0.1/24')
        self.assertEqual(str(ip.host_address()), '00000000000000000000000000000001')

    def test_bin_mask(self):
        ip = IPAddress('192.168.0.1/24')
        self.assertEqual(str(ip.bin_mask()), '11111111111111111111111100000000')

    def test_count_computers(self):
        ip = IPAddress('192.168.0.1/24')
        self.assertEqual(ip.count_computers(), 254)

    def test_domain_address(self):
        ip = IPAddress('192.168.0.1/24')
        self.assertEqual(str(ip.broadcast_address()), '11000000101010000000000011111111')

    def test_min_host(self):
        ip = IPAddress('192.168.0.1/24')
        self.assertEqual(str(ip.min_host()), '11000000101010000000000000000001')

    def test_max_host(self):
        ip = IPAddress('192.168.0.1/24')
        self.assertEqual(str(ip.max_host()), '11000000101010000000000011111110')

if __name__ == '__main__':
    unittest.main()
