// Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

// moveZeros([false,1,0,1,2,0,1,3,"a"]) // returns[false,1,1,2,1,3,"a",0,0]

function moveZeros(arr) {
    let result = []
    let zeros_count = 0
    for(let i = 0; i < arr.length; i++){
      if(arr[i] === 0){
        zeros_count += 1
      } else{
        result.push(arr[i])
      }
    }
    let zeroes = Array(zeros_count).fill(0)
    return result.concat(zeroes)
  
  }

// top solution
var moveZeros = function (arr) {
    var filtedList = arr.filter(function (num){return num !== 0;});
    var zeroList = arr.filter(function (num){return num === 0;});
    return filtedList.concat(zeroList);
  }