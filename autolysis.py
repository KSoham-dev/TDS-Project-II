# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "matplotlib",
#     "pandas",
#     "requests",
#     "seaborn",
#     "tabulate",
#     "scipy"
# ]
# ///

#-----------------------------------------------------
# Setting up important imports 
#-----------------------------------------------------
import itertools
import os
import sys
import logging
import base64
from typing import Tuple, Dict, Any, List

import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency
from tabulate import tabulate

#-----------------------------------------------------
# Configuring logging
#-----------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

#-----------------------------------------------------
# Constants
#-----------------------------------------------------
API_URL = "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions"
MODEL_NAME = "gpt-4o-mini"
SIGNIFICANCE_LEVEL = 0.05

#-----------------------------------------------------
# Function to load the dataset
#-----------------------------------------------------
def load_dataset(file: str) -> Tuple[pd.DataFrame, str]:
    """
    Loads a dataset from a CSV file with fallback encodings.

    Args:
        file (str): Path to the CSV file.

    Returns:
        Tuple[pd.DataFrame, str]: Loaded DataFrame and folder name.
    """
    folder = os.path.splitext(os.path.basename(file))[0]
    os.makedirs(folder, exist_ok=True)
    for encoding in ['utf-8', 'ISO-8859-1', 'windows-1252']:
        try:
            df = pd.read_csv(file, encoding=encoding)
            logging.info(f"Loaded file '{file}' with encoding '{encoding}'.")
            return df, folder
        except UnicodeDecodeError:
            logging.warning(f"Failed to load with encoding '{encoding}'. Trying next encoding.")
    logging.error("All encoding attempts failed.")
    raise UnicodeDecodeError("Failed to decode the file with supported encodings.")

#-----------------------------------------------------
# Function to analyze missing values
#-----------------------------------------------------
def analyze_missing_values(df: pd.DataFrame) -> str:
    """
    Analyzes missing values in the DataFrame.

    Args:
        df (pd.DataFrame): Input DataFrame.

    Returns:
        str: Markdown table of missing value analysis.
    """
    missing_summary = df.isnull().sum().reset_index()
    missing_summary.columns = ['Column', 'Missing Values']
    missing_summary['Percentage'] = (missing_summary['Missing Values'] / len(df) * 100).round(2)
    logging.info("Analyzed missing values.")
    return tabulate(missing_summary, headers='keys', tablefmt='pipe', showindex=False)

#-----------------------------------------------------
# Function to handle missing values
#-----------------------------------------------------
def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Handles missing values by filling numeric columns with their mean.

    Args:
        df (pd.DataFrame): Input DataFrame.

    Returns:
        pd.DataFrame: DataFrame with missing values handled.
    """
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
    logging.info("Filled missing values in numeric columns with mean.")
    return df

#-----------------------------------------------------
# Function to generate advanced statistics
#-----------------------------------------------------
def generate_advanced_statistics(df: pd.DataFrame) -> str:
    """
    Generates advanced statistics including skewness and kurtosis.

    Args:
        df (pd.DataFrame): Input DataFrame.

    Returns:
        str: Markdown table of advanced statistics.
    """
    numeric_cols = df.select_dtypes(include=[np.number])
    if numeric_cols.empty:
        logging.warning("No numeric data available for statistical analysis.")
        return "No numeric data available for statistical analysis."

    stats = numeric_cols.describe().T
    stats['Skewness'] = numeric_cols.skew()
    stats['Kurtosis'] = numeric_cols.kurtosis()
    stats = stats[['mean', 'std', 'min', '25%', '50%', '75%', 'max', 'Skewness', 'Kurtosis']].round(2)
    logging.info("Generated advanced statistics.")
    return tabulate(stats, headers='keys', tablefmt='pipe')

#-----------------------------------------------------
# Function to perform chi-square test for all 
# categorical columns and generate markdown 
# reports
#-----------------------------------------------------
def chi_square_tests_all_categorical(df: pd.DataFrame) -> Dict[Tuple[str, str], str]:
    """
    Performs chi-square tests on all pairs of categorical columns and generates markdown table reports.

    Args:
        df (pd.DataFrame): The dataframe containing the data.

    Returns:
        Dict[Tuple[str, str], str]: Dictionary with column pairs as keys and markdown reports as values.
    """
    categorical_cols = df.select_dtypes(include=['object']).columns
    reports = {}

    for col1, col2 in itertools.combinations(categorical_cols, 2):
        try:
            contingency_table = pd.crosstab(df[col1], df[col2])
            chi2, p, dof, expected = chi2_contingency(contingency_table)
            significance = 'Significant' if p < SIGNIFICANCE_LEVEL else 'Not Significant'
            markdown_report = f"""
