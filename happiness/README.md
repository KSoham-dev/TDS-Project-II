
# Data Analysis Project 
Hey! Hope you are doing fine. Hmm... You've got some interesting data I see.  
Let's begin this journey with fist identifying what your data is like.  
So, you have got 100 rows and 500 columns in your data and as I can  
see this data is related to Well-being. Below are some key statistics  
about the data you provided  

## Key Statistics
|       |   year |   Life Ladder |   Log GDP per capita |   Social support |   Healthy life expectancy at birth |   Freedom to make life choices |   Generosity |   Perceptions of corruption |   Positive affect |   Negative affect |
|:------|-------:|--------------:|---------------------:|-----------------:|-----------------------------------:|-------------------------------:|-------------:|----------------------------:|------------------:|------------------:|
| count |   2363 |          2363 |                 2335 |             2350 |                               2300 |                           2327 |         2282 |                        2238 |              2339 |              2347 |
| mean  |   2014 |             5 |                    9 |                0 |                                 63 |                              0 |            0 |                           0 |                 0 |                 0 |
| std   |      5 |             1 |                    1 |                0 |                                  6 |                              0 |            0 |                           0 |                 0 |                 0 |
| min   |   2005 |             1 |                    5 |                0 |                                  6 |                              0 |            0 |                           0 |                 0 |                 0 |
| 25%   |   2011 |             4 |                    8 |                0 |                                 59 |                              0 |            0 |                           0 |                 0 |                 0 |
| 50%   |   2015 |             5 |                    9 |                0 |                                 65 |                              0 |            0 |                           0 |                 0 |                 0 |
| 75%   |   2019 |             6 |                   10 |                0 |                                 68 |                              0 |            0 |                           0 |                 0 |                 0 |
| max   |   2023 |             8 |                   11 |                0 |                                 74 |                              0 |            0 |                           0 |                 0 |                 0 |  
  
Let's move a little deeper and see what wonders the data is yet to reveal.
  
## Visualizing Data
Let's see how numerical columns correlate with each other  
  
![Figure](./corr_hmap.png)

  
Once upon a time in the land of data, a captivating correlation heatmap emerged, revealing the intricate relationships among various factors affecting quality of life.

At the center of this tale was the year, providing a timeline to measure progress. Its strong bond with the "Life Ladder" (0.78) suggested that as time passed, people felt increasingly optimistic about their lives, like climbing a well-worn path to a brighter future.

The "Log GDP per capita" (0.72) unveiled the economic tale, indicating that wealth was intricately linked to life satisfaction—the higher the wealth, the higher the happiness. However, whispers of caution arose as "Social support" (0.67) revealed that true happiness wasn't just about wealth; it's also about community ties and friendships that uplift spirits.

In another corner, the "Healthy life expectancy at birth" painted a hopeful picture of good health (0.70). As people lived healthier lives, their sense of well-being flourished. Yet, amid this growth, the "Freedom to make choices" (0.47) also demanded attention. It hinted that even in a prosperous land, the ability to choose one’s path was crucial for happiness.

As the story unfolded, "Generosity" (0.42) and "Perception of corruption" (-0.46) offered contrasting lessons. Generosity fostered connections and satisfaction, while corruption echoed shadows of doubt, dampening spirits and trust.

Finally, the contrasting emotions of "Positive affect" (0.31) and "Negative affect" (-0.20) played their roles in this narrative, illustrating how positivity could lift the human spirit, while negativity cast a pall, connecting deeply with the other variables.

And so, this heatmap told a tale of interconnectedness—a reminder that life’s quality is not just a solitary climb but a journey enriched by community, health, freedom, and integrity. In this world of data, every number was a thread woven into the larger tapestry of happiness. 

Now in the second figure we'll see numerical columns spread themselves.  
  
![Figure](./histogram.png)

  
The visual story told by these histograms is a fascinating exploration of the well-being and quality of life metrics as captured in a dataset over a span of years.

Starting with the **year** histogram, we see a clear picture of data collection, with peaks representing different years. This steady rise in recorded years illustrates the growing interest in understanding how various factors influence life satisfaction and societal progress.

Next, the **Life Ladder** histogram reveals a roughly normal distribution, suggesting that most individuals report a moderate level of life satisfaction. However, there are noticeable tails on either end, indicating that while many are content, there are also significant numbers experiencing extreme satisfaction and dissatisfaction.

Moving to the **Log GDP per capita**, the histogram leans towards the higher end, indicating a concentration of countries or regions with relatively high economic performance. This aligns with the expectation that wealthier nations tend to report better quality of life metrics.

The **Social support** histogram shows an interesting distribution with a slight left skew. Most people appear to report moderate to high levels of social support, which is essential for individual well-being and community strength.

The **Healthy life expectancy at birth** histogram suggests that many individuals enjoy a relatively long and healthy life, though some outliers indicate varying conditions across different populations.

In terms of **Freedom to make life choices**, the distribution is centered towards the higher end as well. People generally feel they have a reasonable amount of control over their lives, pointing to varying degrees of liberty and self-determination across different cultures.

The **Generosity** histogram, while also fairly centered, hints at a tendency towards lower generosity scores, suggesting that while some individuals are quite generous, many do not exhibit high levels of charitable behavior.

**Perceptions of corruption** present a slightly different narrative, with a considerable number of respondents leaning towards the belief that corruption exists in their societies, reflecting a widespread distrust in public institutions or systems.

When we look at **Positive affect**, we see a distribution suggesting that people generally experience positive emotions frequently, yet there are some low scores indicating moments of dissatisfaction or unhappiness.

Lastly, **Negative affect** shows a more pronounced peak, indicating that while many individuals experience low levels of negative emotions, a significant portion also grapples with higher levels of negativity, highlighting the ongoing struggles with mental health and emotional well-being in various communities.

Together, these histograms form a complex tapestry of human experience, showing how economic factors, societal support, and individual perceptions intertwine to shape quality of life. Through these insights, we can appreciate the nuances of happiness and well-being in today’s world, recognizing both strides made and challenges that remain.

Lastly, we'll see some mischievous datapoints that don't follow the trend (Outliers!).  
  
![Figure](./box_plot.png)

  
In the serene landscape of data representation, box plots emerge as the wise storytellers of numerical tales, guiding us through the intricate narratives of our chosen variables. 

Let's step into this visual world together, where each box plot invites us to explore different facets of life and well-being.

### The Journey through Time: Year
The first box plot reveals the **Year** variable, with its steady heartbeat between 2015 and 2021. This consistency hints at stability in data collection, allowing us to observe trends without the disruption of abrupt changes. 

### The Ladder of Life: Life Expectancy
Next, we encounter the **Life Ladder**, a metaphor for the journey of life itself. The plot indicates a significant range, with most individuals resting comfortably in the middle, reflecting a general sense of well-being. However, the presence of a few outliers suggests that not everyone has climbed the rungs equally, emphasizing the disparities that exist within society.

### Economic Pulse: Log GDP per Capita
We then ascend to the **Log of GDP per Capita**, which illustrates the economic vitality of each region. The plot indicates a healthy spread, suggesting varying levels of prosperity. While many enjoy economic affluence, the whispered presence of outliers reminds us that not all regions experience this growth equally.

### The Support Structure: Social Support
Moving on, the **Social Support** plot illustrates a comforting sense of community, where most individuals feel a solid backing. The narrow range signifies that the majority share a similar experience, fostering a sense of collective strength and resilience in facing life’s challenges.

### The Gift of Longevity: Healthy Life Expectancy at Birth
In the next scene, we explore **Healthy Life Expectancy at Birth**. Here, the data showcases a promising outlook on health, yet the outliers reveal the harsh realities faced by a minority. The broader shape of the box signifies a generally positive health trajectory, suggesting that many are likely to enjoy longer, healthier lives.

### Choices that Matter: Freedom to Make Life Choices
Finally, we arrive at the **Freedom to Make Life Choices** plot, where the data present a blend of liberation and constraint. While the majority feel empowered to steer their own destinies, the presence of those on the edges of the box reminds us that not everyone has this luxury. The variations highlighted here serve as a call to action for fostering greater equity in personal freedoms.

### Conclusion
As we step back from this visual tale, we realize that these box plots not only present data but weave a narrative of society’s strengths and struggles. Each variable contributes to a larger picture of well-being, economic health, and personal freedom, urging us to consider how we can nurture these areas for a brighter, more equitable future.

