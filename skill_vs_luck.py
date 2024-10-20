import numpy as np
import matplotlib.pyplot as plt
from tqdm.auto import tqdm

def total_score(
        skill_score: float,
        luck_score: float,
        luck_weight: float = 0.05):
    """
    Calculate the total score of a player given their skill and luck scores.
    Args:
        skill_score (float): The player's skill score.
        luck_score (float): The player's luck score.
        luck_weight (float): The weight of luck in the total score. Default is 0.05.
    
    Returns:
        total_score (float): The player's total score.
    """
    
    return ((1.0-luck_weight) * skill_score) + (luck_weight * luck_score)

def select_top_candidates(total_scores, num_candidates):
    """
    Select the top candidates from a list of total scores.
    Args:
        total_scores (list): A list of total scores.
        num_candidates (int): The number of top candidates to select.

    Returns:
        top_candidates (list): A list of the indices of the top candidates.
    """
    
    return np.argsort(total_scores)[::-1][:num_candidates]

def generate_population_scores(
        population:int=1000000, 
        luck_weight:int=0.05):
    """
    Generate random skill, luck, and total scores for a population of players.
    Args:
        population (int): The number of players in the population. Default is 1,000,000.
        luck_weight (float): The weight of luck in the total score. Default is 0.05.

    Returns:
        skill_scores (np.array): An array of skill scores.
        luck_scores (np.array): An array of luck scores.
        total_scores (np.array): An array of total
    """
    
    skill_scores = np.random.normal(0.5, 0.2, population)
    luck_scores = np.random.normal(0.5, 0.2, population)
    total_scores = total_score(skill_scores, luck_scores, luck_weight)
    return skill_scores, luck_scores, total_scores

def simulate_selection(
        population:int=1000000, 
        num_candidates:int=1000, 
        luck_weight:int=0.05):
    """
    Simulate the selection of top candidates from a population of players.
    Args:
        population (int): The number of players in the population. Default is 1,000,000.
        num_candidates (int): The number of top candidates to select. Default is 1,000.
        luck_weight (float): The weight of luck in the total score. Default is 0.05.

    Returns:
        top_candidates (list): A list of the indices of the top candidates.
        all_candidates (dict): A dictionary of the indices of all candidates.
    """
    
    skill_scores, luck_scores, total_scores = generate_population_scores(population, luck_weight)
    all_candidates = {
        "skill_scores": skill_scores,
        "luck_scores": luck_scores,
        "total_scores": total_scores
    }
    top_candidates = select_top_candidates(total_scores, num_candidates)
    return top_candidates, all_candidates
