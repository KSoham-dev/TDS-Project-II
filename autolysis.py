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
import requests
import pandas as pd
import os
import numpy as np
import sys
import matplotlib.pyplot as plt
import seaborn as sns
import base64
from scipy.stats import chi2_contingency

#-----------------------------------------------------
# Function to load the dataset
#-----------------------------------------------------
def load_dataset(file):
    folder = os.path.splitext(os.path.basename(file))[0]
    os.makedirs(folder, exist_ok=True)
    try:
        df = pd.read_csv(file, encoding='utf-8')
    except UnicodeDecodeError:
        try:
            df = pd.read_csv(file, encoding='ISO-8859-1')
        except UnicodeDecodeError:
            df = pd.read_csv(file, encoding='windows-1252')
    return df, folder

#-----------------------------------------------------
# Function to analyze missing values
#-----------------------------------------------------
def analyze_missing_values(df):
    """
    Analyzes missing values in the DataFrame.

    Args:
        df (DataFrame): Input DataFrame.

    Returns:
        str: Markdown table of missing value analysis.
    """
    missing_summary = df.isnull().sum().reset_index()
    missing_summary.columns = ['Column', 'Missing Values']
    missing_summary['Percentage'] = (missing_summary['Missing Values'] / len(df) * 100).round(2)
    return missing_summary.to_markdown(index=False)

#-----------------------------------------------------
# Function to handle missing values
#-----------------------------------------------------
def handle_missing_values(df):
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
    return df

def generate_advanced_statistics(df):
    """
    Generates advanced statistics including skewness and kurtosis.

    Args:
        df (DataFrame): Input DataFrame.

    Returns:
        str: Markdown table of advanced statistics.
    """
    numeric_cols = df.select_dtypes(include=[np.number])
    if numeric_cols.empty:
        return "No numeric data available for statistical analysis."

    stats = numeric_cols.describe().T
    stats['Skewness'] = numeric_cols.skew()
    stats['Kurtosis'] = numeric_cols.kurtosis()
    stats = stats[['mean', 'std', 'min', '25%', '50%', '75%', 'max', 'Skewness', 'Kurtosis']].round(2)
    return stats.to_markdown(index=True)


#-----------------------------------------------------
# Function to perform chi-square test for all 
# categorical columns and generate markdown 
# reports
#-----------------------------------------------------

def chi_square_tests_all_categorical(df):
    """
    Performs chi-square tests on all pairs of categorical columns and generates markdown table reports.

    Args:
        df (pd.DataFrame): The dataframe containing the data.

    Returns:
        dict: A dictionary where keys are column pairs and values are markdown table reports of the chi-square test results.
    """
    categorical_cols = df.select_dtypes(include=['object']).columns
    reports = {}

    for i, col1 in enumerate(categorical_cols):
        for col2 in categorical_cols[i+1:]:
            # Create a contingency table
            contingency_table = pd.crosstab(df[col1], df[col2])

            # Perform chi-square test
            chi2, p, dof, expected = chi2_contingency(contingency_table)

            # Generate markdown table report
            markdown_report = f"""
| Metric | Value |
| --- | --- |
| Chi-Square Statistic | {chi2:.4f} |
| p-value | {p:.4f} |
| Degrees of Freedom | {dof} |
| Expected Frequencies | {expected} |
"""

            reports[(col1, col2)] = markdown_report

    return reports

