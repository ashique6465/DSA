class Solution:
    def findKthLargest(self,nums:List[int], k:int) ->int:
        k = len(nums) - k

        def quickSelect(l,r):
            pivot, P = nums[r],l
            for i in range(l,r):
                if nums[i] <= pivot:
                    nums[P], nums[i] = nums[i],nums[p]
                    P +=1
            nums[P],nums[r] = nums[r], nums[P]

            if P>k:    return quickSelect(l,P-1)
            elif P<k:  return quickSelect(P+1,r)
            else:      return nums[P]

        return quickSelect(0, len(nums)-1)

            
            