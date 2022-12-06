class Decoder:
    def __init__ (self):
        pass
    
    def getPacketMarkerPosition(self, msg: str) -> int:
        """ 
        In the protocol being used by the Elves, 
        the start of a packet is indicated by a sequence of 4 characters that are all different. 
        This function returns the position of the first one
        """
        return self._getMarkerPosition(msg, 4)

    def getMessageMarkerPosition(self, msg: str) -> int:
        """ 
        In the protocol being used by the Elves, 
        the start of a message is indicated by a sequence of 14 characters that are all different. 
        This function returns the position of the first one
        """
        return self._getMarkerPosition(msg, 14)

    def _getMarkerPosition(self, msg: str, n_unique_char: int) -> int:
        first_marker_pos = -1
        # map char -> index_in_string
        unique_map = {}
        
        for i in range(0, len(msg)):
            unique_map[msg[i]] = i
            if( 
                i >= n_unique_char and 
                msg[i-n_unique_char] in unique_map and 
                unique_map[msg[i-n_unique_char]] <= i-n_unique_char
            ):
                del unique_map[msg[i-n_unique_char]] # keep only last n_unique_char chars. deleting 5th

            if len(unique_map) == n_unique_char:
                first_marker_pos = i + 1 # elves doesn't count from zero  
                break

        return first_marker_pos
