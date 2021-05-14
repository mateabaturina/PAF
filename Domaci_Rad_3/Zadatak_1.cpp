#include <iostream>
#include <cmath>
#include <list>
#include <iostream>
#include <string>
#include <fstream>
#include <iterator>
#include <algorithm>

 
using namespace std;

class Harmonic_Oscillate {
    private:
    double dt;  
    double k;  
    double m;  
    double v0;
    double x0;
    double t;
    double ti;
    double a; 

    public:
    Harmonic_Oscillate(double _dt, double _k, double _m, double _v0, double _x0, double _ti){
        dt = _dt; 
        k = _k; 
        m = _m; 
        v0 = _v0; 
        x0 = _x0;
        ti = _ti;
    }
    double oscillate(){
        std::list<int> tlist;
        std::list<int> vlist;
        std::list<int> alist;
        std::list<int> xlist;
        t = 0;
        int i = 0;
        ofstream fw("HO.txt", std::ofstream::out | ios::app);
        if (fw.is_open());
            for (i = 1; i < 8000; i++){
                a = (-k/m)*x0;
                v0 = v0 + a*dt;
                x0 = x0 + v0*dt;
                t += dt;
                fw << t << "\t"; 
                fw << v0 << "\t";
                fw << x0 << "\t";
                fw << a << "\t" << endl;
            } 
        fw.close();
        return 0;
    }
};

int main(){
    Harmonic_Oscillate harmosc1(0.01, 2.0, 5.0, 15.0, 0.0, 10.0);
    harmosc1.oscillate();
}