// Given a number N, verify if N is prime or not.

// Return 1 if N is prime, else return 0.

// Example :

// Input : 7
// Output : True

int Solution::isPrime(int n) {

if(n<=1){
    return false;
}

if(n==3||n==2){
    return true;
}
if(n%3==0 || n%2==0){
    return false;
}
for(int i=5;i*i<=n;i=i+6){
    if(n%i==0 || n%(i+2)==0){
        return false;
    }
}
return true;
}