| Metric               | Value               |
|----------------------|---------------------|
| Chi-Square Statistic | {chi2:.4f}           |
| p-value              | {p:.4f}             |
| Degrees of Freedom   | {dof}                |
| Interpretation       | {significance}      |

"""
            reports[(col1, col2)] = markdown_report
            logging.info(f"Performed chi-square test for {col1} vs {col2}.")
        except Exception as e:
            reports[(col1, col2)] = f"Error performing chi-square test: {e}"
            logging.error(f"Error performing chi-square test for {col1} vs {col2}: {e}")

    return reports

#-----------------------------------------------------
# Function to send request to LLM
#-----------------------------------------------------
def send_llm_request(messages: List[Dict[str, Any]]) -> str:
    """
    Sends a request to the LLM using the provided messages and returns the response content.

    Args:
        messages (List[Dict[str, Any]]): The messages to be sent to the LLM.

    Returns:
        str: The main content returned by the LLM.
    """
    try:
        API_KEY = os.environ.get("AIPROXY_TOKEN")
        if not API_KEY:
            logging.error("API key 'AIPROXY_TOKEN' not found in environment variables.")
            return "LLM request failed. API key is missing."

        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }

        data = {
            "model": MODEL_NAME,
            "messages": messages
        }

        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()
        content = response.json()["choices"][0]["message"]["content"]
        logging.info("Received response from LLM.")
        logging.info(response.json())
        return content
    except requests.exceptions.RequestException as e:
        logging.error(f"Error during API request: {e}")
        return "LLM request failed. Please try again later."

#-----------------------------------------------------
# Function to get domain of the data
#-----------------------------------------------------
def get_domain(df: pd.DataFrame) -> str:
    """
    Determines the domain based on column names using LLM.

    Args:
        df (pd.DataFrame): Input DataFrame.

    Returns:
        str: Determined domain.
    """
    messages = [
        {"role": "system", "content": "Determine the domain based on column names in the data in only one word."},
        {"role": "user", "content": str(df.columns)}
    ]
    domain = send_llm_request(messages)
    logging.info(f"Determined domain: {domain}")
    return domain

#-----------------------------------------------------
# Function to build messages for LLM analysis
#-----------------------------------------------------
def build_msgs(text: str, img: str) -> List[Dict[str, Any]]:
    """
    Generates the 'messages' parameter for the request body using the provided prompt and encoded image.

    Args:
        text (str): The input prompt.
        img (str): The encoded image data.

    Returns:
        List[Dict[str, Any]]: Messages list for the LLM.
    """
    return [{
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": text,
            },
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{img}",
                    "detail": "low"
                },
            },
        ],
    }]
    
#-----------------------------------------------------
# Function to create histograms
#-----------------------------------------------------
def create_histogram(df: pd.DataFrame, folder: str) -> None:
    """
    Creates and saves histograms for numerical features.

    Args:
        df (pd.DataFrame): Input DataFrame.
        folder (str): Folder to save the histogram.
    """
    df.hist(bins=100, figsize=(14, 14))
    plt.suptitle('Histogram of Numerical Features', fontsize=16)
    plt.xlabel('Values', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.legend([f'{col}' for col in df.select_dtypes(include=['number']).columns])
    plt.tight_layout()
    histogram_path = os.path.join(folder, 'histogram.png')
    plt.savefig(histogram_path)
    plt.close()
    logging.info(f"Saved histogram to {histogram_path}.")

#-----------------------------------------------------
# Function to create box plots
#-----------------------------------------------------
def create_box_plots(df: pd.DataFrame, folder: str) -> None:
    """
    Creates and saves box plots for numerical features.

    Args:
        df (pd.DataFrame): Input DataFrame.
        folder (str): Folder to save the box plots.
    """
    sns.set_theme(style="whitegrid")
    fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(14, 14))
    fig.suptitle('Box Plots of Variables', fontsize=16)
    axes = axes.flatten()
    variables = df.select_dtypes(include=['number']).columns.tolist()

    for ax, var in zip(axes, variables):
        sns.boxplot(data=df[var], ax=ax)
        ax.set_title(f'Box Plot of {var.capitalize()}', fontsize=14)
        ax.set_xlabel(var.capitalize(), fontsize=12)
        ax.set_ylabel('Values', fontsize=12)

    for i in range(len(variables), len(axes)):
        fig.delaxes(axes[i])

    plt.tight_layout()
    plt.subplots_adjust(top=0.9)
    plt.legend(variables, loc='upper right')
    box_plot_path = os.path.join(folder, 'box_plot.png')
    plt.savefig(box_plot_path)
    plt.close()
    logging.info(f"Saved box plots to {box_plot_path}.")

#-----------------------------------------------------
# Function to create correlation heatmap
#-----------------------------------------------------
def create_correlation_heatmap(df: pd.DataFrame, folder: str) -> None:
    """
    Creates and saves a correlation heatmap for numerical features.

    Args:
        df (pd.DataFrame): Input DataFrame.
        folder (str): Folder to save the heatmap.
    """
    variables = df.select_dtypes(include=['number']).columns.tolist()
    fig, ax = plt.subplots(figsize=(14, 14))
    sns.heatmap(df.loc[:, variables].corr(), annot=True, fmt=".2f", cmap='coolwarm')
    plt.title('Correlation Heatmap of Numerical Features', fontsize=16)
    plt.xlabel('Features', fontsize=12)
    plt.ylabel('Features', fontsize=12)
    heatmap_path = os.path.join(folder, 'corr_hmap.png')
    plt.tight_layout()
    plt.savefig(heatmap_path)
    plt.close()
    logging.info(f"Saved correlation heatmap to {heatmap_path}.")

#-----------------------------------------------------
# Function to perform LLM analysis
#-----------------------------------------------------
def perform_llm_analysis(images: Dict[str, str], folder: str) -> Dict[str, str]:
    """
    Performs LLM analysis on the provided images.

    Args:
        images (Dict[str, str]): Dictionary of image types and their paths.
        folder (str): Folder where images are stored.

    Returns:
        Dict[str, str]: Analysis results from LLM.
    """
    analyses = {}
    for img_type, img_path in images.items():
        try:
            with open(os.path.join(folder, img_path), "rb") as image_file:
                img_enc = base64.b64encode(image_file.read()).decode("utf-8")

            if img_type == "histogram":
                text = "This figure contains histograms from df.hist(). Provide a detailed analysis in an interesting way."
            elif img_type == "box_plot":
                text = "This figure contains box-plots. Provide a detailed analysis in an interesting way."
            elif img_type == "corr_hmap":
                text = "This figure contains a correlation heatmap. Provide a detailed analysis in an interesting way."
            else:
                text = "Provide an analysis for this image."

            messages = build_msgs(text, img_enc)
            analyses[img_type] = send_llm_request(messages)
            logging.info(f"Performed LLM analysis for {img_type}.")
        except FileNotFoundError:
            analyses[img_type] = "Image file not found for analysis."
            logging.error(f"Image file {img_path} not found in folder {folder}.")
        except Exception as e:
            analyses[img_type] = f"Error during LLM analysis: {e}"
            logging.error(f"Error during LLM analysis for {img_type}: {e}")

    return analyses

#-----------------------------------------------------
# Function to create README.md content
#-----------------------------------------------------
def create_readme_content(
    df: pd.DataFrame,
    folder: str,
    domain: str,
    adv_stat_mdt: str,
    analyses: Dict[str, str],
    missing_mdt: str,
    chi_square_reports: Dict[Tuple[str, str], str]
) -> None:
    """
    Creates and writes README.md content based on the analysis.

    Args:
        df (pd.DataFrame): Input DataFrame.
        folder (str): Folder to save README.md.
        domain (str): Determined domain of the data.
        adv_stat_mdt (str): Advanced statistics in markdown.
        analyses (Dict[str, str]): LLM analyses.
        missing_mdt (str): Missing values analysis in markdown.
        chi_square_reports (Dict[Tuple[str, str], str]): Chi-square test reports.
    """
    content = f"""
