// Find the number with the most digits.

// If two numbers in the argument array have the same number of digits, return the first one in the array.

function findLongest(array){
    max_length = 0
    max_value = 0
    for(let i = 0; i<array.length; i++){
      if (array[i].toString().length > max_length) {
        max_length = array[i].toString().length
        max_value = array[i]
      }
    }
    return max_value
  }

// top solution
function findLongest(array){
    return array.reduce((res, curr) => (String(res).length < String(curr).length) ? curr : res);
  }