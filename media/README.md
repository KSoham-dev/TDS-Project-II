
# Data Analysis Project 
Hey! Hope you are doing fine. Hmm... You've got some interesting data I see.  
Let's begin this journey with first identifying what your data is like.  
So, you have got 2652 rows and 8 columns in your data and as I can  
see this data is related to Reviews. Below are some key statistics  
about the data you provided  

## Missing Value Analysis
The dataset contains the following missing values:

| Column        |   Missing Values |   Percentage |
|:--------------|-----------------:|-------------:|
| date          |               99 |         3.73 |
| language      |                0 |         0    |
| type          |                0 |         0    |
| title         |                0 |         0    |
| by            |              262 |         9.88 |
| overall       |                0 |         0    |
| quality       |                0 |         0    |
| repeatability |                0 |         0    |

## Advanced Statistical Analysis
|               |   mean |   std |   min |   25% |   50% |   75% |   max |   Skewness |   Kurtosis |
|:--------------|-------:|------:|------:|------:|------:|------:|------:|-----------:|-----------:|
| overall       |   3.05 |  0.76 |     1 |     3 |     3 |     3 |     5 |       0.16 |       0.15 |
| quality       |   3.21 |  0.8  |     1 |     3 |     3 |     4 |     5 |       0.02 |      -0.17 |
| repeatability |   1.49 |  0.6  |     1 |     1 |     1 |     2 |     3 |       0.78 |      -0.38 |  
  
Let's move a little deeper and see what wonders the data is yet to reveal.
  
## Visualizing Data
Let's see how numerical columns correlate with each other  
  
![Figure](./corr_hmap.png)

  
Once upon a time in the realm of data analysis, a researcher delved into the intricate relationships between their variables, seeking hidden patterns that could unlock new insights. They created a correlation heatmap, a colorful tapestry displaying how numerical features interacted with one another.

In this vibrant landscape, the key players emerged: **overall**, **quality**, and **repeatability**. The strong bond between **overall** and **quality** shimmered with a correlation coefficient of 0.83, suggesting that as the overall score improved, quality followed suit like a loyal companion. This hinted at a potential synergy between these two attributes, where enhancing one could lead to elevated standards in the other.

The relationship between **overall** and **repeatability** also caught the eye, showing a moderate correlation of 0.51. This connection hinted at an interesting narrative: while some consistency in results was present, it was not as robust as the relationship with quality. It suggested that improvements in overall performance might lead to better repeatability, but the journey would require more nuanced understanding and exploration.

Finally, the link between **quality** and **repeatability** was rather timid, resting at 0.31. This articulation whispered that while quality might play a role in encouraging repeatable outcomes, there were likely external factors at play that could not be ignored.

As the researcher gazed at this heatmap, they felt empowered. Each vibrant hue represented a story waiting to be told—one of collaboration between strengths and weaknesses. With newfound clarity, they set forth to explore these relationships further, eager to transform data into meaningful actions for the future. And so, the journey of data-driven discovery continued. 

Now in the second figure we'll see numerical columns spread themselves.  
  
![Figure](./histogram.png)

  
In the land of data, we stumbled upon a trio of histograms, each telling a unique story about numerical features in our dataset. 

**Overall** features seem to be clustered tightly around the middle of the scale, with spikes at specific intervals, indicating a common consensus in the data. Most observations hover around the range of 1.5 to 3.5, suggesting a potential prevailing norm within whatever metric we’re measuring—perhaps a measure of satisfaction or performance.

Next, we explore the **quality** feature, where the story unfolds with a similar pattern. It mirrors the overall distribution but leans towards slightly better evaluations. Here, we see most values tightly packed between 1.5 and 4.5, suggesting that while there’s an awareness of quality, there may be room for improvement. The central tendency reigns, pointing to a population that is generally satisfied but occasionally experiences dips.

Finally, we confront the **repeatability** feature, which stands out from its companions. This histogram presents a peculiar shape, with a spike concentrated at the lower end of the scale, between 1.5 and 1.75. It suggests that many observations exhibit a lack of consistency—implying that while the data might yield decent overall quality, it struggles to replicate that success consistently. 

Through these visual narratives, we see a dataset rich with insights. While overall satisfaction appears favorable, the quality and repeatability tell us there’s a path forward for improvement—inviting a deeper dive into the factors influencing these trends. Each histogram whispers secrets about user experience, urging us to listen closely and act wisely.

Lastly, we'll see some mischievous datapoints that don't follow the trend (Outliers!).  
  
![Figure](./box_plot.png)

  
Once upon a time, in the realm of data analysis, three distinct characters emerged from the shadows of statistics: Overall, Quality, and Repeatability. Each character brought with them stories of variation and insight.

**Overall** was the most balanced of the trio, standing tall with a median value around 4. This character had a few outliers on both ends, indicating there were instances of particularly high and low values, but the bulk of the data settled comfortably around the 3.5 mark, showcasing a generally favorable scenario.

**Quality**, on the other hand, was a bit of a mixed bag. With its range stretching from just below 3 to a peak at around 4.5, Quality displayed a slight skew towards the higher values. Yet, there were some whispers of inconsistency, as indicated by its wider interquartile span. She was the one who had most of her values focused around the center, but with a few notable exceptions that hinted at underlying challenges.

Then there was **Repeatability**, the smallest of the trio, who revealed a more confined story. With a median around 1.5 and a stark upper limit of barely reaching 2.5, Repeatability struggled to match the composure of the others. It was clear that this character faced considerable challenges, with most values clustering tightly at the lower end, suggesting a need for improvements.

As the characters compared their experiences, it became apparent that while Overall and Quality had many strengths, Repeatability might be the one in need of attention. This analysis sparked conversations about potential improvements and strategic decisions, shaping the future narrative of their intertwined destinies. Together, they would forge a path toward clearer insights and stronger outcomes. And thus, the story of their data journey continued.

