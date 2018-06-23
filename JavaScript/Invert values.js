function invert(array) {
   var sol=[]
   for(i=0;i<array.length;i++){
     if(array[i]!=0)
       sol[i]=array[i]*-1;
      else
        sol[i]=array[i]
   }
   return sol;
}