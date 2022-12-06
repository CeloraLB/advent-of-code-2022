from unittest import TestCase
from day06.Decoder import Decoder

class TryTesting(TestCase):
    def test_detect_packet_marker_with_msg_1(self):
        decoder = Decoder()
        msg = 'bvwbjplbgvbhsrlpgdmjqwftvncz'
        marker_position = decoder.getPacketMarkerPosition(msg)
        self.assertEqual(5, marker_position)

    def test_detect_packet_marker_with_msg_2(self):
        decoder = Decoder()
        msg = 'nppdvjthqldpwncqszvftbrmjlhg'
        marker_position = decoder.getPacketMarkerPosition(msg)
        self.assertEqual(6, marker_position)

    def test_detect_packet_marker_with_msg_3(self):
        decoder = Decoder()
        msg = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'
        marker_position = decoder.getPacketMarkerPosition(msg)
        self.assertEqual(10, marker_position)

    def test_detect_packet_marker_with_msg_4(self):
        decoder = Decoder()
        msg = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'
        marker_position = decoder.getPacketMarkerPosition(msg)
        self.assertEqual(11, marker_position)
