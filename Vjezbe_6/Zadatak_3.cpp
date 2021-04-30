#include <iostream>
#include <list>
#include <iterator>
#include <algorithm>

using namespace std;

void Polje_cijelih_brojeva(list <int> lista){

    list <int> :: iterator it;
    for(it = lista.begin(); it != lista.end(); ++it)
        cout << '\t' << *it;
    cout << '\n';
}

int main() {

    list<int> lista;
    lista.push_back(2);
    lista.push_back(-3);
    lista.push_back(4);
    lista.push_back(0);
    lista.push_back(-6);
    lista.push_back(5);

    cout << "\nOriginalna lista je : ";
    Polje_cijelih_brojeva(lista);

    cout << "\nLista nakon okretanja redoslijeda clanova polja je : ";
    lista.reverse();
    Polje_cijelih_brojeva(lista);

    cout << "\nLista nakon zamjene clanova polja je : ";
    using std::swap;
    for (auto it = std::begin(lista); it != std::end(lista); it = std::adjacent_find(it, std::end(lista), std::less<int>{})) {
    swap(*it, *std::next(it));
    }
    Polje_cijelih_brojeva(lista);

    cout << "\nLista nakon sortiranja clanova polja je : ";
    lista.sort();
    Polje_cijelih_brojeva(lista);

    return 0;
}



