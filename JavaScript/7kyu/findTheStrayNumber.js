// You are given an odd-length array of integers, in which all of them are the same, except for one single number.

// Complete the method which accepts such an array, and returns that single different number.

// The input array will always be valid! (odd-length >= 3)

// Examples
// [1, 1, 2] ==> 2
// [17, 17, 3, 17, 17, 17, 17] ==> 3

function stray(numbers) {
    let count = {}
    for (let i = 0; i < numbers.length; i++){
      if (!(numbers[i] in count)){
        count[numbers[i]] = 0
      }
      count[numbers[i]] += 1
    }
    
    for ([key,value] of Object.entries(count)){
      if (value === 1){
        return Number(key)
      }
    }
  }

// top solution
function stray(numbers){
    for (var i in numbers){
       if (numbers.indexOf(numbers[i]) === numbers.lastIndexOf(numbers[i])){return numbers[i]}
    }
}

function stray(numbers) {
    var a = numbers.sort();
    
    if(a[0] != a[1]) {
      return a[0]
    } 
    return a[a.length-1]
  }