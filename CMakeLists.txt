cmake_minimum_required(VERSION 3.10)
project(one_d_em_wave_sim)

set(CMAKE_CXX_STANDARD 11)

include_directories(include)

file(GLOB SOURCES "src/*.cpp")

add_executable(one_d_em_wave_sim ${SOURCES})

enable_testing()
add_subdirectory(tests)