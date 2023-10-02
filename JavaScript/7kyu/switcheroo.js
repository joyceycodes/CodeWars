// Given a string made up of letters a, b, and/or c, switch the position of letters a and b (change a to b and vice versa). Leave any incidence of c untouched.

// Example:

// 'acb' --> 'bca'
// 'aabacbaa' --> 'bbabcabb'

function switcheroo(x){
  let res = ''
  for(let i = 0; i < x.length; i++){
    if(x[i] === 'a'){
      res += 'b'
    } else if(x[i] === 'b'){
      res += 'a'
    } else {
      res += x[i]
    }
  }
  return res
}

//top solution
const switcheroo=x=>x.replace(/[ab]/g,x=>x=="a"?"b":"a")

function switcheroo(x){
  return x.split('').map(function(e){
    if (e =='b')return 'a';
    if (e == 'a') return 'b';
    if(e=='c') return 'c'
  }).join('');
}
