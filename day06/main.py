import sys
from Decoder import Decoder

def main():
    if len(sys.argv) <= 1 or sys.argv[1] == None:
        sys.exit('need a secret message as first param')
    decoder = Decoder()
    packet_marker_position = decoder.getPacketMarkerPosition(sys.argv[1])
    message_marker_position = decoder.getMessageMarkerPosition(sys.argv[1])
    print('packet marker after character {}'.format(packet_marker_position))
    print('message marker after character {}'.format(message_marker_position))
    sys.exit()

if __name__ == "__main__":
    main()