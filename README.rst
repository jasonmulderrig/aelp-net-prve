#################################################################################
periodic representative volume elements of artificial end-linked polymer networks
#################################################################################

A repository of research codes that computationally synthesize and analyze periodic representative volume elements of artificial end-linked polymer networks. The networks of focus include (in alphabetical order): artificial bimodal end-linked polymer networks, artificial polydisperse end-linked polymer networks, and artificial uniform end-linked polymer networks.

*****
Setup
*****

Once the contents of the repository have been cloned or downloaded, the Python virtual environment associated with the project needs to be installed. The installation of this Python virtual environment and some essential packages is handled by the ``virtual-environment-install-master.sh`` Bash script. Before running the script, make sure to change the ``VENV_PATH`` parameter to comply with your personal filetree structure. Alternatively, a Conda environment can be installed with the required packages. All required packages are listed in the ``requirements.txt`` file.

*********
Structure
*********

The core functions in this repository are modularly distributed in Python files that reside in the following source directories:

* ``src/descriptors``
* ``src/file_io``
* ``src/helpers``
* ``src/networks``

The core functions can then be called upon in Python files (or Jupyter notebooks) for various tasks. The following directories contain various Python files that synthesize and analyze the aforementioned types of artificial end-linked polymer networks:

* ``abelp``
* ``apelp``
* ``auelp``

Importantly, configuration settings for each of these networks are stored in an appropriately named sub-directory within the ``configs/networks`` directory (``configs/networks/abelp``, ``configs/networks/apelp``, ``configs/networks/auelp``). Each of these sub-directories contain a YAML file defining a wide variety of parameter configuration settings. Moreover, each of these sub-directories contain two more sub-directories, ``topology`` and ``descriptors``. Within each of these sub-directories are YAML files that define parameter configuration settings specifically related to network topology and descriptor calculations, respectively. The Hydra package is employed to load in the settings from the YAML files.

The following Python files synthesize various artificial end-linked polymer networks and calculate descriptors when run in the order provided:

* In the ``abelp`` directory: ``abelp_networks_topology_synthesis.py`` -> ``abelp_networks_topology_descriptors.py``
* In the ``apelp`` directory: ``apelp_networks_topology_synthesis.py`` -> ``apelp_networks_topology_descriptors.py``
* In the ``auelp`` directory: ``auelp_networks_topology_synthesis.py`` -> ``auelp_networks_topology_descriptors.py``

In addition, several Python files are supplied in the ``abelp``, ``apelp``, and ``auelp`` directories that plot the spatially-embedded structure of a given network and analyze the statistics of various network topological features.

*****
Usage
*****

**Before running any of the code, it is required that the user verify the baseline filepath in the ``filepath_str()`` function of the ``file_io.py`` Python file in the ``file_io`` directory. Note that filepath string conventions are operating system-sensitive.**

*************************
Example timing benchmarks
*************************

The following contains some timing benchmarks for the network synthesis and descriptor Python files on my Dell Inspiron computer with ``cpu_num = 8`` for the ``topology\20250102A`` and ``descriptors\20250102A`` parameter configuration settings:

* ``abelp_networks_topology_synthesis.py`` -> ``abelp_networks_topology_descriptors.py``: ~ 60 seconds (for ``abelp_networks_topology_synthesis.py``) + ~ 15 minutes (for ``abelp_networks_topology_descriptors.py``)
* ``apelp_networks_topology_synthesis.py`` -> ``apelp_networks_topology_descriptors.py``: ~ 45 minutes (for ``apelp_networks_topology_synthesis.py``) + ~ 15 minutes (for ``apelp_networks_topology_descriptors.py``)
* ``auelp_networks_topology_synthesis.py`` -> ``auelp_networks_topology_descriptors.py``: ~ 30 seconds (for ``auelp_networks_topology_synthesis.py``) + ~ 10 minutes (for ``auelp_networks_topology_descriptors.py``)

Note that essentially every type of descriptor is calculated for each network in the descriptor Python files (for the sake of benchmarking).