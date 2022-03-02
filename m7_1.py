class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return '/n'.join('/t'.join([f"{itm:03}" for itm in line]) for line in self.data)

    def __add__(self, other):
        try:
            m=[[int(self.data[line][itm])+int(other.data[line][itm]) for itm in range(len(self.data[line]))]
                for line in range(len(self.data))]
            return Matrix(m)
        except IndexError:
            return f'Error matrix size'

m_1=[[1,2,3], [4,5,6], [7,8,9]]
m_2= [[11, 22,33], [44,55,66], [77,88,99]]

matrix_1=Matrix(m_1)
matrix_2=Matrix(m_2)
sum_m=matrix_1+matrix_2
print(sum_m)