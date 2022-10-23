// Trolls are attacking your comment section!

// A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

// Your task is to write a function that takes a string and return a new string with all vowels removed.

// For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

// Note: for this kata y isn't considered a vowel.

// my solution (DIDN'T PASS ALL TESTS)
function disemvowel(str) {
    const vowels = ['a','e','i','o','u'];
    const str1 = str.split('')
    for(let char of str1){
      if(isAlpha(char)) {
       for(let letter of vowels){
         if(char.toLowerCase() ===letter) {
          const index = str1.indexOf(char);
          str1.splice(index,1);
        }
      } 
    }
    }  
    return str1.join('');


//top solution 
function disemvowel(str) {
    return str.replace(/[aeiou]/gi, '');
  }
  // this is solved using regex, or regular expressions
  // it's used to perform matches in strings 
  // looks for a match of /[aeiou]/