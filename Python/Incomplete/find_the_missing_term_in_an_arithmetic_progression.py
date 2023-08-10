# https://www.codewars.com/kata/52de553ebb55d1fca3000371/

def find_missing(nums):
        nums.sort()
        longest_seq = 1
        curr_seq = 1
        for i in range(1,len(nums)):
            # start of seq
            if nums[i] - nums[i-1] == 1:
                curr_seq += 1
                while curr_seq+i < len(nums) and nums[i] + curr_seq == nums[i+curr_seq]:
                    curr_seq += 1
                longest_seq = max(longest_seq, curr_seq) 
            curr_seq = 1
        return longest_seq 
    
print(find_missing([100,4,200,1,3,2]))