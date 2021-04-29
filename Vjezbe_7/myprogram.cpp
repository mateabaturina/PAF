#include <iostream>
#include "Particle.h"

int main(){

    Particle particle1(25.0, 60.0, 0.0, 0.0);
    particle1.move();
    particle1.range();
    particle1.time();

    Particle particle2(25.0, 30.0, 0.0, 0.0);
    particle2.move();
    particle2.range();
    particle2.time();
    return 0;
}