def encode_rail_fence_cipher(string, n):
    result = [[] for i in range(n)]
    for index, char in enumerate(string):
        index = index % (2 * (n-1))
        if index > n - 1:
            index = 2 * (n-1) - index
        result[index].append(char)
    return ''.join(''.join(rail) for rail in result)
    
def decode_rail_fence_cipher(string, n):
    return None
