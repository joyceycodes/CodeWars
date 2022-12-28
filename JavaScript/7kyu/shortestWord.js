// Simple, given a string of words, return the length of the shortest word(s).

// String will never be empty and you do not need to account for different data types.

// my solution
function findShort(s){
    const lst = s.split(' ')
    let shortest = lst[0].length
    lst.forEach(function(e) {
      if(e.length < shortest){
        shortest = e.length
      }
    })
    return shortest
  }

// top solution
function findShort(s){
    return Math.min.apply(null, s.split(' ').map(w => w.length));
  }

