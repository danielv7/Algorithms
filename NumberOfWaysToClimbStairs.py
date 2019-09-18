#Number of ways to climb stairs

#Time: O(n) Space: O(1)
def climbstairs(n):
  if n == 0 or n == 1:
    return 1
  nums = [0] * (n + 1)
  nums[0] = 1
  nums[1] = 1
  for i in range(2, n + 1):
    nums[i] = nums[i - 1] + nums[i - 2]
  return nums[n]
