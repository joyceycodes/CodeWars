// Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

// Note: input will never be an empty string

//My solution
function fakeBin(x) {
    //returns a string with all 0s and 1s
    let result = '';
    for(let i = 0; i < x.length; i++){
        if (num(x[i]) < 5){
            result += 0;
        } else {
            result += 1;
        }
    }
    return result;
}

//Top solution
function fakeBin(x) {
    //splits string into list
    //uses map to create a new list
    //ternary operator to return 0 if n < 5, else return 1
    //join list into string
    return x.split('').map(n => n < 5 ? 0 : 1).join('');
}