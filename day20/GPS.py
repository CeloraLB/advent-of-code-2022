class GPS():

    def __init__(self):
        pass
        
    def decryptCoordinates(self, enc_coordinates: list) -> list:
        coordinates = []
        decrypted_coordinate = []
        n = len(enc_coordinates)

        for i in range(n):
            coordinates.append((i, enc_coordinates[i]))

        for i in range(n):
            if coordinates[i] == 0:
                continue
            coordinates = self._doStep(coordinates, i)
            decrypted_coordinate = self._composeListFromCoordinates(coordinates)

        return decrypted_coordinate

    def _doStep(self, coordinates: list, i: int) -> list:
        n = len(coordinates)
        index, value = coordinates[i]
        new_index = index + value
        fw_or_bw = -1
        if value < 0:
            # new_index = (new_index-1) % n
            new_index = new_index % (n-1)
        elif new_index >= n:
            fw_or_bw = 1
            # new_index = (new_index+1) % n
            new_index = new_index % (n-1)

        for j in range(n):
            c_index, c_value = coordinates[j]                
            if i != j and min(index, new_index) <= c_index <= max(index, new_index):
                c_index += fw_or_bw

            coordinates[j] = (c_index % n, c_value)     
        coordinates[i] = (new_index % n, value)
        return coordinates

    def _composeListFromCoordinates(self, coordinates: list) -> list:
        l = [0 for x in range(len(coordinates))]
        for c in coordinates:
            index, value = c
            l[index] = value

        return l

    def getSumCoordinates(self, decrypted_coordinate: list) -> int:
        n = len(decrypted_coordinate)
        start = decrypted_coordinate.index(0)
        return sum([decrypted_coordinate[(start+1000) % n], decrypted_coordinate[(start+2000) % n], decrypted_coordinate[(start+3000) % n]])