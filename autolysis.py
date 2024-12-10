# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "matplotlib",
#     "pandas",
#     "requests",
#     "seaborn",
#     "tabulate"
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

#-----------------------------------------------------
# Getting file from inline arguments and 
# converting it to d DataFrame
#-----------------------------------------------------
file = sys.argv[1]
folder = os.path.splitext(os.path.basename(file))[0]
os.makedirs(folder, exist_ok=True)
try: 
    df = pd.read_csv(file, encoding='utf-8') 
except UnicodeDecodeError: 
    try: 
        df = pd.read_csv(file, encoding='ISO-8859-1') 
    except UnicodeDecodeError: 
        df = pd.read_csv(file, encoding='windows-1252')


#-----------------------------------------------------
# Gets Summary Statistics and converts to 
# markdown table format
#----------------------------------------------------- 
desc = df.describe() 
desc = desc.round(2)
desc = desc.map(lambda x: int(x) if not np.isnan(x) else x)
summary_mdt = desc.to_markdown(index=True)


#-----------------------------------------------------
# Generating three different figures which show
# various aspects of the data 
#----------------------------------------------------- 
# Figure-1: Histogram
df.hist(bins=100, figsize=(14, 14))
plt.savefig(f'./{folder}/histogram.png')
plt.close()

#Figure-2: Box Plot
sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(14, 14))
fig.suptitle('Box Plots of Variables', fontsize=16)
axes = axes.flatten()
variables = df.select_dtypes(include=['number']).columns.tolist()

for ax, var in zip(axes, variables):
    sns.boxplot(data=df[var], ax=ax)
    ax.set_title(f'Box Plot of {var.capitalize()}', fontsize=14)
    ax.set_xlabel(var.capitalize(), fontsize=12)


for i in range(len(variables), len(axes)):
    fig.delaxes(axes[i])

plt.tight_layout()
plt.subplots_adjust(top=0.9)
plt.savefig(f'./{folder}/box_plot.png')

#Figure-3
fig, ax = plt.subplots(figsize=(14, 14)) 
sns.heatmap(df.loc[:,variables].corr(), annot=True, fmt=".2f")
plt.tight_layout()
plt.savefig(f'./{folder}/corr_hmap.png')


#-----------------------------------------------------
# Consulting LLM
#----------------------------------------------------- 
# Defining a useful request function
def send_llm_request(messages):
    """
    Sends a request to the LLM using the provided message parameter and returns the main content.

    Args:
        messages (str): The message to be sent to the LLM.

    Returns:
        str: The main content returned by the LLM.
    """

    
    # Setting up API_KEY and model to be used
    API_KEY = os.environ["AIPROXY_TOKEN"]
    model = "gpt-4o-mini"

    #Setting up request headers 
    headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
    }
    
    #Setting up request body
    data = {
        "model": model,
        "messages": messages
    }
    url = "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions"
    
    #Setting out the request
    r = requests.post(url,headers=headers,json=data)
    the_main_thing = r.json()["choices"][0]["message"]["content"]
    return the_main_thing
    
#Getting domain of the data
messages = [
    {"role": "system", "content": "Determine the domain based on column names in the data in only one word"},
    {"role": "user", "content": str(df.columns)}
]
domian = send_llm_request(messages)


#Getting Information about the charts obtained
#-----------------------------------------------------
# Converting images to base64
#----------------------------------------------------- 
with open(f"./{folder}/box_plot.png", "rb") as image_file: 
    box_plot_enc = base64.b64encode(image_file.read()).decode("utf-8")
    
with open(f"./{folder}/corr_hmap.png", "rb") as image_file: 
    corr_hmap_enc = base64.b64encode(image_file.read()).decode("utf-8")
    
with open(f"./{folder}/histogram.png", "rb") as image_file: 
    histogram_enc = base64.b64encode(image_file.read()).decode("utf-8")
    
def build_msgs(text, img):
    """
    Generates the 'messages' parameter for the request body using the provided prompt and encoded image.

    Args:
        text (str): The input prompt.
        imge (str): The encoded image data.

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
    }
  ]
    
# Histogram Analysis by LLM
messages=build_msgs("This figure contains histograms from df.hist(). Provide a brief analysis in a story-telling way", histogram_enc)
histogram_ana_llm = send_llm_request(messages)

# Correlation Heatmap Analysis by LLM
messages=build_msgs("This figure contains correlation heatmap.Provide a brief analysis in a story-telling way", corr_hmap_enc)
corr_hmap_ana_llm = send_llm_request(messages)

# Box-Plot Analysis by LLM
messages=build_msgs("This figure contains box-plots.Provide a brief analysis in a story-telling way", box_plot_enc)
box_plot_ana_llm = send_llm_request(messages)

#-----------------------------------------------------
# Binding all this into README.md
#----------------------------------------------------- 
content = f"""
# Data Analysis Project 
Hey! Hope you are doing fine. Hmm... You've got some interesting data I  
see. Let's begin this journey with fist identifying what your data is like.  
So, you have got {df.shape[0]} rows and {df.shape[1]} columns in your data and  
as I can see this data this data is related to {domian}. Below are some key  
statistics about the data you provided

## Key Statistics
{summary_mdt}  
  
Let's move a little deeper and see what wonders the data is yet to reveal.
  
## Visualizing Data
Let's see how numerical columns correlate with each other  
  
![Figure](./corr_hmap.png)\n
  
{corr_hmap_ana_llm} 

Now in the second figure we'll see numerical columns spread themselves.  
  
![Figure](./histogram.png)\n
  
{histogram_ana_llm}

Lastly, we'll see some mischievous datapoints that don't follow the trend (Outliers!).  
  
![Figure](./box_plot.png)\n
  
{box_plot_ana_llm}

"""
with open(f'./{folder}/README.md', 'w') as file: 
    file.write(content)