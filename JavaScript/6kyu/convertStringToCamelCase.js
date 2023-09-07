// Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.

// Examples
// "the-stealth-warrior" gets converted to "theStealthWarrior"

// "The_Stealth_Warrior" gets converted to "TheStealthWarrior"

// "The_Stealth-Warrior" gets converted to "TheStealthWarrior"

function toCamelCase(str){
    let splitStr = str.split(/-|_/)
    let res = splitStr[0]
    for(let i = 1; i < splitStr.length; i++){
      res += splitStr[i].charAt(0).toUpperCase()
      res += splitStr[i].slice(1)
    }
    return res
  }