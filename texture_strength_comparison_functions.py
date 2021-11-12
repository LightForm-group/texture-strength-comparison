import pathlib
import re

from tqdm.notebook import tqdm
import numpy as np
import matplotlib.pyplot as plt
import yaml

def get_config(path: str) -> dict:
    """Open a yaml file and return the contents."""
    with open(path) as input_file:
        return yaml.safe_load(input_file)
    
def load_ebsd_alpha(config_path: str):
    """Load EBSD alpha-phase texture results from text file 
    based on input parameters from a yaml configuration file.
    
    :param config_path: path to the configuration file.
    
    :return: EBSD alpha texture results as a dictionary, 
    containing arrrays of texture refinement data.
    """
    config = get_config(config_path)
    
    ebsd_alpha_results_file = config["file_paths"]["ebsd_alpha_results_file"]
    print("The EBSD results file is: ", ebsd_alpha_results_file, sep = '\n', end = '\n\n')
    ebsd_results = np.loadtxt(ebsd_alpha_results_file, usecols = np.arange(0,11), dtype='str', skiprows = 1)
    
    print("The data headers from the EBSD results file are...", sep = '\n', end = '\n\n')
    with open (ebsd_alpha_results_file) as file:
        header = file.readline().split()
        for i in range(0, len(header)):
            print('header column ', i ,' = ', header[i])
    
    ebsd_alpha_results = {
                    "image_number" : ebsd_results[:,0].astype(float),
                    "texture_index" : ebsd_results[:,1].astype(float),
                    "odf_max" : ebsd_results[:,2].astype(float),
                    "phi1" : ebsd_results[:,3].astype(float),
                    "PHI" : ebsd_results[:,4].astype(float),
                    "phi2" : ebsd_results[:,5].astype(float),
                    "0002_pf_max" : ebsd_results[:,6].astype(float),
                    "10-10_pf_max" : ebsd_results[:,7].astype(float),
                    "11-20_pf_max" : ebsd_results[:,8].astype(float),
                    "basal_TD_volume" : ebsd_results[:,9].astype(float),
                    "basal_RD_volume" : ebsd_results[:,10].astype(float),
                    }
    print('\n', "The EBSD results have been written to new arrays with the following keys: ", ebsd_alpha_results.keys(), sep = '\n', end = '\n\n')
    
    return ebsd_alpha_results

def load_sxrd_cpf_alpha(config_path: str):
    """Load SXRD alpha-phase texture results refined using 
    Continuous-Peak-Fit, using Fourier peak analysis, from 
    text file based on input parameters from a yaml configuration file.
    
    :param config_path: path to the configuration file.
    
    :return: SXRD alpha texture results from Continuous-Peak-Fit 
    as a dictionary, containing arrrays of texture refinement data.
    """
    config = get_config(config_path)
    
    sxrd_experiment_number = config["user_inputs"]["sxrd_experiment_number"]
    print("The SXRD experiment number is: ", sxrd_experiment_number, sep = '\n', end = '\n\n')

    sxrd_cpf_alpha_results_file = config["file_paths"]["sxrd_cpf_alpha_results_file"].format(experiment_number = sxrd_experiment_number)
    print("The SXRD results file is: ", sxrd_cpf_alpha_results_file, sep = '\n', end = '\n\n')

    sxrd_cpf_results = np.loadtxt(sxrd_cpf_alpha_results_file, usecols = np.arange(0,9), dtype='str', skiprows = 1)
    
    cpf_alpha_results = {
                    "image_number" : sxrd_cpf_results[:,0].astype(float),
                    "texture_index" : sxrd_cpf_results[:,1].astype(float),
                    "odf_max" : sxrd_cpf_results[:,2].astype(float),
                    "phi1" : sxrd_cpf_results[:,3].astype(float),
                    "PHI" : sxrd_cpf_results[:,4].astype(float),
                    "phi2" : sxrd_cpf_results[:,5].astype(float),
                    "0002_pf_max" : sxrd_cpf_results[:,6].astype(float),
                    "10-10_pf_max" : sxrd_cpf_results[:,7].astype(float),
                    "11-20_pf_max" : sxrd_cpf_results[:,8].astype(float),
                    }
    
    print("The SXRD results using Fourier peak analysis have been written to new arrays with the following keys: ", cpf_alpha_results.keys(), sep = '\n', end = '\n\n')
    
    return cpf_alpha_results
    
