#include <iostream>

void Jednadzba(float a1, float b1, float c1, float a2, float b2, float c2){

    float d = a1*b2 - b1*a2;
    float x = (c1*b2 - b1*c2)/ d;
    float y = (a1*c2 - c1*a2)/ d;

    if(d != 0){
        std::cout << "X iznosi " << x <<" a Y iznosi "<< y;
        
    } else{
        printf("Jednadzba nema rijesenja ili ih mnogo postoje.\n");
    }
}

int main() {

    float a1 = 2.0;
    float b1 = 1.0;
    float c1 = 3.0;
    float a2 = 2.0;
    float b2 = 2.0;
    float c2 = 5.0;

    Jednadzba(a1, b1, c1, a2, b2, c2);

    return 0;
}