function century(year) {
  var x= year%100;
  if (x>0){
    return parseInt(year/100)+1
  }
  else return parseInt(year/100);
}


const century = year => Math.ceil(year/100)


function century(year) {
  return (year + 99) / 100 | 0;
}


const century = year => year % 100 === 0 ? parseInt(year / 100) : parseInt(year / 100) + 1;

function century(year) {
  if (year <= 100){
    return 1;
  }

  let cen = parseInt(year / 100);
  let rem = year % 100;
  
  return rem === 0 ? cen : cen + 1;
}


function century(year) {
  var century = 0;
  
  for(var i = 0; i < year; i++) {
    if(i % 100 == 0) {
      century++;
    }
  }
  return century;
}