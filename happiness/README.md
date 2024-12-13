
# Data Analysis Project 
Hey! Hope you are doing fine. Hmm... You've got some interesting data I see.  
Let's begin this journey by first identifying what your data is like.  
So, you have got 2363 rows and 11 columns in your data, and as I can  
see, this data is related to Well-being. Below are some key statistics  
about the data you provided:

## Missing Value Analysis
The dataset contains the following missing values:

| Column                           |   Missing Values |   Percentage |
|:---------------------------------|-----------------:|-------------:|
| Country name                     |                0 |            0 |
| year                             |                0 |            0 |
| Life Ladder                      |                0 |            0 |
| Log GDP per capita               |                0 |            0 |
| Social support                   |                0 |            0 |
| Healthy life expectancy at birth |                0 |            0 |
| Freedom to make life choices     |                0 |            0 |
| Generosity                       |                0 |            0 |
| Perceptions of corruption        |                0 |            0 |
| Positive affect                  |                0 |            0 |
| Negative affect                  |                0 |            0 |

## Advanced Statistical Analysis
|                                  |    mean |   std |     min |     25% |     50% |     75% |     max |   Skewness |   Kurtosis |
|:---------------------------------|--------:|------:|--------:|--------:|--------:|--------:|--------:|-----------:|-----------:|
| year                             | 2014.76 |  5.06 | 2005    | 2011    | 2015    | 2019    | 2023    |      -0.06 |      -1.09 |
| Life Ladder                      |    5.48 |  1.13 |    1.28 |    4.65 |    5.45 |    6.32 |    8.02 |      -0.05 |      -0.56 |
| Log GDP per capita               |    9.4  |  1.15 |    5.53 |    8.52 |    9.49 |   10.38 |   11.68 |      -0.34 |      -0.75 |
| Social support                   |    0.81 |  0.12 |    0.23 |    0.74 |    0.83 |    0.9  |    0.99 |      -1.11 |       1.15 |
| Healthy life expectancy at birth |   63.4  |  6.75 |    6.72 |   59.54 |   64.9  |   68.4  |   74.6  |      -1.15 |       3.09 |
| Freedom to make life choices     |    0.75 |  0.14 |    0.23 |    0.66 |    0.77 |    0.86 |    0.98 |      -0.71 |       0.1  |
| Generosity                       |    0    |  0.16 |   -0.34 |   -0.11 |   -0.02 |    0.09 |    0.7  |       0.78 |       0.97 |
| Perceptions of corruption        |    0.74 |  0.18 |    0.04 |    0.7  |    0.79 |    0.86 |    0.98 |      -1.53 |       2.08 |
| Positive affect                  |    0.65 |  0.11 |    0.18 |    0.57 |    0.66 |    0.74 |    0.88 |      -0.46 |      -0.12 |
| Negative affect                  |    0.27 |  0.09 |    0.08 |    0.21 |    0.26 |    0.33 |    0.7  |       0.7  |       0.66 |  
  
Let's move a little deeper and see what wonders the data is yet to reveal.
  
## Visualizing Data
### Correlation Heatmap
Understanding how numerical columns correlate with each other can provide insights into potential relationships and dependencies between variables. Here's a heatmap showing these correlations:

![Correlation Heatmap](./corr_hmap.png)

  
Once upon a time in the realm of data, we stumbled upon a vibrant correlation heatmap that revealed the relationships between various numerical features related to well-being and societal factors.

At the center of this story was the **"year,"** a constant presence, with perfect harmony to itself and a significant connection to **"Log GDP per capita"** (0.72). This tells us that as time progressed, nations with higher economic output per person thrived. However, the shadows loom when we look at **"Healthy life expectancy at birth"** (0.04), suggesting that economic growth didn’t always equate to longer, healthier lives.

The tale took a bright turn when we encountered **"Life Ladder,"** a metaphor for happiness, which correlated strongly with both **"Healthy life expectancy at birth"** (0.77) and **"Generosity"** (0.54). This implies that people who reported greater satisfaction with their lives tended to live healthier and were more inclined to give back to their communities.

Delving deeper, we saw that **"Freedom to make life choices"** (0.61) had a significant relationship with overall happiness as well. This connection reminded us that true happiness often comes from the ability to choose one’s own path.

However, the riddles of life surfaced with the appearance of **"Negative affect,"** which displayed a troubling correlation with **"Positive affect"** (-0.74). This stark contrast illustrated the delicate balance of emotions; where joy thrived, negativity tended to recede. 

In conclusion, our heatmap journey revealed that well-being is an intricate tapestry woven with threads of health, happiness, freedom, and generosity. This interplay invites us to ponder how societal advancements can enhance the quality of life, urging us to nurture both the mind and body for a flourishing future. 

