##########################################################################

# ---------------------------------------------------------------------------------------------------------------------

# This is Python code to produce IPCC AR6 WGI Figure 4.11 and the assessed GSAT time series.

# Creator: Sebastian Milinski, Max Planck Institute for Meteorology, Hamburg, Germany

# Contact: sebastian.milinski@mpimet.mpg.de, jochem.marotzke@mpimet.mpg.de

# Last updated on: May 18th, 2022

# --------------------------------------------------------------------------------------------------------------------

#

# - Code functionality: The Jupyter Notebook figure4.11.ipynb computes the AR6 WG1 assessed GSAT projections and figure 4.11.

# - Input data: AR6 WG1 assessed ERF, constrained CMIP6 projections according to the papers cited in the report (Liang et. al 2020, Ribes et al. 2021, Tokarska et al. 2020). 
    All input and final data is distributed with the code and they have been archived by DKRZ and made available here: https://www.wdc-climate.de/ui/entry?acronym=IPCC-DDC_AR6_Sup_GSATPr.

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

#  License: Apache 2.0

#

# ----------------------------------------------------------------------------------------------------

# How to cite:

# When citing this code, please include both the code citation and the following citation for the related report component:
Lee, J.-Y., J. Marotzke, G. Bala, L. Cao, S. Corti, J.P. Dunne, F. Engelbrecht, E. Fischer, J.C. Fyfe, C. Jones, A. Maycock, J. Mutemi, O. Ndiaye, S. Panickal, and T. Zhou, 2021:
Future Global Climate: Scenario-Based Projections and Near-Term Information Supplementary Material. In Climate Change 2021: The Physical Science Basis. Contribution of 
Working Group I to the Sixth Assessment Report of the Intergovernmental Panel on Climate Change [Masson-Delmotte, V., P. Zhai, A. Pirani, S.L. Connors, C. Péan, S. Berger, N. Caud,
 Y. Chen, L. Goldfarb, M.I. Gomis, M. Huang, K. Leitzell, E. Lonnoy, J.B.R. Matthews, T.K. Maycock, T. Waterfield, O. Yelekçi, R. Yu, and B. Zhou (eds.)]


########################################################################
