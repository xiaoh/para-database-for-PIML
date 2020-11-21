# Flows Over Periodic Hills of Parameterized Geometries
### A Dataset for Data-Driven Turbulence Modeling From Direct Simulations
---------------------------------------------------------------------------------


For data-driven turbulence modeling, we need benchmark data from systematically and continuously varied flow conditions (e.g., Reynolds number and geometry) with maximum coverage in the parameter space. To this end, we perform direct numerical simulations of flows over periodic hills with varying slopes, resulting in a family of flows over periodic hills which ranges from incipient to mild and massive separations.

The details are provided in the paper below: 
- H. Xiao, J.-L. Wu, S. Laizet, L. Duan. Flows over periodic hills of parameterized geometries: a dataset for data-driven turbulence modeling from direct simulations. Computers and Fluids, 200, 104431, 2020. DOI: https://doi.org/10.1016/j.compfluid.2020.104431 Also available at: https://arxiv.org/abs/1910.01264

Notes on data format:
- Mean flow data are provided in *coarse* meshes (comparable to those used in  RANS simulations) as OpenFOAM cases.
- The same data on the original DNS meshes are also provided as ASCII files.
- The data include mean pressure field, mean velocities fields, and second order statistics (Reynolds stress fields)
- Note: instantaneous data and higher order statistics are *not* saved during our simulations. 


Contact: 
- Heng Xiao <hengxiao@vt.edu> (Virginia Tech) 
- Jinlong Wu <jinlong@vt.edu> 
- Sylvain Laizet <s.laizet@imperial.ac.uk> (Imperial College London)