def load_sxrd_maud_alpha(config_path: str):
    """Load SXRD alpha-phase texture results refined using MAUD,
    using Rietveld refinement analysis, from text file 
    based on input parameters from a yaml configuration file.
    
    :param config_path: path to the configuration file.
    
    :return: SXRD alpha texture results from MAUD as a dictionary, 
    containing arrrays of texture refinement data.
    """
    config = get_config(config_path)
    
    sxrd_experiment_number = config["user_inputs"]["sxrd_experiment_number"]
    print("The SXRD experiment number is: ", sxrd_experiment_number, sep = '\n', end = '\n\n')
    sxrd_maud_alpha_results_file = config["file_paths"]["sxrd_maud_alpha_results_file"].format(experiment_number = sxrd_experiment_number)
    print("The SXRD results file is: ", sxrd_maud_alpha_results_file, sep = '\n', end = '\n\n')
    sxrd_maud_results = np.loadtxt(sxrd_maud_alpha_results_file, usecols = np.arange(0,9), dtype='str', skiprows = 1)
    
    maud_alpha_results = {
                    "image_number" : sxrd_maud_results[:,0].astype(float),
                    "texture_index" : sxrd_maud_results[:,1].astype(float),
                    "odf_max" : sxrd_maud_results[:,2].astype(float),
                    "phi1" : sxrd_maud_results[:,3].astype(float),
                    "PHI" : sxrd_maud_results[:,4].astype(float),
                    "phi2" : sxrd_maud_results[:,5].astype(float),
                    "0002_pf_max" : sxrd_maud_results[:,6].astype(float),
                    "10-10_pf_max" : sxrd_maud_results[:,7].astype(float),
                    "11-20_pf_max" : sxrd_maud_results[:,8].astype(float),
                    }
    print("The SXRD results using MAUD have been written to new arrays with the following keys: ", maud_alpha_results.keys(), sep = '\n', end = '\n\n')
    
    return maud_alpha_results

def load_ebsd_beta(config_path: str):
    """Load EBSD beta-phase texture results from text file 
    based on input parameters from a yaml configuration file.
    
    :param config_path: path to the configuration file.
    
    :return: EBSD beta texture results as a dictionary, 
    containing arrrays of texture refinement data.
    """
    config = get_config(config_path)
    
    ebsd_beta_results_file = config["file_paths"]["ebsd_beta_results_file"]
    print("The EBSD results file is: ", ebsd_beta_results_file, sep = '\n', end = '\n\n')
    ebsd_results = np.loadtxt(ebsd_beta_results_file, usecols = np.arange(0,12), dtype='str', skiprows = 1)
    
    print("The data headers from the EBSD results file are...", sep = '\n', end = '\n\n')
    with open (ebsd_beta_results_file) as file:
        header = file.readline().split()
        for i in range(0, len(header)):
            print('header column ', i ,' = ', header[i])
            
    ebsd_beta_results = {
                    "image_number" : ebsd_results[:,0].astype(float),
                    "texture_index" : ebsd_results[:,1].astype(float),
                    "odf_max" : ebsd_results[:,2].astype(float),
                    "phi1" : ebsd_results[:,3].astype(float),
                    "PHI" : ebsd_results[:,4].astype(float),
                    "phi2" : ebsd_results[:,5].astype(float),
                    "001_pf_max" : ebsd_results[:,6].astype(float),
                    "110_pf_max" : ebsd_results[:,7].astype(float),
                    "111_pf_max" : ebsd_results[:,8].astype(float),
                    "rotated_cube_volume" : ebsd_results[:,9].astype(float),
                    "alpha_fibre_volume" : ebsd_results[:,10].astype(float),
                    "gamma_fibre_volume" : ebsd_results[:,11].astype(float),
                    }
    print('\n', "The EBSD results have been written to new arrays with the following keys: ", ebsd_beta_results.keys(), sep = '\n', end = '\n\n')
    
    return ebsd_beta_results

