cmake_minimum_required(VERSION 3.26)
project(C C)

set(CMAKE_C_STANDARD 11)

# Define the number of hod directories to include
set(NUMBER_OF_HOD "3" CACHE STRING "Number of hod directories to include")

# Add the main.c and hod files based on the selected number
add_executable(C main.c)

# Conditionally include hod files based on the selected number
if(NUMBER_OF_HOD MATCHES "^[0-9]+$" AND NUMBER_OF_HOD GREATER 1 AND NUMBER_OF_HOD LESS_EQUAL 10)
    target_sources(C PRIVATE
            ${NUMBER_OF_HOD}hod/${NUMBER_OF_HOD}hod.c
            ${NUMBER_OF_HOD}hod/${NUMBER_OF_HOD}hod.h
    )
else()
    message(FATAL_ERROR "Invalid value for NUMBER_OF_HOD. Please provide a number between 2 and 10.")
endif()
