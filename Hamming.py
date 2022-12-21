import numpy as np
import random


# def hamming_d():
#     print("D Tier")
#     G = [[1, 1, 0, 1], [1, 0, 1, 1], [1, 0, 0, 0], [0, 1, 1, 1], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
#
#     H = [[1, 0, 1, 0, 1, 0, 1], [0, 1, 1, 0, 0, 1, 1], [0, 0, 0, 1, 1, 1, 1]]
#
#     R = [[0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1]]
#
#     p = np.array([[1], [0], [1], [1]])
#
#     print("Message (p): ", p.flatten())
#
#     x = np.matmul(G, p)
#     x = x % 2
#
#     print("Send vector (x): ", x.flatten())
#
#     r = x.copy()
#     print("Received Message (r): ", r.flatten())
#
#     z = np.matmul(H, r)
#     z = z % 2
#
#     print("Parity Check (z): ", z.flatten())
#
#     r = [[0], [1], [1], [0], [1], [1], [1]]
#     z = np.matmul(H, r)
#     z = z % 2
#     # print(z)
#
#
# def hamming_c():
#     print("C Tier")
#     G = [[1, 1, 0, 1], [1, 0, 1, 1], [1, 0, 0, 0], [0, 1, 1, 1], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
#
#     H = [[1, 0, 1, 0, 1, 0, 1], [0, 1, 1, 0, 0, 1, 1], [0, 0, 0, 1, 1, 1, 1]]
#
#     R = [[0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1]]
#
#     p = np.random.randint(0, 2, (4, 1))
#     print("Message: ", p.flatten())
#
#     x = np.matmul(G, p)
#     x = x % 2
#     print("Send vector: ", x.flatten())
#
#     random_bit = random.randint(0, 7)
#
#     e = np.zeros((7, 1), dtype=int)
#     if random_bit > 0:
#         e[random_bit - 1] = 1
#
#     r = x + e
#     r = r % 2
#     print("Received Message: ", r.flatten())
#
#     z = np.matmul(H, r)
#     z = z % 2
#     print("Parity Check: ", z.flatten())
#
#     sum = 0
#     for arr in range(z.size):
#         sum += int(pow(2, arr) * z[arr])
#
#     if sum > 0:
#         if r[sum - 1] == 1:
#             r[sum - 1] = 0
#         else:
#             r[sum - 1] = 1
#
#     print("Corrected Message: ", r.flatten())
#
#     pr = np.matmul(R, r)
#     print("Decoded Message: ", pr.flatten())
#
#
# def hamming_b():
#     print("B Tier")
#     print("Enter Mode: ")
#     version = input()
#
#     if version == 'H1511':
#         G = [[1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
#              [1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1],
#              [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#              [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
#              [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#              [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#              [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
#              [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
#              [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
#              [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#              [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
#              [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
#              [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
#              [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
#              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]
#
#         H = [[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
#              [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
#              [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
#              [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]]
#
#         R = [[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#              [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#              [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#              [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#              [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
#              [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
#              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
#              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
#              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
#              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]
#
#         p = np.random.randint(0, 2, (11, 1))
#         print("Message: ", p.flatten())
#
#         x = np.matmul(G, p)
#         x = x % 2
#         print("Send vector: ", x.flatten())
#
#         random_bit = random.randint(0, 15)
#
#         e = np.zeros((15, 1), dtype=int)
#         if random_bit > 0:
#             e[random_bit - 1] = 1
#
#         r = x + e
#         r = r % 2
#         print("Received Message: ", r.flatten())
#
#         z = np.matmul(H, r)
#         z = z % 2
#         print("Parity Check: ", z.flatten())
#
#         adding = 0
#         for arr in range(z.size):
#             adding += int(pow(2, arr) * z[arr])
#
#         if adding > 0:
#             if r[adding - 1] == 1:
#                 r[adding - 1] = 0
#             else:
#                 r[adding - 1] = 1
#
#         print("Corrected Message: ", r.flatten())
#
#         pr = np.matmul(R, r)
#         print("Decoded Message: ", pr.flatten())
#
#     else:
#         hamming_c()


def hamming_a():
    """
    It takes the number of data bits, calculates the number of parity bits, creates the H and G matrices, creates the
    message, encodes it, adds an error, decodes it, and prints the results
    """
    print("Tier A")
    print("Enter number of databits: ")
    data_bits = int(input())
    parity_bits = num_of_parity(data_bits)
    total_bits = parity_bits + data_bits
    h_row_col = (parity_bits, total_bits)
    h_array = np.zeros(h_row_col).astype(int)

    for h_row_index in range(parity_bits):
        for h_col_index in range(total_bits):
            if pow(2, h_row_index) == (h_col_index + 1) & pow(2, h_row_index):
                h_array[h_row_index][h_col_index] = 1

    dummy_array = h_array
    for col in range(total_bits, 0, -1):
        if is_pow_of_two(col):
            dummy_array = np.delete(dummy_array, col - 1, 1)

    g_row_col = (total_bits, data_bits)
    g_array = np.zeros(g_row_col).astype(int)
    g_identity = np.identity(data_bits).astype(int)
    g_identity_row = 0
    dummy_row = 0

    for g_row in range(total_bits):
        if is_pow_of_two(g_row + 1) and dummy_row < parity_bits:
            g_array[g_row] = dummy_array[dummy_row]
            dummy_row += 1
        else:
            g_array[g_row] = g_identity[g_identity_row]
            g_identity_row += 1

    r_row_col = (total_bits, data_bits)
    r_array = np.zeros(r_row_col).astype(int)
    r_identity = np.identity(data_bits).astype(int)
    r_identity_row = 0
    for r_row in range(total_bits):
        if not is_pow_of_two(r_row + 1):
            r_array[r_row] = r_identity[r_identity_row]
            r_identity_row += 1

    r_array = r_array.transpose()

    p = np.random.randint(0, 2, (data_bits, 1))
    print("Message: ", p.flatten())

    x = np.matmul(g_array, p)
    x = x % 2
    print("Send vector: ", x.flatten())

    random_bit = random.randint(0, total_bits)
    e = np.zeros((total_bits, 1), dtype=int)
    if random_bit > 0:
        e[random_bit - 1] = 1

    r = x + e
    r = r % 2
    print("Received Message: ", r.flatten())

    z = np.matmul(h_array, r)
    z = z % 2
    print("Parity Check: ", z.flatten())

    summation = 0
    for arr in range(z.size):
        summation += int(pow(2, arr) * z[arr])

    if summation > 0:
        if r[summation - 1] == 1:
            r[summation - 1] = 0
        else:
            r[summation - 1] = 1

    print("Corrected Message: ", r.flatten())

    pr = np.matmul(r_array, r)
    print("Decoded Message: ", pr.flatten())


def num_of_parity(data_bits) -> int:
    """
    It counts the number of parity bits needed for a given number of data bits

    :param data_bits: the number of data bits in the message
    :return: The number of parity bits needed for the given number of data bits.
    """
    count = 0
    while data_bits + count >= pow(2, count):
        count += 1
    return count


def is_pow_of_two(num) -> bool:
    """
    If the number is a power of two, return True.

    :param num: The number to check if it's a power of two
    :return: True or False
    """
    i = 0
    for i in range(num):
        if num == pow(2, i):
            return True


if __name__ == '__main__':
    # hamming_d()
    # print(">>> main")
    # hamming_c()
    # print(">>> main")
    # hamming_b()
    # print(">> main")
    hamming_a()
    print(">> main")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
