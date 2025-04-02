# modules/reporting.py

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import pandas as pd

def generate_and_export_report(exploration_results, model_results, output_path):
    """
    Generates a PDF report of the analysis results.

    Parameters:
        exploration_results (dict): Paths to generated plots.
        model_results (dict): Model evaluation metrics.
        output_path (str): The file path to save the report.
    """
    try:
        print("Generating PDF report...")
        c = canvas.Canvas(output_path, pagesize=letter)
        width, height = letter
        
        # Title
        c.setFont("Helvetica-Bold", 16)
        c.drawString(72, height - 72, "Data Analysis Report")
        
        # Add plots
        y_position = height - 100
        for plot_title, plot_path in exploration_results.items():
            c.setFont("Helvetica", 12)
            c.drawString(72, y_position, plot_title.replace('_', ' ').title())
            y_position -= 20
            img = ImageReader(plot_path)
            c.drawImage(img, 72, y_position - 200, width=400, height=200)
            y_position -= 220
        
        # Add model results
        c.setFont("Helvetica-Bold", 14)
        c.drawString(72, y_position - 20, "Model Evaluation Metrics")
        y_position -= 40
        
        c.setFont("Helvetica", 12)
        report_df = pd.DataFrame(model_results['classification_report']).transpose()
        report_text = report_df.to_string()
        text_object = c.beginText(72, y_position)
        for line in report_text.split('\n'):
            text_object.textLine(line)
        c.drawText(text_object)
        
        # Save the PDF
        c.save()
        print("Report saved to {}.".format(output_path))
    except Exception as e:
        print("An error occurred during report generation: {}".format(e))

