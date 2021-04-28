#include <iostream>
#include <list>
#include <iterator>

using namespace std;

void Polje_cijelih_brojeva(list <int> lista){

    list <int> :: iterator it;
    for(it = lista.begin(); it != lista.end(); ++it)
        cout << '\t' << *it;
    cout << '\n';
    
}

int main() {

    list<int> lista;
    int a = 2;
    int b = 5;
    lista.push_back(a);
    lista.push_back(-3);
    lista.push_back(4);
    lista.push_back(0);
    lista.push_back(-6);
    lista.push_back(b);

    cout << "\nOriginalna lista je : ";
    Polje_cijelih_brojeva(lista);

    cout << "\nLista nakon okretanja redoslijeda clanova polja je : ";
    lista.reverse();
    Polje_cijelih_brojeva(lista);

    cout << "\nLista nakon zamjene clanova polja je : ";
    std::swap(a, b);
    Polje_cijelih_brojeva(lista);

    cout << "\nLista nakon sortiranja clanova polja je : ";
    lista.sort();
    Polje_cijelih_brojeva(lista);

    return 0;
}



