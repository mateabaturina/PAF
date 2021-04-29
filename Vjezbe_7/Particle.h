#define _USE_MATH_DEFINES
#include<cmath>

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
    double move();
    double range();
    double time();
};