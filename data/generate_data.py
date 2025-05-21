# Save this as generate_data.py (optional helper script)
import pandas as pd
import random

random.seed(42)
heights = [random.randint(60, 76) for _ in range(100)]  # heights in inches
tall = [1 if h > 66 else 0 for h in heights]            # label: 1 if height > 66 inches

df = pd.DataFrame({
    'height': heights,
    'tall': tall
})

df.to_csv('heights.csv', index=False)

print("Dataset created at ml_app/data/heights.csv")
