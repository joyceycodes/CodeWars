// Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

// Example
// "abcde" -> 0 # no characters repeats more than once
// "aabbcde" -> 2 # 'a' and 'b'
// "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
// "indivisibility" -> 1 # 'i' occurs six times
// "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
// "aA11" -> 2 # 'a' and '1'
// "ABBA" -> 2 # 'A' and 'B' each occur twice


function duplicateCount(txt){
    count = {}
    let lower_text = txt.toLowerCase()
    for(let i = 0; i < txt.length; i++){
      if(!(lower_text[i] in count)){
        count[lower_text[i]] = 0
      }
      count[lower_text[i]] += 1
    }
    let distinct = 0
    for(let i = 0; i< Object.values(count).length; i++){
      if(Object.values(count)[i] > 1){
        distinct += 1
      }
    }
    return distinct
  }