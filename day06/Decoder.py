class Decoder:
    def __init__ (self):
        pass
    
    def getPacketMarkerPosition(self, msg: str) -> int:
        """ 
        In the protocol being used by the Elves, 
        the start of a packet is indicated by a sequence of four characters that are all different. 
        This function returns the position of the first one
        """
        print(msg)
        first_marker_pos = -1
        # map char -> index_in_string
        unique_map = {}
        
        for i in range(0, len(msg)):
            unique_map[msg[i]] = i
            if i >= 4 and msg[i-4] in unique_map and unique_map[msg[i-4]] <= i-4:
                del unique_map[msg[i-4]] # keep only last 4 chars. deleting 5th

            if len(unique_map) == 4:
                first_marker_pos = i + 1 # elves doesn't count from zero  
                break

        return first_marker_pos
