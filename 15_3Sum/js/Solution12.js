var threeSum = function(nums){
  nums.sort((a,b) => a-b)
  const output = []
  const target_sum = 0
  const count = nums.length;
  for (let i=0; i<count-2; i++){
    if (nums[i] > 0) break
    if(nums[i] === nums[i-1]) continue
    let j = i + 1
    let k = count - 1
    if(count < 3) return output
    while (j<k){
      const nSum = nums[i]+nums[j]+nums[k]
      if (nSum < 0) j += 1
      else if (nSum > 0) k -= 1
      else{
        output.push([nums[i], nums[j], nums[k]])
        while (j < k && nums[j] === nums[j + 1]) j += 1
        while (j < k && nums[k] === nums[k - 1]) k -= 1
        j += 1
        k -= 1
      }
    }
  }
  return output
}