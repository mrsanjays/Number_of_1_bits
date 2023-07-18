def Number_of_1_bits(num):
    cnt=0
    while num:
        cnt+=num&1
        num >>= 1
    return cnt
"""
Write a function that takes an integer and returns the number of 1 bits present in its binary representation.
"""
if __name__ == '__main__':
    num=int(input())
    print(Number_of_1_bits(num))