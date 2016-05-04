/**
Training JS #9:
loop statement --while and do..while
If you want your code to do a lot of similar work, loop statement is a good choice. For example, if we need to calculate the cumulative value from 1 to 10, we can write code like this:

function sum1_10(){
  return 1+2+3+4+5+6+7+8+9+10;
}
Wow~~,looks very cool! But if we need to calculate the cumulative value from 1 to 100, the code became:

function sum1_100(){
  return 1+2+3+4+5+6+7+8+9+10+11+12+13+14+15+16+17+18+19+20+21+22+23+24+25
  +26+27+28+29+30+31+32+33+34+35+36+37+38+39+40+41+42+43+44+45+46+47+48+49+50
  +51+52+53+54+55+56+57+58+59+60+61+62+63+64+65+66+67+68+69+70+71+72+73+74+75
  +76+77+78+79+80+81+82+83+84+85+86+87+88+89+90+91+92+93+94+95+96+97+98+99+100;
}
Do you feel a bit tired? So we can use a loop statement do it:

function sum1_100(){
  var sum=0,num=1;    //Initialize two variable sum and num
  while (num<=100){   //Determine the expression in brackets, while true, 
                      //run the code block one time, while false, break the loop
    sum=sum+num;      //Each time sum will add the current value of the num
                      //It can be simplified as:  sum+=num
    num=num+1;        //Each time the value of num increased by 1
                      //It can be simplified as:  num++
  }
  return sum;         //return the final cumulative value
}
The do..while is a variant of while, the example above can write like this:

function sum1_100(){
  var sum=0,num=1;
  do{
    sum+=num;
    num++;
  }while (num<=100)
  return sum;
}
Their difference is, while judge condition before code execution, do..while judge condition after code run one time.
Finally, it is worth mentioning: Do not forget to change the value of the variable (for conditional expressions), 
otherwise it will turn into an infinite loop.Ok, lesson is over, let us do some task with while.

Task

Coding in function padIt, function accept 2 parameters:
1.str, it's a string, we need pad some "*" at leftside or rightside of str
2.n, it's a number, means the times of pad.
method of pad: you need write a loop statement, loop n times. first time pad a "*" at leftside of str, 
second time pad a "*" at rightside of str, and so on...return the finally string.
*/

function padIt(str,n){
  var i=1;
  var x=str;
  do{
     if(i%2==0){
       x=x.concat('*');
       i++;
     }else{
       x='*'.concat(x);
       i++
     }
  }while(i<=n)
  return x;
}