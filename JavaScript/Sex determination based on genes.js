function chromosomeCheck(sperm) {
  return (sperm.includes('Y')?"Congratulations! You're going to have a son."
  : "Congratulations! You're going to have a daughter.")
}

function chromosomeCheck(sperm) {
  return `Congratulations! You're going to have a ${sperm === 'XY' ? 'son' : 'daughter'}.`
}

function chromosomeCheck(sperm) {
if(sperm == "XY")
{
  return "Congratulations! You're going to have a son.";
}
return "Congratulations! You're going to have a daughter.";
}


function chromosomeCheck(sperm) {
  return "Congratulations! You're going to have a " + (sperm == 'XX' ? 'daughter' : 'son') + '.';
}


chromosomeCheck=s=>`Congratulations! You're going to have a ${s=='XY'?'son':'daughter'}.`