# Data Analysis Project

Hey! Hope you are doing fine. Hmm... You've got some interesting data I see.  
Let's begin this journey by first identifying what your data is like.  
So, you have {df.shape[0]} rows and {df.shape[1]} columns in your data, and as I can  
see, this data is related to {domain}. Below are some key statistics  
about the data you provided:

## Missing Value Analysis
The dataset contains the following missing values:

{missing_mdt}

## Advanced Statistical Analysis
{adv_stat_mdt}  

Let's move a little deeper and see what wonders the data is yet to reveal.

## Visualizing Data
### Correlation Heatmap
Understanding how numerical columns correlate with each other can provide insights into potential relationships and dependencies between variables. Here's a heatmap showing these correlations:

![Correlation Heatmap](./corr_hmap.png)

**Analysis for Correlation Heatmap:**

{analyses.get('corr_hmap', 'No analysis available.')}

### Histograms
Histograms help us understand the distribution of numerical columns. They can reveal patterns such as skewness, modality, and the presence of outliers. Here's a look at the histograms for the numerical columns:

![Histograms](./histogram.png)

**Analysis for Histograms:**

{analyses.get('histogram', 'No analysis available.')}

### Box Plots
Box plots are useful for identifying outliers and understanding the spread and central tendency of the data. Here's a look at the box plots for the numerical columns:

