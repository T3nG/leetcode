var threeSum = function(nums) {
  let result = []
  let negatives = []
  let positives = []
  let zero_count = 0
    
  // 1. split positive, negative and count zero
  nums.forEach(num => {
    if (num > 0) positives.push(num)
    else if (num < 0) negatives.push(num)
    else zero_count += 1
  })
  
  // 2. create a unique array for each of the positives and negatives
  let uPos = [...new Set(positives)]
  let uNeg = [...new Set(negatives)]
 
  // 3. if zero in nums, check cases where -num + num = 0
  if (zero_count > 0) {
    uPos.forEach(num => {
      if (uNeg.includes(-num)) result.push([-num, 0 , num])
    })
  }
  
  // 4. push case where at least 3 zeros in nums
  if (zero_count >= 3) result.push([0,0,0])
  
  // 5. for all pairs of negatives, check if their complement exist in uPos, [-1,-2][3]
  negatives.forEach((neg, i) => {
    let j = i
    while (j+1 < negatives.length){
      let complement = -(neg + negatives[j+1])
      if (uPos.includes(complement)) {
        result.push([neg, negatives[j+1], complement].sort())
      }
      j += 1
    }
  })
  
  // 6. for all pairs of positives, check if their complement exist in uNeg, [1,2][-3]
  positives.forEach((pos, i) => {
    let j = i
    while (j+1 < positives.length){
      let complement = -(pos + positives[j+1])
      if (uNeg.includes(complement)) {
        result.push([pos, positives[j+1], complement].sort())
      }
      j += 1
    }
  })

  let uniqueResult = []
  result.forEach(arr => {
    if (!uniqueResult.some(element => JSON.stringify(element) === JSON.stringify(arr)))
      uniqueResult.push(arr)
  })
  return uniqueResult
}
