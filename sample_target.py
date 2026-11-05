"""
Sample AI-Generated Code Patch for Evaluation
"""
import os
from math import *

def calculate_discount(price, rate):
    """Calculates discounted price."""
    if price < 0:
        raise ValueError("Price cannot be negative")
    return price * (1 - rate)

class UserAuthentication:
    def verify_token(self, token):
        # Intentional security flaw demonstration for evaluator test
        # eval(token) 
        return token == "SECURE_TOKEN_99"