#-----------------------------------------------------
# Function to create histograms
#-----------------------------------------------------
def create_histogram(df, folder):
    df.hist(bins=100, figsize=(14, 14))
    plt.suptitle('Histogram of Numerical Features', fontsize=16)
    plt.xlabel('Values', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.legend([f'{col}' for col in df.select_dtypes(include=['number']).columns])
    plt.savefig(f'./{folder}/histogram.png')
    plt.close()

#-----------------------------------------------------
# Function to create box plots
#-----------------------------------------------------
def create_box_plots(df, folder):
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
    plt.savefig(f'./{folder}/box_plot.png')

#-----------------------------------------------------
# Function to create correlation heatmap
#-----------------------------------------------------
def create_correlation_heatmap(df, folder):
    variables = df.select_dtypes(include=['number']).columns.tolist()
    fig, ax = plt.subplots(figsize=(14, 14))
    sns.heatmap(df.loc[:, variables].corr(), annot=True, fmt=".2f", cmap='coolwarm')
    plt.title('Correlation Heatmap of Numerical Features', fontsize=16)
    plt.xlabel('Features', fontsize=12)
    plt.ylabel('Features', fontsize=12)
    plt.legend(variables, loc='upper right')
    plt.tight_layout()
    plt.savefig(f'./{folder}/corr_hmap.png')

#-----------------------------------------------------
# Function to send request to LLM
#-----------------------------------------------------
def send_llm_request(messages):
    """
    Sends a request to the LLM using the provided message parameter and returns the main content.

    Args:
        messages (str): The message to be sent to the LLM.

    Returns:
        str: The main content returned by the LLM.
    """
    try:
        # Setting up API_KEY and model to be used
        API_KEY = os.environ["AIPROXY_TOKEN"]
        model = "gpt-4o-mini"

        # Setting up request headers 
        headers = {
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
        }
        
        # Setting up request body
        data = {
            "model": model,
            "messages": messages
        }
        url = "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions"
        
        # Sending the request
        r = requests.post(url, headers=headers, json=data)
        r.raise_for_status()  # Check for HTTP request errors
        the_main_thing = r.json()["choices"][0]["message"]["content"]
        return the_main_thing
    except requests.exceptions.RequestException as e:
        print(f"Error during API request: {e}")
        return "LLM request failed. Please try again later."

#-----------------------------------------------------
# Function to get domain of the data
#-----------------------------------------------------
def get_domain(df):
    messages = [
        {"role": "system", "content": "Determine the domain based on column names in the data in only one word"},
        {"role": "user", "content": str(df.columns)}
    ]
    return send_llm_request(messages)

#-----------------------------------------------------
# Function to build messages for LLM analysis
#-----------------------------------------------------
def build_msgs(text, img):
    """
    Generates the 'messages' parameter for the request body using the provided prompt and encoded image.

    Args:
        text (str): The input prompt.
        img (str): The encoded image data.

    Returns:
        (list): A list 'messages' as required by request body.
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
                    "url":  f"data:image/jpeg;base64,{img}",
                    "detail": "low"
                },
            },
        ],
    }]

#-----------------------------------------------------
# Function to perform LLM analysis
#-----------------------------------------------------
def perform_llm_analysis(images, folder):
    analyses = {}
    for img_type, img_path in images.items():
        with open(f"./{folder}/{img_path}", "rb") as image_file:
            img_enc = base64.b64encode(image_file.read()).decode("utf-8")
        if img_type == "histogram":
            text = "This figure contains histograms from df.hist(). Provide a brief analysis in a story-telling way"
        elif img_type == "box_plot":
            text = "This figure contains box-plots. Provide a brief analysis in a story-telling way"
        elif img_type == "corr_hmap":
            text = "This figure contains correlation heatmap. Provide a brief analysis in a story-telling way"
        messages = build_msgs(text, img_enc)
        analyses[img_type] = send_llm_request(messages)
    return analyses

#-----------------------------------------------------
# Function to create README.md content
#-----------------------------------------------------
def create_readme_content(df, folder, domain, adv_stat_mdt, analyses, missing_mdt, chi_square_reports):
    content = f"""
# Data Analysis Project 
Hey! Hope you are doing fine. Hmm... You've got some interesting data I see.  
Let's begin this journey by first identifying what your data is like.  
So, you have got {df.shape[0]} rows and {df.shape[1]} columns in your data, and as I can  
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

![Correlation Heatmap](./corr_hmap.png)\n
  
{analyses['corr_hmap']} 

### Histograms
Histograms help us understand the distribution of numerical columns. They can reveal patterns such as skewness, modality, and the presence of outliers. Here's a look at the histograms for the numerical columns:

![Histograms](./histogram.png)\n
  
{analyses['histogram']}

### Box Plots
Box plots are useful for identifying outliers and understanding the spread and central tendency of the data. Here's a look at the box plots for the numerical columns:

![Box Plots](./box_plot.png)\n
  
{analyses['box_plot']}

## Chi-Square Test Reports
Chi-square tests help us understand the relationships between categorical variables. Here are the results of the chi-square tests for pairs of categorical columns:



"""
    for cols, report in chi_square_reports.items():
        content += f"\n### Chi-Square Test for {cols[0]} and {cols[1]}\n{report}\n"

    with open(f'./{folder}/README.md', 'w') as file:
        file.write(content)

#-----------------------------------------------------
# Main function to execute the script
#-----------------------------------------------------
def main(file):
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
    create_readme_content(df,folder, domain, adv_stat_mdt, analyses, missing_mdt,chi_square_reports)

if __name__ == "__main__":
    file = sys.argv[1]
    main(file)
