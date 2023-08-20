// Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

// It should remove all values from list a, which are present in list b keeping their order.

// arrayDiff([1,2],[1]) == [2]
// If a value is present in b, all of its occurrences must be removed from the other:

// arrayDiff([1,2,2,2,3],[2]) == [1,3]

function arrayDiff(a, b) {
    let res = []
    let hash = {}
    for(let i = 0; i < b.length; i++){
      hash[b[i]] = 0
    }
    for(let j = 0; j < a.length; j++){
      if(!(a[j] in hash)){
        res.push(a[j])
      }
    }
    return res
  }

// top solution  
function array_diff(a, b) {
    return a.filter(e => !b.includes(e));
}