### Histograms
Histograms help us understand the distribution of numerical columns. They can reveal patterns such as skewness, modality, and the presence of outliers. Here's a look at the histograms for the numerical columns:

![Histograms](./histogram.png)

  
In the vibrant tapestry of societal well-being, the histograms present a compelling narrative, illustrating the nuances of various numerical features over time.

Starting with the **Life Ladder**, we observe a gentle upward slope from 2005 to 2015, hinting at a gradual improvement in perceived life satisfaction. This suggests that people are increasingly feeling more content and hopeful about their lives, although fluctuations suggest that not every year was equally favorable.

Turning to **Log GDP per capita**, the distribution reveals a more pronounced peak, indicating that while most individuals might experience moderate levels of economic prosperity, a significant portion still grapples with lower economic circumstances. This tells a story of inequality, where wealth is not distributed evenly across the population.

The **Social Support** histogram reflects a crucial element of community and belonging. The central clustering around higher values indicates that a majority of individuals feel they have strong support systems, essential for emotional and psychological health. However, the tail on the left hints at those who may feel isolated or unsupported.

**Healthy Life Expectancy at birth** exhibits a promising trend, suggesting that many individuals enjoy longer, healthier lives. The rightward skewed distribution suggests that the most healthy populations are thriving, yet there remains a consistent number facing health challenges.

When examining **Freedom to make life choices**, the histogram shows a broad, near-normal distribution, with a noted preference towards the higher end. This indicates that many individuals feel empowered to shape their own destinies, though the dips at the lower end remind us that not everyone enjoys this freedom.

Moving to **Generosity**, we see a right-skewed distribution, hinting that while many practice generosity, quite a few contribute minimally. This suggests a society where many are inclined to assist others, yet barriers still exist for some in extending their resources or time.

As we delve into perceptions of **Corruption**, the right-skew suggests a belief that many perceive their environments as corrupt, yet there is optimistic clustering towards the lower end, indicating hope for integrity in certain regions or communities.

In the realms of **Positive Affect**, the histogram reveals a heartening concentration around higher values. Many individuals report feeling positive emotions, fostering an optimistic societal outlook. In stark contrast, the **Negative Affect** histogram shows a more prominent left skew, where many individuals experience few negative feelings. However, the longer tail suggests that a significant minority struggles with persistent negative emotions, indicating areas of mental health that need attention.

Together, these histograms weave a complex narrative of societal dynamics, balancing hope against challenges, and highlighting both the support present in our communities and the struggles faced by some individuals. The data illustrates a society that, while prospering in many areas, must remain vigilant in addressing disparities and promoting well-being for all.

### Box Plots
Box plots are useful for identifying outliers and understanding the spread and central tendency of the data. Here's a look at the box plots for the numerical columns:

![Box Plots](./box_plot.png)

  
In a bustling town, where data flowed like a river, six box plots gathered to tell their unique stories. 

First, the **Year** plot stood tall, revealing a steady increase over time. The whiskers stretched far, hinting at some years of remarkable highs, while the central box signaled consistency, mostly lingering around the 2010 mark. It whispered tales of progress and growth, bridging generations.

Next came the **Life ladder**, a faithful companion to the townsfolk's happiness. Its box was broad and centered, suggesting that, generally, people felt content. Yet, a few outliers indicated moments of unexpected joy or perhaps hardship—reminders that life can be unpredictable.

The **Log gdp per capita** plot revealed the economic health of the village. With most values clustering tightly, it suggested a solid, if not soaring, average income. The longer whisker on the top hinted at wealthy outliers, perhaps a few fortunate individuals, while the bottom whisker signaled a few struggling households that barely managed to make ends meet.

On the topic of **Social support**, this plot radiated warmth. The box was comfortably high, indicating that, on average, residents felt there was always someone to lean on. However, those few outliers cried out for attention, representing a portion of the community that felt isolated, a timely reminder of the importance of connection.

Next, the **Healthy life expectancy at birth** plot stood proud, with most values hovering around the 70-year mark. This indicated a generally healthy population, though the occasional outlier revealed that some individuals faced harsher realities that pulled the average down, telling a tale of disparities in healthcare.

Finally, the **Freedom to make life choices** plot gleamed brightly, with the central box sitting high. It illustrated a community where freedom was valued, though the slight asymmetry of the whiskers hinted that not all voices felt equally empowered. 

Together, these plots painted a tapestry of a community: one growing and maturing, filled with both support and challenges, and thriving amidst the joys and sorrows of life. Each plot carried its narrative, inviting the townspeople to reflect, engage, and strive towards a brighter future.

## Chi-Square Test Reports
Chi-square tests help us understand the relationships between categorical variables. Here are the results of the chi-square tests for pairs of categorical columns:



