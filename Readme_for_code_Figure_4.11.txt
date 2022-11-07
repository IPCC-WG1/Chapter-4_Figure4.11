##########################################################################
# ---------------------------------------------------------------------------------------------------------------------
# This is Python code to produce IPCC AR6 WGI Figure 4.11 and the assessed GSAT time series.
# Creator: Sebastian Milinski, Max Planck Institute for Meteorology, Hamburg, Germany
# Contact: sebastian.milinski@mpimet.mpg.de, jochem.marotzke@mpimet.mpg.de
# Last updated on: May 18th, 2022
# --------------------------------------------------------------------------------------------------------------------
#
# - Code functionality: The Jupyter Notebook figure4.11.ipynb computes the AR6 WG1 assessed GSAT projections and figure 4.11.
# - Input data: AR6 WG1 assessed ERF, constrained CMIP6 projections according to the papers cited in the report (Liang et. al 2020, Ribes et al. 2021, Tokarska et al. 2020). All input data is distributed with the code.
# - Output variables: The code plots the figure as in the report. The code can optionally produce the assessed GSAT projections (5%, central estimate, 95%) as NetCDF files.
#
# ----------------------------------------------------------------------------------------------------
# Information on  the software used
# - Software Version: Python 3.8.8
# - Landing page to access the software: [if possible provide a DOI]* 
# - Operating System: [insert operating system and date of last update]*
# - Environment required to compile and run: matplotlib 3.3.3, numpy 1.19.5, XArray 0.16.2, pandas 1.2.0, tqdm 4.56.0, cdo 1.9.9 , python-cdo 1.5.4
#  ----------------------------------------------------------------------------------------------------
#
#  License: Creative Commons Attribution 4.0 International License (http://creativecommons.org/licenses/by/4.0/)]
#
# ----------------------------------------------------------------------------------------------------
# How to cite:
# When citing this code, please include both the code citation and the following citation for the related report component:
########################################################################