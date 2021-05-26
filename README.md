# Flows Over Periodic Hills of Parameterized Geometries
### A Dataset for Data-Driven Turbulence Modeling From Direct Simulations
---------------------------------------------------------------------------------


For data-driven turbulence modeling, we need benchmark data from systematically and continuously varied flow conditions (e.g., Reynolds number and geometry) with maximum coverage in the parameter space. To this end, we perform direct numerical simulations of flows over periodic hills with varying slopes, resulting in a family of flows over periodic hills which ranges from incipient to mild and massive separations.

The details are provided in the paper below: 
- H. Xiao, J.-L. Wu, S. Laizet, L. Duan. Flows over periodic hills of parameterized geometries: a dataset for data-driven turbulence modeling from direct simulations. Computers and Fluids, 200, 104431, 2020. DOI: https://doi.org/10.1016/j.compfluid.2020.104431 Also available at: https://arxiv.org/abs/1910.01264

Notes on data format:
- Mean flow data are provided in *coarse* meshes (comparable to those used in  RANS simulations) as OpenFOAM cases.
- The same data on the original DNS meshes are also provided as ASCII files.
- The data include (and only include) 
  * mean pressure field, 
  * mean velocities fields, and 
  * second order statistics of velocities (i.e., the Reynolds stress fields)
  * mean dissipation rate (only for data uploaded on April 15, 2021 or later)
- Note: instantaneous data and higher order statistics are *not* saved during our simulations; these data would require very large storage spaces.

### Additional data uploaded on April 15, 2021:
- Dr. Laizet added a *new database with 27 simulations* (Reynolds=5600, 3 different heights, 3 different streamwise extents and 3 different hill shapes). For details see:  [``pehill_new_DNS_database/README``](pehill_new_DNS_database/README_NEWDATABASE.pdf)

Contact: 
- Sylvain Laizet <s.laizet@imperial.ac.uk> (Imperial College London)
- Heng Xiao <hengxiao@vt.edu> (Virginia Tech) 