def load_sxrd_cpf_beta(config_path: str):
    """Load SXRD beta-phase texture results refined using 
    Continuous-Peak-Fit, using Fourier peak analysis, from 
    text file based on input parameters from a yaml configuration file.
    
    :param config_path: path to the configuration file.
    
    :return: SXRD beta texture results from Continuous-Peak-Fit 
    as a dictionary, containing arrrays of texture refinement data.
    """
    config = get_config(config_path)
    
    sxrd_experiment_number = config["user_inputs"]["sxrd_experiment_number"]
    print("The SXRD experiment number is: ", sxrd_experiment_number, sep = '\n', end = '\n\n')

    sxrd_cpf_beta_results_file = config["file_paths"]["sxrd_cpf_beta_results_file"].format(experiment_number = sxrd_experiment_number)
    print("The SXRD results file is: ", sxrd_cpf_beta_results_file, sep = '\n', end = '\n\n')

    sxrd_cpf_results = np.loadtxt(sxrd_cpf_beta_results_file, usecols = np.arange(0,9), dtype='str', skiprows = 1)
    
    cpf_beta_results = {
                    "image_number" : sxrd_cpf_results[:,0].astype(float),
                    "texture_index" : sxrd_cpf_results[:,1].astype(float),
                    "odf_max" : sxrd_cpf_results[:,2].astype(float),
                    "phi1" : sxrd_cpf_results[:,3].astype(float),
                    "PHI" : sxrd_cpf_results[:,4].astype(float),
                    "phi2" : sxrd_cpf_results[:,5].astype(float),
                    "001_pf_max" : sxrd_cpf_results[:,6].astype(float),
                    "110_pf_max" : sxrd_cpf_results[:,7].astype(float),
                    "111_pf_max" : sxrd_cpf_results[:,8].astype(float),
                    }
    
    print("The SXRD results using Fourier peak analysis have been written to new arrays with the following keys: ", cpf_beta_results.keys(), sep = '\n', end = '\n\n')
    
    return cpf_beta_results

def load_sxrd_maud_beta(config_path: str):
    """Load SXRD beta-phase texture results refined using MAUD,
    using Rietveld refinement analysis, from text file 
    based on input parameters from a yaml configuration file.
    
    :param config_path: path to the configuration file.
    
    :return: SXRD beta texture results from MAUD as a dictionary, 
    containing arrrays of texture refinement data.
    """
    config = get_config(config_path)
    
    sxrd_experiment_number = config["user_inputs"]["sxrd_experiment_number"]
    print("The SXRD experiment number is: ", sxrd_experiment_number, sep = '\n', end = '\n\n')
    sxrd_maud_beta_results_file = config["file_paths"]["sxrd_maud_beta_results_file"].format(experiment_number = sxrd_experiment_number)
    print("The SXRD results file is: ", sxrd_maud_beta_results_file, sep = '\n', end = '\n\n')
    sxrd_maud_results = np.loadtxt(sxrd_maud_beta_results_file, usecols = np.arange(0,9), dtype='str', skiprows = 1)
    
    maud_beta_results = {
                    "image_number" : sxrd_maud_results[:,0].astype(float),
                    "texture_index" : sxrd_maud_results[:,1].astype(float),
                    "odf_max" : sxrd_maud_results[:,2].astype(float),
                    "phi1" : sxrd_maud_results[:,3].astype(float),
                    "PHI" : sxrd_maud_results[:,4].astype(float),
                    "phi2" : sxrd_maud_results[:,5].astype(float),
                    "001_pf_max" : sxrd_maud_results[:,6].astype(float),
                    "110_pf_max" : sxrd_maud_results[:,7].astype(float),
                    "111_pf_max" : sxrd_maud_results[:,8].astype(float),
                    }
    print("The SXRD results using MAUD have been written to new arrays with the following keys: ", maud_beta_results.keys(), sep = '\n', end = '\n\n')
    
    return maud_beta_results    
    
