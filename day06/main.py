import sys
from Decoder import Decoder

def main():
    if len(sys.argv) <= 1 or sys.argv[1] == None:
        sys.exit('need a secret message as first param')
    decoder = Decoder()
    marker_position = decoder.getMessageMarkerPosition(sys.argv[1])
    print('first marker after character {}'.format(marker_position))
    sys.exit()

if __name__ == "__main__":
    main()