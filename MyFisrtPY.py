import pandas as pd

def read_data(file_path):
    try:
            df = pd.read_csv(file_path)
    except FileNotFoundError:
            print("file not found")

read_data("path")