# src/evaluation.py
import numpy as np

# Example: Mean Average Precision (MAP)
def mean_average_precision(recommended, relevant):
    """
    Calculate MAP for a single user.
    """
    relevant_set = set(relevant)
    ap = 0.0
    num_hits = 0
    for i, rec in enumerate(recommended):
        if rec in relevant_set:
            num_hits += 1
            ap += num_hits / (i + 1)
    return ap / len(relevant_set)

# Example: Click-through Rate (CTR)
def click_through_rate(clicks, impressions):
    return clicks / impressions
