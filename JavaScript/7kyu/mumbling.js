// This time no story, no theory. The examples below show you how to write function accum:

// Examples:
// accum("abcd") -> "A-Bb-Ccc-Dddd"
// accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
// accum("cwAt") -> "C-Ww-Aaa-Tttt"
// The parameter of accum is a string which includes only letters from a..z and A..Z.

// my solution
function accum(s) {
	// your code
  let result = s[0]
  for(let i = 1; i < s.length; i++){
    let accum = s[i].repeat(i+1)
    result += '-' + accum[0].toUpperCase() + accum.substr(1).toLowerCase() 
  }
  return result
}

// top solution
function accum(s) {
	return s.split('').map((c, i) => (c.toUpperCase() + c.toLowerCase().repeat(i))).join('-');
}