![Box Plots](./box_plot.png)

**Analysis for Box Plots:**

{analyses.get('box_plot', 'No analysis available.')}

## Chi-Square Test Reports
Chi-square tests help us understand the relationships between categorical variables. Here are the results of the chi-square tests for pairs of categorical columns:
"""

    for cols, report in chi_square_reports.items():
        content += f"\n### Chi-Square Test for {cols[0]} and {cols[1]}\n{report}\n"

    readme_path = os.path.join(folder, 'README.md')
    try:
        with open(readme_path, 'w') as file:
            file.write(content)
        logging.info(f"Created README.md at {readme_path}.")
    except Exception as e:
        logging.error(f"Failed to write README.md: {e}")

#-----------------------------------------------------
# Main function to execute the script
#-----------------------------------------------------
def main(file: str) -> None:
    """
    Main function to execute the data analysis script.

    Args:
        file (str): Path to the CSV file.
    """
    try:
        df, folder = load_dataset(file)
        df = handle_missing_values(df)
        missing_mdt = analyze_missing_values(df)
        adv_stat_mdt = generate_advanced_statistics(df)
        create_histogram(df, folder)
        create_box_plots(df, folder)
        create_correlation_heatmap(df, folder)
        domain = get_domain(df)
        images = {
            "histogram": "histogram.png",
            "box_plot": "box_plot.png",
            "corr_hmap": "corr_hmap.png"
        }
        analyses = perform_llm_analysis(images, folder)
        chi_square_reports = chi_square_tests_all_categorical(df)
        create_readme_content(df, folder, domain, adv_stat_mdt, analyses, missing_mdt, chi_square_reports)
        logging.info("Data analysis completed successfully.")
    except Exception as e:
        logging.error(f"An error occurred during data analysis: {e}")

#-----------------------------------------------------
# Entry point of the script
#-----------------------------------------------------
if __name__ == "__main__":
    if len(sys.argv) != 2:
        logging.error("Usage: python autolysis.py <path_to_csv_file>")
        sys.exit(1)
    file_path = sys.argv[1]
    main(file_path)