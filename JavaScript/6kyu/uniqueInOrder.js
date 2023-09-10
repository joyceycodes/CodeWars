// Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

// For example:

// uniqueInOrder('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
// uniqueInOrder('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
// uniqueInOrder([1,2,2,3,3])       == [1,2,3]

var uniqueInOrder=function(iterable){
    let unique;
    if (iterable.length > 0){
      unique = [iterable[0]]
    } else {
      return []
    }
   for(let i = 1; i < iterable.length; i++){
     if(iterable[i] !== unique[unique.length - 1]){
       unique.push(iterable[i])
     }
   }
    return unique
  }

// top solution
var uniqueInOrder=function(iterable){
    return [...iterable].filter((a, i) => a !== iterable[i-1])
}