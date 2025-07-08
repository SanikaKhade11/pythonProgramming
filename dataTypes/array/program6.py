# 2. check for duplication
def contains_duplication(nums):
    pass
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                print(f"Duplicate found: {nums[i]}")
                return True
    print("No duplicates found") 
    return False

nums1=[1,2,3,1]
nums2=[1,2,3,4]

print(contains_duplication(nums1))
print(contains_duplication(nums2))
