// Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

// Examples input/output:

// XO("ooxx") => true
// XO("xooxx") => false
// XO("ooxXm") => true
// XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
// XO("zzoo") => false

// my solution
function XO(str) {
    //code here
  let dict = {"x":0, "o": 0}
  for(let i = 0; i < str.length; i++){

    const string = str.toLowerCase()
    if(string[i]==="o"){
      dict["o"] ++
    }
    if(string[i]==="x"){
      dict["x"] ++
    }
  }

  return (dict["x"]===dict["o"]) 
}

// top solution
// this solution uses the .match() method with regex, searching for 'x', 'gi' = global (searching for all cases) and case insensitive
function XO(str) {
    let x = str.match(/x/gi);
    let o = str.match(/o/gi);

    // we need to check for x and x.length for the edge case that there are no exes, x would be null and would not have a length property, causing an error
    // if x is null (falsy), it won't even evaluate the right hand of the expression (x.length)
    return (x && x.length) === (o && o.length);
  }