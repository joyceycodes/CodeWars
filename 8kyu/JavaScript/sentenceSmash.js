// Write a function that takes an array of words and smashes them together into a sentence and returns the sentence. You can ignore any need to sanitize words or add punctuation, but you should add spaces between each word. Be careful, there shouldn't be a space at the beginning or the end of the sentence!

// Example
// ['hello', 'world', 'this', 'is', 'great']  =>  'hello world this is great'


// my solution 
function smash (words) {
    sentence = words[0]
    if (words.length == 0){
      return '';
    }
    for (let i = 1; i < words.length ; i++){
      sentence += ' ' + words[i];
    }
    return sentence;
  };


// top solution
smash = function (words) {
    return words.join(" ");
  };