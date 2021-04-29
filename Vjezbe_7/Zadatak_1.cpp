#include <iostream>
#define _USE_MATH_DEFINES
#include <cmath>
#include <list>

class Particle{
    private:
    double v0;
    double kut;
    double kt; 
    double x;
    double y;
    double t;
    double k;
    double k2;
    double dt;

    public:
    Particle(double _v0,  double _kut, double _x, double _y){
        v0 = _v0;
        kut = _kut;
        x = _x;
        y = _y;
        kt = kut * (M_PI / 180);
        k = cos(kt);
        k2 = sin(kt);
    }
    double move( ){
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
    double range(){
        double X = x;
        move();
        double d = x - X;
        std::cout << "Domet iznosi " << d << " m. ";
        return 0;
    }
    double time(){
        move();
        double T = t;
        std::cout << "Vrijeme trajanje iznosi " << T << " s. ";
        return 0;
    }
};

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