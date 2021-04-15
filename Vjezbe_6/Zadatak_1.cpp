#include <iostream>

void Jednadba_pravca(float x1, float x2, float y1, float y2){

    float result = (x2 - x1)/(y2 - y1);
    std::cout << "Jednadba pravca je y - " << y1 <<" = "<< result << " * x - "<< x1;
}
int main() {
    float x1 = 2.0;
    float x2 = 6.0;
    float y1 = 1.0;
    float y2 = 3.0;
    
    Jednadba_pravca(x1, x2, y1, y2);

    return 0;
}