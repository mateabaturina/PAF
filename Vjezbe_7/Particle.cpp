#include <iostream>
#include "Particle.h"

int main(){

    Particle particle1;

    particle1.move(10.0, 60.0, 0.0, 0.0);
    float a = particle1.range();
    std::cout << "Domet iznosi " << a << " m. ";
    float b = particle1.time();
    std::cout << "Vrijeme trajanje iznosi " << b << " s. ";
    return 0;
}