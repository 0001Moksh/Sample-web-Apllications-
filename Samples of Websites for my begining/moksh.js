
// document.write("this is a document write");
// console.log("hello world");
// // alert("this is an alert");
// console.warn("this is an waring");
// console.error("this is an error");

// var a=23;
// var b=99;
// console.log(a+b);
// console.log(a*b);
 
// var c=b;
// c*=10;
// console.log(c/b);

// let age = 10;
// if (age>18){
//     console.log("you are above 18");
// }
// else if (age>30) {
//     console.log("you are above 30");
// }
// else if(age>50){
//     console.log("you are above 50");
// }
// else if(age>60){
//     console.log("you are above 60");
// }
// else if(age>70){
//     console.log("you are above 70");
// }
// else if(age>80){
//     console.log("tou are above 80");
// }
// else if(age>90){
//     console.log("you are above 90");
// }
// else{
//     console.log("you are above 100");
// }

// function avg(a,b)
// {    c=(a+b)/2
//   return c;
// }
// c1=avg(23,3);
// console.log(c1);

// var un;
// console.log(un);
// var un =null;
// console.log(un);

// let x=10;
//     y=20;
// console.log(x==y);
// console.log(x>y);
// console.log(x<y);
// console.log(x>=y);
// console.log(x<=y);

// console.log(true||false);
// console.log(false||false);
// console.log(false||true);
// console.log(true||true);

// console.log(true&&false);
// console.log(false&&false);
// console.log(true&&true);
// console.log(false&&true);

// console.log(!true);
// console.log(!false);

// let arry =["fan",12,null,true];
// console.log(arry.length);
// arry.pop();
// arry.push("harry");
// arry.unshift("monty");
// arry.shift();
// console.log(arry);

// let mylovelystring="moksh is a good boy good good moksh";
// console.log(mylovelystring.length);
// console.log(mylovelystring.indexOf("good"));
// console.log(mylovelystring.lastIndexOf("good"));
// d=mylovelystring.replace("moksh","harry");
// console.log(d,mylovelystring);

// // let mydate= new Date()
// // console.log(mydate.getUTCDate());
// // let elemclass = document.getElementsByClassName("container");
// //   console.log(elemclass);
// // console.log();
// // let elemclass =document.getElementsByClassName('container');
// // elemclass[0].classList.add("bg-primary");
// // let live_ka_tora=document.getElementsByClassName('container');
// // live_ka_tora[0].classList.add('text_success');
// // console.log('selecting query');
// // sel1 =document.querySelector('.container');
// // sel2=document.querySelectorAll('.container');
// // console.log(sel1,sel2);

// tn=document.getElementsByTagName('div');
// console.log(tn);
// createdElement=document.createElement('p');
// createdElement.innerText='this is a created para';
// tn[0].appendChild(createdElement);
// createdElement2=document.createElement('b');
// createdElement2.innerText="this is a created bold";
// tn[0].replaceChild(createdElement2,createdElement);

// function clicked(){
//     console.log("the button was clicked by you bro ")
// };
// window.onload=function(){
//     console.log('the document is loaded')};

// firstcontainer.addEventListener('click', function(){
//     console.log("mouse on container")
// });

// firstcontainer.addEventListener('mouseover',function(){
//     console.log("mouse over (means mouse container per aya)")
// });
// firstcontainer.addEventListener('mouseout',function(){
//     console.log("mouse out(means mouse container se gya)")
// });
// firstcontainer.addEventListener('mousedown',function(){
//     console.log("mouse down (means mouse container per click kiya)")
// });
// firstcontainer.addEventListener('mouseup',function(){
//     console.log("mouse up(means mouse container per se click htaya)")
// });

// firstcontainer.addEventListener('click', function(){
//     document.querySelectorAll('.container')[1].innerHTML="we have clicked"
//     console.log("clicked on container")
// });

// let preHTML=document.querySelectorAll('.container')[1].innerHTML;
// firstcontainer.addEventListener('mouseup',function(){
//     document.querySelectorAll('.container')[1].innerHTML=preHTML;
//       console.log("mouse up ");
// })
firstcontainer.addEventListener('click',function(){
    document.querySelectorAll('.container')[1].innerHTML="<b>we have clicked</b>"
    console.log("mousedown")
})


// let a;
// let date;
// let time;
// setInterval(()=>{
//  let   a = new Date();
//     date =a.toLocaleDateString();
//     time=a.getHours()+':'+ a.getMinutes()+':'a.getSeconds();
//     document.getElementById('time').innerHTML=time+"on"+date;
// },1000);

// function summ(a,b) 
// {
//    return a+b;
// };

// summ =(a,b)=>{
//     return a+b
// };

// logkro =()=>{
//     document.querySelectorAll(".container")[1].innerHTML="this is caused by set interval in every second";
//     console.log("i am log")
// }
// // setTimeout(logkro,2000);
// clr=setInterval(logkro,1000)




