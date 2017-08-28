#!/usr/bin/env python

import sys

class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sets = [set() for i in range(0, len(nums))]
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0:
                    sets[i].add(nums[j])
            print sets[i]
        return list(set.intersection(*sets))

def stringToIntegerList(input):
    input = input.strip()
    input = input[1:-1]
    return [int(number) for number in input.split(",")]

def integerListToString(nums, len_of_list=None):
    result = ""
    if not len_of_list:
        len_of_list = len(nums)
    for index in range(len_of_list):
        num = nums[index]
        result += str(num) + ", "
    return result[:-2]

import sys
def readlines():
    for line in sys.stdin:
        yield line.strip('\n')

def main():
    lines = readlines()
    while True:
        try:
            line = lines.next()
            nums = stringToIntegerList(line)

            ret = Solution().largestDivisibleSubset(nums)

            out = integerListToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()
