cmake_minimum_required(VERSION 3.16)
project(HYDRA_Track VERSION 0.1 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(hydra_track
    src/main.cpp
)

target_include_directories(hydra_track PRIVATE src)
