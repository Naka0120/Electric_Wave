#include "visualization.h"
#include <iostream>
#include <vector>
#include <matplotlibcpp.h>

namespace plt = matplotlibcpp;

void plotFields(const std::vector<double>& ey, const std::vector<double>& bz, double time) {
    plt::figure_size(800, 600);
    
    plt::subplot(2, 1, 1);
    plt::title("Electric Field (Ey) at time " + std::to_string(time));
    plt::xlabel("Position");
    plt::ylabel("Ey");
    plt::plot(ey);
    
    plt::subplot(2, 1, 2);
    plt::title("Magnetic Field (Bz) at time " + std::to_string(time));
    plt::xlabel("Position");
    plt::ylabel("Bz");
    plt::plot(bz);
    
    plt::show();
}

void visualize(const std::vector<double>& ey, const std::vector<double>& bz, double time) {
    plotFields(ey, bz, time);
}