def plot_texture_strength(sxrd_experiment_number: int, phase: str, texture_strength_type: str, output_folder: str,
                          ebsd_results: dict, cpf_results: dict, maud_results: dict):
    """Plot texture strength versus image (scan) number
    for EBSD, SXRD-CPF and SXRD-MAUD texture results.
    Options available to select phase (alph or beta) and 
    type of texture strength being plotted i.e. texture index, 
    ODF maxima, or pole figure maxima for different alpha/beta 
    lattice planes.
    
    :param sxrd_experiment_number: Experiment number for the SXRD test.
    :param phase: Phase (alpha or beta) used to label output folder.
    :param texture_strength_type: Type of texture strength variable being plotted 
    (choose from texture_index, odf_max, 0002_pf_max, 10-10_pf_max, 11-20_pf_max, 001_pf_max, 110_pf_max, 111_pf_max).
    :param output_folder: File path to the output folder.
    :param ebsd_results: Dictionary containing arrays of EBSD texture results.
    :param cpf_results: Dictionary containing arrays of SXRD texture results, refined using Continuous-Peak-Fit.
    :param maud_results: Dictionary containing arrays of SXRD texture results, refined using MAUD.
    """
    plt.rc('xtick', labelsize = 24)
    plt.rc('ytick', labelsize = 24)
    plt.rc('legend', fontsize = 20)
    plt.rc('axes', linewidth = 2)
    plt.rc('xtick.major', width = 2, size = 10)
    plt.rc('xtick.minor', width = 2, size = 5)
    plt.rc('ytick.major', width = 2, size = 10)
    plt.rc('ytick.minor', width = 2, size = 5)
    
    fig, ((ax1),(ax2),(ax3)) = plt.subplots(1, 3, figsize = (25, 10))

    colour = '#440154ff', '#3b528bff', '#21908cff'

    if texture_strength_type == "texture_index":
        y_label = "Texture Index"
    
    elif texture_strength_type == "odf_max":
        y_label = "ODF Maxima (mrd)"
        
    elif texture_strength_type == "0002_pf_max":
        y_label = "0002 Pole Figure Maxima (mrd)"
        
    elif texture_strength_type == "10-10_pf_max":
        y_label = "10-10 Pole Figure Maxima (mrd)"
        
    elif texture_strength_type == "11-20_pf_max":
        y_label = "11-20 Pole Figure Maxima (mrd)"
        
    elif texture_strength_type == "001_pf_max":
        y_label = "001 Pole Figure Maxima (mrd)"
        
    elif texture_strength_type == "110_pf_max":
        y_label = "110 Pole Figure Maxima (mrd)"
        
    elif texture_strength_type == "111_pf_max":
        y_label = "111 Pole Figure Maxima (mrd)"
        
    ax1.minorticks_on()
    ax1.plot(ebsd_results["image_number"], ebsd_results[texture_strength_type], color = colour[0], linewidth = 4)
    ax1.set_xlabel("Scan Number", fontsize = 30)
    ax1.set_ylabel(y_label, fontsize = 30)

    ax2.minorticks_on()
    ax2.plot(cpf_results["image_number"], cpf_results[texture_strength_type], color = colour[1], linewidth = 4)
    ax2.set_xlabel("Scan Number", fontsize = 30)
    ax2.set_ylabel(y_label, fontsize = 30)

    ax3.minorticks_on()
    ax3.plot(maud_results["image_number"], maud_results[texture_strength_type], color = colour[2], linewidth = 4)
    ax3.set_xlabel("Scan Number", fontsize = 30)
    ax3.set_ylabel(y_label, fontsize = 30)

    title = "i) EBSD \t\t\t  ii) Fourier Peak Analysis \t\t\t    iii) MAUD".expandtabs()
    fig.suptitle(title, x = 0.515, y = 0.97, fontsize = 36)

    fig.tight_layout()
    fig.savefig(f"{output_folder}{sxrd_experiment_number}_{phase}_{texture_strength_type}.png")
    
    print(f"Figure saved to: {output_folder}{sxrd_experiment_number}_{phase}_{texture_strength_type}.png")

