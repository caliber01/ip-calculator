from tabulate import tabulate
import itertools
from BitVector import BitVector
import utils


class IPAddress:
    def __init__(self, str_val=None, bit_vector=None, mask=None):
        if str_val is not None:
            self.ip, self.mask = str_val.split('/')
            self.mask = int(self.mask)
            self.ip_dec = self.ip.split('.')
            bitstring = ''.join(itertools.chain.from_iterable(utils.dec_to_bin(octet, 8) for octet in self.ip_dec))
            self.ip_bin = BitVector(bitstring=bitstring)
        if bit_vector is not None:
            if mask is None:
                raise Exception('need mask')
            self.ip_bin, self.mask = bit_vector, mask
            self.ip = self.__ip_to_dec(bit_vector)
            self.ip_dec = self.ip.split('.')

    def network_address(self):
        return self.ip_bin[:self.mask] + BitVector(bitstring='0' * (32 - self.mask))

    def host_address(self):
        return BitVector(bitstring=self.mask * '0') + self.ip_bin[self.mask:]

    def bin_mask(self):
        return BitVector(bitstring='1' * self.mask + '0' * (32 - self.mask))

    def count_computers(self):
        return int(self.max_host()) - int(self.min_host()) + 1

    def broadcast_address(self):
        return self.network_address() | (~self.bin_mask())

    def min_host(self):
        return BitVector(intVal=int(self.network_address()) + 1)

    def max_host(self):
        return BitVector(intVal=int(self.broadcast_address()) - 1)

    def info(self):
        return tabulate([
            ['ip', self.ip],
            ['binary', self.__ip_to_bits(self.ip_bin)],
            ['mask', self.__ip_to_bits(self.bin_mask())],
            ['network address', self.__ip_to_dec(self.network_address())],
            ['host address', self.__ip_to_dec(self.host_address())],
            ['broadcast address', self.__ip_to_dec(self.broadcast_address())],
            ['min host', self.__ip_to_dec(self.min_host())],
            ['max host', self.__ip_to_dec(self.max_host())],
            ['total computers', self.count_computers()]
        ])

    def __str__(self):
        return self.ip

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.ip == other.ip and self.mask == other.mask

    def __ne__(self, other):
        return not self.__eq__(other)


    @staticmethod
    def __ip_to_bits(ip):
        return ' '.join(str(chunk) for chunk in utils.chunks(ip, 8))

    @staticmethod
    def __ip_to_dec(ip):
        return '.'.join(str(int(chunk)) for chunk in utils.chunks(ip, 8))

