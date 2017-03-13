import numpy as np
import scipy.stats as ss

def generate_synth_data(n = 50):
    """Create two sets of points from bivariate normal distributions."""
    points = np.concatenate((ss.norm(0, 1).rvs((n, 2)), ss.norm(1, 1).rvs((n, 2))), axis = 0)
    outcomes = np.concatenate((np.repeat(0, n), np.repeat(1, n)))
    return (points, outcomes) 
