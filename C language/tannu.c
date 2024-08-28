// //Calculate the area of rectangle, information taken by user
// #include<stdio.h>
//  int main()
//  {
//     int length,breadth;
//  printf("length of your rectangle:");
//  scanf("%d",&length);
//  printf("breadth of your rectangle: ");
//  scanf("%d",&breadth);
//  printf("Area of your rectangle :%d ", length*breadth );
//  return 0;
//  }

// //Calculate the volume of cyclinder, information taken by user
// #include <stdio.h>
// int main(){
//     int radius,Height;
//     float pi = 3.14;
//     printf("Radius of your cylinder is: ");
//     scanf("%d",&radius);
//     printf("Height of your cylinder is: ");
//     scanf("%d",&Height);
//     printf("Volume of your cylinder is: %f",pi*radius*radius*Height);
//     return 0;
// }

// // Farhrenheit to Celsius
// #include<stdio.h>
//      int main(){
//      float F;
//      printf("Temperature in farenheit :");
//      scanf("%f",&F);
//      printf("Temperture in Celsius %f",(F-32)*5/9);
//      return 0;
// }

// // simple interest
// #include<stdio.h>
//      int main(){
//     int principle, rate, years;
//     printf("principle :");
//     scanf("%d",&principle);
//     printf("Rate :");
//     scanf("%d",&rate);
//     printf("Year :");
//     scanf("%d",&years);
//     printf("Simple interest of given Imformation is :%d",(principle*rate*years)/100);
//      return 0;
// }

// Gusus the Number Game
// #include<stdio.h>
// #include<stdlib.h>
// #include<time.h>
//      int main(){
//           int number, user, guss_num=0;
// srand(time(0));
// number=rand()%100+1;
// printf("%d \n", number);
// printf("___START THE GAME___ \n");
//  printf("Pridiect the number - ");
// while (user>number|| number>user){
// guss_num++;
// scanf("%d",&user);
//  if(user>number){
//      printf("lower Number plz\n");
// }
// else if (user<number){
//      printf("higher Number plz\n");
// }
// else if (user==number){
//      printf("     WELL DONE\n You Gusses the number \nAttempt would be-%d \n" , guss_num);
// }
// else {
//      printf("ERROR");
// }
// }
//      printf("________THE_END____________");
//      return 0;
// }

// // switch case
// #include <stdio.h>
// int main()
// {
//      int date, month, year;
//      printf("Calender\n enter the date: ");
//      scanf("%d", &date);
//      printf("enter the Month: ");
//      scanf("%d", &month);
//      printf("enter the Year: ");
//      scanf("%d", &year);
//      switch (date)
//      {
//      case 1:
//      printf("%d-%d-%d Day-Monday", date, month, year);
//           break;
//      case 2:
//      printf("%d-%d-%d Day-Tuesday", date, month, year);
//           break;
//      case 3:
//      printf("%d-%d-%d Day-Wednesday", date, month, year);
//           break;
//      case 4:
//      printf("%d-%d-%d Day-Thursday", date, month, year);
//           break;
//      case 5:
//      printf("%d-%d-%d Day-Friday", date, month, year);
//           break;
//      case 6:
//      printf("%d-%d-%d Day-Saturday", date, month, year);
//           break;
//      case 7:
//      printf("%d-%d-%d Day-Sunday", date, month, year);
//           break;
//      default:
//           printf("Typing Error");
//           break;
//      }
// }

