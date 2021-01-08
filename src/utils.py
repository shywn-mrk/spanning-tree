# from math import sqrt

def get_termials_info():
    while True:
        try:
            terminals_freqeuncy = int(input('How many terminals we have? '))

            points = []
            for i in range(terminals_freqeuncy):
                x = int(input(f'Enter the X of the terminal number {i + 1}: '))
                y = int(input(f'Enter the Y of the terminal number {i + 1}: '))

                points.append((x, y))

            return points
        except ValueError:
            print('Values must be integer')


# def get_adjacency_matrix(points):
#     length = len(points)

#     if length <= 2:
#         print('Number of points must be more than 2!')
#         return None

#     adjacency_matrix = []
#     for src in range(length - 1):
#         dst = src + 1
#         for _ in range(src, length - 1):
#             x_distance = (points[src][0] - points[dst][0])
#             y_distance = (points[src][1] - points[dst][1])
#             distance = sqrt(x_distance ** 2 + y_distance ** 2)

#             adjacency_matrix.append((
#                 src,
#                 dst,
#                 distance
#             ))

#             dst += 1

#     return adjacency_matrix
