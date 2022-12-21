import os
import sys

from GPS import GPS

def main():
    if len(sys.argv) <= 1 or sys.argv[1] == None:
        sys.exit('need a secret message as first param')
    input_file = open(sys.argv[1], 'r')
    enc_coordinates = input_file.read().splitlines()
    enc_coordinates = [int(x) for x in enc_coordinates]
    
    gps = GPS()
    dec_coordinates = gps.decryptCoordinates(enc_coordinates)
    sum_coordinates = gps.getSumCoordinates(dec_coordinates)
    print('sum of the coordinates is {}'.format(sum_coordinates))

if __name__ == '__main__':
    main()