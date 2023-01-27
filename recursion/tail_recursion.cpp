// ### Tail Recursion
// It is a way of writing the recursive call function at the end of the function,
// so there is nothing else left to do in the function. The compiler optimizes the tail recursion.


/* A NON-tail-recursive function */
//  The function is not tail recursive because the value returned by fact(n-1) is used in fact(n)
// and call to fact(n-1) is not the last thing done by fact(n)
unsigned int fact(unsigned int n)
{
    if (n <= 0)
        return 1;

    return n * fact(n - 1);
}

/* A tail-recursive funciton */
// The idea is to use one more argument and accumulate the factorial value in the second argument. When n reaches 0, return the accumulated value.
unsigned int factTR(unsigned int n, unsigned int a)
{
    if(n<=1)
        return a;
    
    return factTR(n-1, n*a);
}

unsigned int fact(unsigned int n )
{
    return factTR(n, 1);
}
