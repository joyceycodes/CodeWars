# https://www.codewars.com/kata/52de553ebb55d1fca3000371/

def find_missing(nums):
        sorted_nums = sorted(nums)
        res = []

        for i,e in enumerate(sorted_nums):
            if i > 0 and e == sorted_nums[i-1]:
                continue

            B = A + 1
            C = len(sorted_nums)-1

            while B < C:
                three_sum = sorted_nums[B] + sorted_nums[C] + e
                if three_sum > 0:
                    C -= 1
                elif three_sum < 0:
                    B += 1
                else:
                    res.append([sorted_nums[B], sorted_nums[C], e])
                    B += 1
                    while sorted_nums[B] == sorted_nums[B-1] and B < C:
                        B += 1

        return res
    
print(find_missing([-1,0,1,2,-1,-4]))