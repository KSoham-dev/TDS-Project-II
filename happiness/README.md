
# Data Analysis Project 
Hey! Hope you are doing fine. Hmm... You've got some interesting data I see.  
Let's begin this journey with first identifying what your data is like.  
So, you have got 2363 rows and 11 columns in your data and as I can  
see this data is related to Wellbeing. Below are some key statistics  
about the data you provided  

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
Let's see how numerical columns correlate with each other  
  
![Figure](./corr_hmap.png)

  
Imagine stepping into a vibrant tapestry of connections, where every thread tells a story about how our lives intertwine. In this colorful correlation heatmap, a tale unfolds through the relationships between various numerical features that reflect the well-being of individuals and nations.

At the heart of this narrative, we discover the strongest bond—between **Life Ladder** and **Log GDP per capita**. This relationship reveals that as the economy flourishes, so too does the perceived quality of life. Picture a thriving market bustling with opportunities, lifting spirits and aspirations alike.

Next, the linkage between **Healthy life expectancy at birth** and the **Life Ladder** suggests that longer, healthier lives contribute to a greater sense of fulfillment. Imagine communities where people live not just longer but richer lives, filled with purpose and well-being.

In another corner of this story, we see **Freedom to make life choices** positively correlating with both **Life Ladder** and **Generosity**. This illustrates how the ability to choose one’s path can enhance happiness and foster a culture of giving, weaving a fabric of support and kindness within societies.

Yet, not all threads vibrate in harmony. The **Negative affect**, with its slight negative correlations to features like **Positivity of affect and Generosity**, hints at the shadows that occasionally darken our emotional landscape. It reminds us that feelings of sorrow or negativity can pull against the lighter threads of happiness and altruism.

Finally, the overall tale conveyed by this heatmap is one of interconnectedness—each feature a thread in a larger tapestry of life. The warmth of community, the strength of personal freedom, and the cycles of prosperity contribute to a rich narrative of human experience, urging us to reflect on how our choices impact not just our own lives, but the collective well-being of all. 

Now in the second figure we'll see numerical columns spread themselves.  
  
![Figure](./histogram.png)

  
In the vibrant tapestry of life depicted through these histograms, each subplot reveals a unique aspect of human experience over the years, with a focus on well-being and societal traits.

Starting with **year**, we see the timeline stretching from 2005 to 2019, showcasing a steady evolution—perhaps a reflection of growing awareness and shifts in lifestyle that accompany societal changes.

**Life Ladder** is a whimsical curve, hinting at the aspirations and happiness towards the middle of the spectrum. Its peaks suggest many individuals find themselves if not atop, then certainly nearer to the top rungs of contentment.

As we traverse to **Log GDP per capita**, the data paints a more diverse picture. This distribution suggests a significant number of individuals live in economies benefitting from wealth, yet a noticeable tail indicates some who are far below the average prosperity.

**Social support** shines through as a crucial feature with a pronounced peak around the middle values. This implies that many people perceive a strong network around them, emphasizing the importance of community and emotional backing in nurturing happy lives.

Next, **Healthy life expectancy at birth** brings a hopeful stride to the narrative, reflecting on the years of good health many can expect. The spread hints at disparities, but overall, it signals substantial progress in public health.

In a world where autonomy matters, **Freedom to make life choices** reveals a moderately distributed sentiment. Most seem to experience a decent level of freedom, yet there are still pockets of individuals feeling constricted, urging a call for greater personal liberty.

The **Generosity** histogram gives rise to a notion of altruism, with a slight tilt towards higher values. This suggests that while many are inclined to give, there is still room for more magnanimous actions within communities.

**Perceptions of corruption** tell a compelling tale, with a notable majority expressing lesser corruption perceptions. It opens a window to the optimism with which people view the integrity of their institutions, paving the way for trust in societal structures.

In the emotional landscape, **Positive affect** and **Negative affect** balance each other, presenting a coexistence of joy and sorrow. While positive emotions hover around the mid-range, the negative emotions tend to linger in lower frequencies, revealing a narrative where people generally experience more positivity than negativity in their lives.

Together, these histograms weave a narrative of human well-being, revealing a society striving for happiness, health, and trust, whilst recognizing the challenges and disparities that still lurk beneath the surface.

Lastly, we'll see some mischievous datapoints that don't follow the trend (Outliers!).  
  
![Figure](./box_plot.png)

  
In a vibrant land of data, a powerful tale unfolds through the box plots, each revealing secrets of various variables that shape lives and destinies.

**Year and Life Ladder:**
In the first box plot, dedicated to the year, we see a consistent narrative with values hovering around the 2010 mark, hinting at a steady progression. Meanwhile, the life ladder box plot shows a more vibrant spectrum of experiences, with a mean that rises notably, painting a picture of growing aspirations and well-being.

**Economic Insights:**
The next plot, showcasing the logarithm of GDP per capita, stands tall and proud. It reflects not just wealth but the vibrancy of economies, with minimal outliers indicating stability. Here, prosperity seems to touch many, suggesting a robust economic foundation.

**Social Support:**
Turning to the box plot of social support, we find an interesting contrast. While the median suggests an underlying strength, the presence of outliers hints at individuals with exceptional or challenging circumstances, underscoring the importance of community and belonging in navigating life’s ups and downs.

**Healthy Life Expectancy:**
The plot on healthy life expectancy at birth reveals a similar tale, with the whiskers suggesting that while most enjoy long, healthy lives, a significant minority grapples with health challenges. This duality illustrates the critical importance of health systems in safeguarding futures.

**Freedom and Choice:**
Finally, the box plot representing freedom to make life choices presents a compelling narrative. With a mean skewed towards the higher end, it reflects the increasing liberties many enjoy. Yet, the few outliers call attention to those whose choices are severely restricted, reminding us that the path to freedom is not universally paved.

In this intricate weave of plots, we discover the complexities and interconnections of life variables—each telling its own story, yet they converge to illuminate the shared human experience, celebrating both triumphs and challenges in the journey through life.

