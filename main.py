# main.py

from modules.data_ingestion import load_and_clean_data
from modules.data_visualization import explore_data
from modules.data_modeling import model_data
from modules.reporting import generate_and_export_report
import os

def main():
    print("Starting Modular Data Analysis Tool...\n")
    # Step 1: Create the output directories
    os.makedirs('output/plots', exist_ok=True)
    
    # Step 2: Data Ingestion and Preprocessing
    data = load_and_clean_data('data/input_dataset.csv')
    if data is None:
        print("Data ingestion failed. Exiting.")
        return
    print("Data ingestion and preprocessing completed.\n")
    
    # Step 3: Data Exploration and Visualization
    exploration_results = explore_data(data)
    print("Data exploration and visualization completed.\n")
    
    # Step 4: Data Modeling and Analysis
    model_results = model_data(data)
    print("Data modeling and analysis completed.\n")
    
    # Step 5: Reporting and Exporting Results
    generate_and_export_report(exploration_results, model_results, 'output/final_report.pdf')
    print("Reporting and exporting results completed.\n")
    
    print("Data analysis workflow completed successfully.")

if __name__ == '__main__':
    main()

