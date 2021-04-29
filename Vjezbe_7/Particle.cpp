#include <iostream>
#include "Particle.h"
#include<cmath>

double Particle::move(){
        double a = 9.81; 
        double v = v0 * k;
        double v2 = v0 * k2;
        dt = 0.01;
        t = 0;
        int i = 0;
        for (i = 1; i < 1000; i++){
            x = x + v * dt;
            v2 = v2 - a * dt;
            y = y + v2 * dt;
            t = t + dt;
            if(y <= 0){
                break;
            } 
        }
        return 0; 
    } 
    double Particle::range(){
        double X = x;
        move();
        double d = x - X;
        std::cout << "Domet iznosi " << d << " m. ";
        return 0;
    }
    double Particle::time(){
        move();
        double T = t;
        std::cout << "Vrijeme trajanje iznosi " << T << " s. ";
        return 0;
    }