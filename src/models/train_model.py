# Importing Libraries

import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

from sklearn.linear_model import LinearRegression

TRAIN_DATA = os.path.join(
    os.path.dirname(__file__),
    "D:\Experiment\ML Model Deployment With Flask API\salary_estimation\data\processed\\final_hiring.csv",
)
MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "D:\Experiment\ML Model Deployment With Flask API\salary_estimation\models\model.pkl",
)


def run_experiment(save_model: bool = False):
    hiring_data_processed = pd.read_csv(TRAIN_DATA)
    features = hiring_data_processed.iloc[:, :3]  # selecting all rows but three columns
    target = hiring_data_processed.iloc[:, -1]  # selecting all rows but last column
    regressor = LinearRegression()
    regressor.fit(features, target)

    if save_model:
        pickle.dump(regressor, open(MODEL_PATH, "wb"))


def main():
    run_experiment(save_model=True)


if __name__ == "__main__":
    main()
