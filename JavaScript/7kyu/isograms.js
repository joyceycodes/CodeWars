// An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

// Example: (Input --> Output)

// "Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)

// isIsogram "Dermatoglyphics" = true
// isIsogram "moose" = false
// isIsogram "aba" = false

function isIsogram(str){
    str = str.toLowerCase()
    let count = {}
    for(let i = 0; i < str.length; i++){
      if (!(str[i] in count)){
        count[str[i]] = 0
      } 
      count[str[i]] += 1
      if(count[str[i]] > 1){
        return false
      } 
    }
     return true
  }

// top solution
function isIsogram(str){
    return new Set(str.toUpperCase()).size == str.length;
}