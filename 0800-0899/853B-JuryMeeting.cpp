#include <cstdio>
#include <iostream>
#include <vector>
#include <set>

int main(){

    const int F = 4;
    int64_t n, m, k; scanf("%lld %lld %lld", &n, &m, &k);
    std::vector<std::vector<int64_t> > fl(m, std::vector<int64_t>(F, 0));
    int64_t D(0);
    for(int64_t p = 0; p < m; p++){
        scanf("%lld %lld %lld %lld", &fl[p][0], &fl[p][1], &fl[p][2], &fl[p][3]);
        D = (D > fl[p][0]) ? D : fl[p][0];
    }
    int64_t total = 0;

    std::vector<int64_t> costA(D, -1);
    std::vector<int64_t> cheapA(n + 1, 1e7);
    std::set<int64_t> citiesA;
    for(int64_t p = 0; p < m; p++){
        std::vector<int64_t> v = fl[p];
        if(v[1] == 0){continue;}
        int64_t city = fl[p][1];
        int64_t cost = fl[p][3];
        if(cheapA[city] == 0 || cost < cheapA[city]){
            cheapA[city] = cost;
            total += cost - cheapA[city];
        }

        citiesA.insert(city);
        if(citiesA.size() >= n){costA[p] = total;}
        if(p > 0 && costA[p - 1] > 0 && costA[p - 1] < costA[p]){costA[p] = costA[p - 1];}
    }


    std::vector<int64_t> costB(D, -1);
    std::vector<int64_t> cheapB(n + 1, 1e7);
    std::set<int64_t> citiesB;
    for(int64_t p = m - 1; p >= 0; p--){
        std::vector<int64_t> v = fl[p];
        if(v[2] == 0){continue;}
        int64_t city = fl[p][2];
        int64_t cost = fl[p][3];
        if(cheapB[city] == 0 || cost < cheapB[city]){
            cheapB[city] = cost;
            total += cost - cheapB[city];
        }

        citiesB.insert(city);
        if(citiesB.size() >= n){costB[p] = total;}
        if(p > 0 && costB[p - 1] > 0 && costB[p - 1] < costB[p]){costB[p] = costB[p - 1];}
    }





    return 0;
}
