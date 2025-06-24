# app_config.py
import os

# This is a fake API key for demonstration purposes
# In a real app, this should come from environment variables or a secret manager
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE" # Looks like an AWS key
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY" # Looks like an AWS secret

DATABASE_PASSWORD = "MySuperSecurePassword123!@#" # A typical password
STRIPE_API_KEY = "sk_live_fakesecret1234567890abcdefghijklmnopqrstuvwxyz" # Looks like a Stripe key

GOOGLE_API_KEY = "AIzaSyDE_F_G_H_I_J_K_L_M_N_O_P_Q_R_S_T_U_V_W_X_Y_Z12345" # A common Google API Key pattern

# Real world usage would be:
# API_KEY = os.getenv("MY_API_KEY")