def plot_sxrd_map(sxrd_experiment_number: int, phase: str, texture_strength_type: str, output_folder: str, 
                  cpf_results: dict, c_map: str, v_min: int, v_max: int):
    """Plot 2D map of SXRD pole figure intensities, as well as 
    texture strength, in X,Y positions,from SXRD texture results 
    refined using Continuous-Peak-Fit. Options available to select 
    phase (alpha or beta) and type of texture strength being plotted 
    i.e. texture index, ODF maxima, or pole figure maxima for different 
    alpha/beta lattice planes.
    
    :param sxrd_experiment_number: Experiment number for the SXRD test.
    :param phase: Phase (alpha or beta) used to label output folder.
    :param texture_strength_type: Type of texture strength variable being plotted 
    (choose from texture_index, odf_max, 0002_pf_max, 10-10_pf_max, 11-20_pf_max, 001_pf_max, 110_pf_max, 111_pf_max).
    :param output_folder: File path to the output folder.
    :param cpf_results: Dictionary containing arrays of SXRD texture results, refined using Continuous-Peak-Fit.
    :param c_map: Colour of the map i.e. Reds, Blues, Greens, etc.
    :param v_min: Set minimum value of the colour scale.
    :param v_max: Set maximum value of the colour scale.
    """
    fig, ax = plt.subplots(figsize=(20, 10))
    cpf_texture_strength = np.array(cpf_results[texture_strength_type])
    shape = (9, 41)
    image = ax.imshow(cpf_texture_strength.reshape(shape), interpolation='nearest', cmap = c_map, vmin = v_min, vmax = v_max, extent=[0,20,0,4])
    ax.set_xlabel("X (mm)", fontsize = 25)
    ax.set_ylabel("Y (mm)", fontsize = 25, rotation = 0, labelpad=50)
    plt.colorbar(image, ax=ax, location = 'top', shrink = 0.4)
    fig.tight_layout()
    fig.savefig(f"{output_folder}{sxrd_experiment_number}_{phase}_{texture_strength_type}_SXRD_map.png")
    
    print(f"Figure saved to: {output_folder}{sxrd_experiment_number}_{phase}_{texture_strength_type}_SXRD_map.png")
    
def plot_texture_strength_two_phase(output_folder: str, sxrd_experiment_number: int, 
                                    alpha_results: dict, beta_results: dict, 
                                    texture_strength_type: str,  fitting_type: str,
                                    x_min: int, x_max: int, y_min: int, y_max: int):
    """Plot texture strength versus image (scan) number
    for EBSD, SXRD-CPF and SXRD-MAUD texture results for both 
    alpha and beta phases. Options available to plot thw type 
    of texture strength being plotted i.e. texture index or 
    ODF maxima.
    
    :param output_folder: File path to the output folder.
    :param sxrd_experiment_number: Experiment number for the SXRD test.
    :param alpha_results: Dictionary containing arrays of EBSD, SXRD-CPF, or SXRD-MAUD alpha-phase texture results.
    :param beta_results: Dictionary containing arrays of EBSD, SXRD-CPF, or SXRD-MAUD beta-phase texture results.
    :param texture_strength_type: Type of texture strength variable being plotted (choose from texture_index, odf_max).
    :param fitting_type: Choose either 'ebsd, 'cpf', or 'maud' to signify the data analysis (fitting) used.
    :param x_min: Minimum value for the x-axis.
    :param x_max: Maximum value for the x-axis.
    :param y_min: Minimum value for the y-axis.
    :param y_max: Maximum value for the y-axis.
    """
    plt.rc('xtick', labelsize = 24)
    plt.rc('ytick', labelsize = 24)
    plt.rc('legend', fontsize = 20)
    plt.rc('axes', linewidth = 2)
    plt.rc('xtick.major', width = 2, size = 10)
    plt.rc('xtick.minor', width = 2, size = 5)
    plt.rc('ytick.major', width = 2, size = 10)
    plt.rc('ytick.minor', width = 2, size = 5)
    
    fig, ax = plt.subplots(1, 1, figsize = (20, 7))
    
    if texture_strength_type == "texture_index":
        y_label = "Texture Index"
    
    elif texture_strength_type == "odf_max":
        y_label = "ODF Maxima (mrd)"
    
    ax.minorticks_on()
    ax.plot(alpha_results["image_number"], alpha_results[texture_strength_type], color = "red", linewidth = 4, label = r"$\alpha$-phase")
    ax.plot(beta_results["image_number"], beta_results[texture_strength_type], color = "blue", linewidth = 4, label = r"$\beta$-phase")
    ax.set_xlabel("Scan Number", fontsize = 30)
    ax.set_ylabel(y_label, fontsize = 30)
    ax.legend(loc="upper left", fontsize = 30)
    ax.set_xlim(x_min,x_max)
    ax.set_ylim(y_min,y_max)

    fig.tight_layout()
    fig.savefig(f"{output_folder}{fitting_type}/{sxrd_experiment_number:03d}_{texture_strength_type}_{fitting_type}.png")
    
    print(f"Figure saved to: {output_folder}{fitting_type}/{sxrd_experiment_number:03d}_{texture_strength_type}_{fitting_type}.png")
    