// calender using ...
// #include<stdio.h>
// date_determiner(int date , int month,int year);
//       int main(){
//  int date, month, year;
// printf("Calender\n enter the date: ");
// scanf("%d", &date);
// printf("enter the Month: ");
// scanf("%d", &month);
// printf("enter the Year: ");
// scanf("%d", &year);
//     date_determiner(int date , int month,int year)
//       return 0;
// }
// date_determiner(int date , int month,int year){
//      int date=28 ;
//      int month=4;
//      int year=2024;
//      if(date>=20){
//           date=date-20;
//      }
//      else if(date>=10){
//           date=date-10;
//      }
//      switch (date)
//      {
//      case 1:
//      printf("%d-%d-%d Day-Monday", date, month, year);
//           break;
//      case 2:
//      printf("%d-%d-%d Day-Tuesday", date, month, year);
//           break;
//      case 3:
//      printf("%d-%d-%d Day-Wednesday", date, month, year);
//           break;
//      case 4:
//      printf("%d-%d-%d Day-Thursday", date, month, year);
//           break;
//      case 5:
//      printf("%d-%d-%d Day-Friday", date, month, year);
//           break;
//      case 6:
//      printf("%d-%d-%d Day-Saturday", date, month, year);
//           break;
//      case 7:
//      printf("%d-%d-%d Day-Sunday", date, month, year);
//           break;
//      default:
//           printf("Typing Error");
//           break;
//      }
// }

// fibonacci series 0 1 1 2 3 5 8 13 21 34
// #include <stdio.h> 
// int fibonacci(int n) { 
//  if (n <= 1) { 
//  return n; 
//  } 
//  else { 
//  return fibonacci(n - 1) + fibonacci(n - 2); 
//  } 
// } 
// int main() { 
//  int num;
//  printf("Enter the steps to print fibonacci : ");
//  scanf("%d",&num);
//  for (int i = 0; i < num; i++) { 
//  printf("%d ", fibonacci(i));
//  } 
//  return 0; 
// } 

// factorial determiner
// #include<stdio.h>
// int factorial(int number){
//     if (number<=1){
//         return number;
//     }
//     else{
//         return number *factorial(number-1);
//     }
// }
// int main(){
//     int num;
//     printf("Enter the Number to find Factorial: \n");
//     scanf("%d",&num);
//     int answer = factorial(num);
//     printf("factorial of %d is %d",num, answer);
//     return 0;
// }

// Practical Question to solve
// #include<stdio.h>
// int main()
// {
//     int a,b,c;
//     printf("Enter the  any three Number: \n");
//     scanf("%d%d%d",&a,&b,&c);
//     if(a>b){
//         printf("First Number is Greater than other, %d ",a);
//     }
//     else if(c>b){
//          printf("Third Number is Greater than other, %d ",c);
//     }
//     else{
//          printf("Second Number is Greater than other, %d ",b);
//     }
//     return 0;
// }

// #include <stdio.h> 
// int main() 
// { 
//     int rows = 5; 
//     // first loop to print all rows 
//     for (int i = 0; i < rows; i++) { 
//         // inner loop 1 to print white spaces 
//         for (int j = 0; j < 2 * (rows - i) - 1; j++) { 
//             printf(" "); 
//         } 
//         // inner loop 2 to print star * character 
//         for (int k = 0; k < 2 * i + 1; k++) { 
//             printf("* "); 
//         } 
//         printf("\n"); 
//     } 
//     return 0; 
// }

//          * 
//        * * *
//      * * * * *
//    * * * * * * *
//  * * * * * * * * *

// // program to swap two number using function 
// #include<stdio.h>
// int swap(int *a,int *b){
//     int temp;
//     temp=*a;
//     *a=*b;  
//     *b=temp;
// }
//     int main(){
//     int a, b;
//     printf("Enter the value of two number: ");
//     scanf("%d%d",&a,&b);
//     printf("before swap a: %d, b: %d\n",a,b);
//     swap(&a,&b);
//     printf("After swaping a: %d, b: %d",a,b);
//      return 0;
// }

// Multiple the two martix by function
#include<stdio.h>
     int main(){
    int a[10][10],b[10][10], m[10][10];
    int r,c;
    printf("enter the number of rows : ");
    scanf("%d",&r);
    printf("enter the number of Columns : ");
    scanf("%d",&c);

    printf("Enter the elements of A matrix: ");
    for(int i=0;i<r;i++){
    for(int j=0;j<c;j++){
    scanf("%d",&a[i][j]);
    }}
     printf("Enter the elements of B matrix: ");
    for(int i=0;i<r;i++){
    for(int j=0;j<c;j++){
    scanf("%d",&b[i][j]);
    }}
    for(int i=0;i<r;i++){
        printf("")
    }
     return 0;
}