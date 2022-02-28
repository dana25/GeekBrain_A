class Road:

    def __init__(self, length, width):
        self._length = length
        self._wigth = width

    def profit(self, weight=10, thickness=0.1):
        return f"{self._length} m *{self._wigth} m *{weight} kg *{thickness} m =" \
                f"{(self._length *self._wigth*weight * thickness)/1000} t"

road_1 = Road(100, 2)
print(road_1.profit())