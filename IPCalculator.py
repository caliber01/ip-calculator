from BitVector import BitVector
from math import log, ceil
from IPAddress import IPAddress


class IPCalculator:
    @staticmethod
    def split_into_subnets(ip_address, number_of_networks):
        power_of_two = ceil(log(number_of_networks, 2))
        mask = ip_address.mask + power_of_two
        if mask >= 32:
            raise Exception('too many networks')
        addresses = [ip_address.ip_bin[:ip_address.mask] +
                     BitVector(intVal=i, size=power_of_two) +
                     BitVector(bitstring='0' * (32 - (power_of_two + ip_address.mask)))
                     for i in range(number_of_networks)]
        return [IPAddress(bit_vector=address, mask=mask) for address in addresses]
