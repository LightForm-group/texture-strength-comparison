texture-strength-comparison
-----------

A set of python scripts for comparing the texture strength output of synchrotron X-ray diffraction (SXRD) and electron backscatter diffraction (EBSD) data processed using MTEX, producing texture intensity plots and 2D texture intensity maps.

This package has been used to analyse a number of synchrotron diffraction experiments at DESY and Diamond Light Source beamlines.

Used to compare texture intensity variation from stage scan synchrotron measurements using MAUD and Continuous-Peak-Fit, with the texture variation recorded using an EBSD map that had been divided into equivalent sized squares as were used for the synchrotron analysis.

Development
--------------

This package was developed by Christopher S. Daniel at The 
University of Manchester, UK, and was funded by the Engineering and Physical Sciences Research Council (EPSRC) via the LightForm programme grant (EP/R001715/1). LightForm is a 5 year multidisciplinary project, led by The Manchester University with partners at University of Cambridge and Imperial College, London (https://lightform.org.uk/).

Contents
-----------

**The following notebooks have been used to analyse different experimental data:**
    
1. `texture_strength_comparison_diamond_2017.ipynb` A notebook analysing texture intensity changes from a series of synchrotron measurements recorded during high temperature deformation of a Ti-6Al-4V tensile specimen. The texture data was fitted using two different methods, MAUD (a Rietveld refinement software) and Continuous-Peak-Fit (a Fourier series based peak analysis method).

2. `texture_strength_comparison_diamond_2021.ipynb` A notebook analysing texture intensity changes from a series of synchrotron measurements recorded as a stage-scan (X-Y) across a pre-rolled Ti-6Al-4V sample. The texture data was used to compare texture intensity variation from stage scan synchrotron measurements using MAUD and Continuous-Peak-Fit, with the texture variation recorded using an EBSD map that had been divided into equivalent sized squares as were used for the synchrotron analysis.

3. `texture_strength_comparison_desy_2020-21.ipynb` A notebook analysing texture intensity changes from a series of synchrotron measurements recorded during high temperature deformation of Ti-6Al-4V compression specimens, at different temperatures and strain rates. The texture data was fitted using Continuous-Peak-Fit.

4. `texture_strength_comparison_desy_2020-21_multihit.ipynb` A notebook analysing texture intensity changes from a series of synchrotron measurements recorded during high temperature deformation of Ti-6Al-4V compression specimens, with multi-hit deformation and hold stages. The texture data was fitted using Continuous-Peak-Fit.

*Note, the `example-data/` and `example-analysis/` folders contain instuctions for downloading data that can be used as an example analysis, but a clear external file structure should be setup to support the analysis of large synchrotron datasets.*

Installation and Virtual Environment Setup
-----------

Follow along by copying / pasting the commands below into your terminal (for a guide on using a python virtual environments follow steps 4-7).

**1. First, you'll need to download the repository to your PC. Open a unix command line on your PC and navigate to your Desktop (or GitHub repository):**
```unix
cd ~/Desktop
```
**2. In your teminal, use the following command to clone this repository to your Desktop:**
```unix
git clone https://github.com/LightForm-group/texture-strength-comparison.git
```
**3. Navigate inside `Desktop/texture-strength-comparison/` and list the contents using `ls`(macOS) or `dir`(windows):**
```unix
cd ~/Desktop/texture-strength-comparison/
```
**4. Next, create a python virtual environment (venv) which contains all of the python libraries required to use texture-strength-comparison.
Firstly, use the following command to create the venv directory which will contain the necessary libraries:**
```unix
python -m venv ~/Desktop/texture-strength-comparison/venv
```
**5. Your `texture-strength-comparison/` directory should now contain `venv/`. Install the relevant libraries to this venv by first activating the venv:**
```unix
source ~/Desktop/texture-strength-comparison/venv/bin/activate
```
*Note, the beginning of your command line should change from `(base)` to include `(venv)`.*

**6. Install the python libraries to this virtual environment using pip and the `requirements.txt` file included within the repository:**
```unix
pip install -r ~/Desktop/texture-strength-comparison/requirements.txt
```
**7. To ensure these installed correctly, use the command `pip list` and ensure the following packages are installed:**
```unix
pip list
# Check to ensure that all of the following are listed:
#jupyter
#numpy
#matplotlib
#pathlib
#tqdm
#pyyaml
```
**8. If all in step 7 are present, you can now run the example notebooks.
Ensure the venv is active and use the following command to boot jupyter notebook (using all libraries installed in the venv)
Warning - using just `jupyter notebook` without `python -m` can result in using your default python environment (the libraries may not be recognised):**
```unix
python -m jupyter notebook
```
**9. Work through the notebooks and setup yaml text files for reproducible texture strength intensity analysis of large synchrotron datasets.**

**10. When you're finished using the virtual environment, deactivate it!
This will avoid confusion when using different python libraries that are not installed within the virtual environment:**
```unix
deactivate
```

Required Libraries
--------------------

The required libraries are listed in requirements.txt