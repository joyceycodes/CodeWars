// Given a string of words, you need to find the highest scoring word.

// Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

// For example, the score of abad is 8 (1 + 2 + 1 + 4).

// You need to return the highest scoring word as a string.

// If two words score the same, return the word that appears earliest in the original string.

// All letters will be lowercase and all inputs will be valid.

function high(x){
    let highest = 0
    let word = ''
    let words = x.toLowerCase().split(' ')
    for(let i =0; i < words.length; i++){
      sum = 0
      for(let j = 0; j < words[i].length; j++){
        sum += words[i][j].charCodeAt(0)-96
      }
      if(sum > highest){
        highest = sum
        word = words[i]
      }
    }
    return word
  }

// top solution
function high(s){
    let as = s.split(' ').map(s=>[...s].reduce((a,b)=>a+b.charCodeAt(0)-96,0));
    return s.split(' ')[as.indexOf(Math.max(...as))];
  }
  