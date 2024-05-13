# n-body problem
# A Matlab script to compute n-body

Several Solar System bodies are used to calculate their orbits based on the following:
1) Masses,
2) Initial positions on specific date and
3) Initial velocities.

The script makes use of a call to Python to retrieve real positions and velocities from JPL Horizons System.
The positions are in Astronomical Units (AU) and the velocities in AU/day.

The procedures are as follows:
1) Ensure a Python environment is accessible by Matlab as per instructions here:
    https://www.mathworks.com/support/search.html/answers/1750425-python-virtual-environments-with-python-interface.html?fq%5B%5D=asset_type_name:answer&page=1.
2) Edit the date required in the python script.
3) Run the nbody Matlab script. 
