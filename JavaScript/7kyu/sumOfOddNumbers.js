// Given the triangle of consecutive odd numbers:

//              1
//           3     5
//        7     9    11
//    13    15    17    19
// 21    23    25    27    29
// ...
// Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)

// 1 -->  1
// 2 --> 3 + 5 = 8

function rowSumOddNumbers(n) {
    let odds = []
  curr_num = 1
  for(let i = 0; i < n+1; i++){
    let row = []
    while (row.length < i){
      row.push(curr_num)
      curr_num += 2
    }
    odds.push(row)
  }
  return (odds[n].reduce((a,e)=> a + e, 0))
}


function rowSumOddNumbers(n) {
    return Math.pow(n, 3);
  }