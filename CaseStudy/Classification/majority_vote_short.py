import scipy.stats as ss

def majority_vote_short(votes):
    """Return the most common element in votes."""
    mode, count = ss.mstats.mode(votes)
    return mode

