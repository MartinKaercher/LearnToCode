# include <stdio.h>
# include <time.h>
# include <math.h>

int main()
{

         
    clock_t start, end;
    double cpu_time_used;
    start = clock();
    int i ;
    double d;
    for (i=0; i<1000000; ++i)
    {
        d  = sqrt(sqrt(i));
    }
    printf("%d \n", i);
    end = clock();
    cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
    printf("Time used for the sum: %f \n", cpu_time_used);
}
