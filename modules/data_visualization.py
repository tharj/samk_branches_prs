# modules/data_visualization.py

import matplotlib.pyplot as plt
import seaborn as sns
import os

def explore_data(data):
    """
    Generates descriptive statistics and visualizations.

    Parameters:
        data (pd.DataFrame): The data to explore.

    Returns:
        dict: A dictionary containing paths to generated plots.
    """
    try:
        print("Generating descriptive statistics...")
        stats = data.describe()
        print(stats)

        print("Creating visualizations...")
        plot_paths = {}

        # Histogram of Age
        plt.figure()
        sns.histplot(data['age'], kde=True)
        plt.title('Age Distribution')
        age_plot_path = 'output/plots/age_distribution.png'
        plt.savefig(age_plot_path)
        plot_paths['age_distribution'] = age_plot_path
        plt.close()
        
        # Income vs. Credit Score
        plt.figure()
        sns.scatterplot(x='income', y='credit_score', hue='defaulted', data=data)
        plt.title('Income vs. Credit Score')
        income_credit_plot_path = 'output/plots/income_vs_credit_score.png'
        plt.savefig(income_credit_plot_path)
        plot_paths['income_vs_credit_score'] = income_credit_plot_path
        plt.close()
        
        return plot_paths
    except Exception as e:
        print("An error occurred during data exploration: {}".format(e))
        return {}

