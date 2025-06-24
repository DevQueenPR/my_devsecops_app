# app.py
from PIL import Image # Import Pillow to ensure it's part of the dependency graph

def run_app():
    print("DevSecOps app container is starting...")
    # Simulate some app logic that might use Pillow
    try:
        img = Image.new('RGB', (1, 1)) # Simple use of Pillow
        print("Pillow imported and used.")
    except Exception as e:
        print(f"Error using Pillow: {e}")
    print("DevSecOps app container finished.")

if __name__ == "__main__":
    run_app()
