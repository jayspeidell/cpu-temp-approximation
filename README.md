
               _____ ______ _   _   _____                    
              /  __ \| ___ \ | | | |_   _|                   
              | /  \/| |_/ / | | |   | | ___ _ __ ___  _ __  
              | |    |  __/| | | |   | |/ _ \ '_ ` _ \| '_ \
              | \__/\| |   | |_| |   | |  __/ | | | | | |_) |
              \____/ \_|    \___/    \_/\___|_| |_| |_| .__/
                                                      | |    
                                                      |_|    
                ___              _           _               
               / _ \            | |         (_)              
              / /_\ \_ __   __ _| |_   _ ___ _ ___           
              |  _  | '_ \ / _` | | | | / __| / __|          
              | | | | | | | (_| | | |_| \__ \ \__ \          
              \_| |_/_| |_|\__,_|_|\__, |___/_|___/          
                                   __/ |                    
                                  |___/                     


                                      by
                                 Jay Speidell


## 1. Getting Started     

Langauge: Python 3

Documentation is in docs/ (numpy style)

Unit tests are in tests/

Sample input data is in data/

Results are written to files in output/

## 2. Project Info

This program solves the problem of interpolating or approximating a timeline of CPU temperatures. It uses three strategies:

- Linear Piecewise Interpolation: This allows us to reasonably approximate values in between time steps. One piecewise function is generated for each time step.
- Linear Least Squares: This creates a generalized function to approximate the CPU temperature as a function of time. But since CPU temperature is based on CPU activity rather than time, I believe that as more time steps are added this function will converge to a horizontal line intercepting the y axis at the average temperature value.
- Cubic Spline: Another piecewise strategy, this time drawing bezier curves between points. 

## 3. Requirements  

numpy


## 4. Compilation & Execution Instructions     

Run unit tests:

> python -m pytest

Run program

> python main.py { path to data file } { data labels : yes/no }

Example

> python main.py data/sensors-2018.12.26.txt yes
