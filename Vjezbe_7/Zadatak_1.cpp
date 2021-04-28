#include <iostream>
#include <cmath>
#include <list>

class Particle{
    private:
    float v0;
    float kut;
    float kt = kut * (M_PI / 180);
    float x;
    float y;

    public:
    float move( float v0,  float kut, float x, float y){
        float a = 9.81;
        float k = cos(kt);
        float k2 = sin(kt);
        float v = v0 * k;
        float v2 = v0 * k2;
        float dt = 0.01;
        float t = 0;
        std::list<int> xlist;
        int i = 0;
        for (i = 1; i < 1000; i++){
            float x = x + v * dt;
            float v2 = v2 - a * dt;
            float y = y + v2 * dt;
            float t = t + dt;
            if(y <= 0){
                break;
            xlist.push_back(x);
            } 
        }
        return x; 
    } 
    float range(){
        float X = x;
        move(v0, kut, x, y);
        //float a = xlist[-1]
        float d = x - X;
        std::cout << "Domet iznosi " << x << " m. ";
        return 0;
    }
    float time(){
        move(v0, kut, x, y);
        float t = t;
        std::cout << "Vrijeme trajanje iznosi " << t << " s. ";
        return 0;
    }
};

int main(){

    Particle particle1;

    particle1.move(10.0, 60.0, 0.0, 0.0);
    particle1.range();
    particle1.time();
    return 0;
}