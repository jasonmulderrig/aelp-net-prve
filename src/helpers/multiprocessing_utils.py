from src.networks.aelp_networks import (
    aelp_L,
    aelp_network_local_topological_descriptor,
    aelp_network_global_topological_descriptor,
    aelp_network_global_morphological_descriptor
)
from src.networks.auelp_networks import auelp_network_topology
from src.networks.abelp_networks import abelp_network_topology
from src.networks.apelp_networks import apelp_network_topology
from src.helpers.node_placement_utils import initial_node_seeding

def run_aelp_L(args):
    aelp_L(*args)

def run_initial_node_seeding(args):
    initial_node_seeding(*args)

def run_auelp_network_topology(args):
    auelp_network_topology(*args)

def run_abelp_network_topology(args):
    abelp_network_topology(*args)

def run_apelp_network_topology(args):
    apelp_network_topology(*args)

def run_aelp_network_local_topological_descriptor(args):
    aelp_network_local_topological_descriptor(*args)

def run_aelp_network_global_topological_descriptor(args):
    aelp_network_global_topological_descriptor(*args)

def run_aelp_network_global_morphological_descriptor(args):
    aelp_network_global_morphological_descriptor(*args)