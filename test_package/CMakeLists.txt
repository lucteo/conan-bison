project(TestBison)
cmake_minimum_required(VERSION 2.8.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

# Find BISON in the Conan path
set(CMAKE_PREFIX_PATH ${CONAN_BISON_ROOT} ${CMAKE_PREFIX_PATH})
find_package(BISON)

# Add a test grammar
BISON_TARGET(test-bison mfcalc.y ${CMAKE_CURRENT_BINARY_DIR}/mfcalc.c VERBOSE ${CMAKE_CURRENT_BINARY_DIR}/mfcalc.output)
message(STATUS "Bison executable: ${BISON_EXECUTABLE}")

include_directories( "." )
include_directories( "${CMAKE_CURRENT_BINARY_DIR}" )
add_executable(test-bison ${BISON_test-bison_OUTPUTS})
