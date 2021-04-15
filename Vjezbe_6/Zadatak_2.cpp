#include <iostream>

void Kruznica(float p, float q, float r, float x, float y){

    float d =  (x-p)*(x-p) + (y-q)*(y-q);
    float R = r*r;

    if (d==R) {
        std::cout << "Tocka se nalazi na kruznici.";
    } else if (d<R) {
        std::cout << "Tocka se nalazi unutar kruznice.";
    } else {
        std::cout << "Tocka se nalazi van kruznice.";
    }
}

int main() {

    float p = 1.0;
    float q = 1.0;
    float r = 3.0;
    float x = 2.0;
    float y = 2.0;

    Kruznica(p, q, r, x, y);

    return 0;
}