def plot_pf_intensity_two_phase(output_folder: str, sxrd_experiment_number: int, 
                                phase: str, results: dict, fitting_type: str,
                                x_min: int, x_max: int, y_min: int, y_max: int):
    """Plot pole figure intensity maxima for multiple lattice planes
    versus image (scan) number for EBSD, SXRD-CPF and SXRD-MAUD texture 
    results for either alpha or beta phases. Options available to plot 
    the type of texture strength being plotted i.e. texture index or 
    ODF maxima.
    
    :param output_folder: File path to the output folder.
    :param sxrd_experiment_number: Experiment number for the SXRD test.
    :param phase: Choose the phase, either 'alpha' or 'beta', to set the lattice plane peaks.
    :param results: Dictionary containing arrays of EBSD, SXRD-CPF, or SXRD-MAUD texture results for either alpha or beta phases.
    :param fitting_type: Choose either 'ebsd, 'cpf', or 'maud' to signify the data analysis (fitting) used.
    :param x_min: Minimum value for the x-axis.
    :param x_max: Maximum value for the x-axis.
    :param y_min: Minimum value for the y-axis.
    :param y_max: Maximum value for the y-axis.
    """
    fig, ax = plt.subplots(1, 1, figsize = (12.5, 10))
    
    if phase == "alpha":
    
        ax.minorticks_on()
        ax.plot(results["image_number"], results["0002_pf_max"], color = "red", linewidth = 4, label = "{0002}")
        ax.plot(results["image_number"], results["11-20_pf_max"], color = "red", linewidth = 4, alpha = 0.5, label = "{11-20}")
        ax.plot(results["image_number"], results["10-10_pf_max"], color = "red", linewidth = 4, alpha = 0.2, label = "{10-10}")
        ax.set_xlabel("Scan Number", fontsize = 30)
        ax.set_ylabel("Pole Figure Maxima (mrd)", fontsize = 30)
        ax.legend(loc="upper right", fontsize = 30)
        ax.set_xlim(x_min,x_max)
        ax.set_ylim(y_min,y_max)

        title = r"a) $\alpha$-phase".expandtabs()
        fig.suptitle(title, x = 0.515, y = 0.97, fontsize = 36)

    elif phase == "beta":
    
        ax.minorticks_on()
        ax.plot(results["image_number"], results["110_pf_max"], color = "blue", linewidth = 4, label = "{110}")
        ax.plot(results["image_number"], results["001_pf_max"], color = "blue", linewidth = 4, alpha = 0.5, label = "{001}")
        ax.plot(results["image_number"], results["111_pf_max"], color = "blue", linewidth = 4, alpha = 0.2, label = "{111}")
        ax.set_xlabel("Scan Number", fontsize = 30)
        ax.set_ylabel("Pole Figure Maxima (mrd)", fontsize = 30)
        ax.legend(loc="upper left", fontsize = 30)
        ax.set_xlim(x_min,x_max)
        ax.set_ylim(y_min,y_max)

        title = r"b) $\beta$-phase".expandtabs()
        fig.suptitle(title, x = 0.515, y = 0.97, fontsize = 36)
        
    fig.tight_layout()
    fig.savefig(f"{output_folder}{fitting_type}/{sxrd_experiment_number:03d}_{phase}_pf_max_{fitting_type}.png")
    
    print(f"Figure saved to: {output_folder}{fitting_type}/{sxrd_experiment_number:03d}_{phase}_pf_max_{fitting_type}.png")