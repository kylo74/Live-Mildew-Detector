import streamlit as st
from app_pages.multi_page import Multipage

# load pages script
from app_pages.page_summary import page_summary_body
from app_pages.page_leaves_visualiser import page_leaves_visualiser_body
from app_pages.page_mildew_detector import page_mildew_detector_body
from app_pages.page_ml_performance import page_ml_performance_metrics
from app_pages.page_project_hypothesis import page_project_hypothesis_body

app = Multipage(app_name= "Mildew detector") # Create instance of app

# Add app pages
app.add_page("Project Summary", page_summary_body)
app.add_page("Leaves Visualiser", page_leaves_visualiser_body)
app.add_page("Detection", page_mildew_detector_body)
app.add_page("Project Hypothesis", page_project_hypothesis_body)
app.add_page("Ml Performance Metrics", page_ml_performance_metrics)

app.run() # Run app