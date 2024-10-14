import pandas as pd

def calculate_points(df):
    # Initialize points column
    df['points'] = 0
    
    # Stage 1: Posting a complaint (200 points per complaint)
    df['points'] += df['complaints'] * 200
    
    # Stage 2: Complaint approval (500 points per approved complaint)
    df['points'] += df['approved_complaints'] * 500
    
    # Stage 3: Complaint resolution (1000 points per resolved complaint)
    df['points'] += df['resolved_complaints'] * 1000
    
    # Additional points based on likes (10 points per like)
    df['points'] += df['likes'] * 10
    
    return df
