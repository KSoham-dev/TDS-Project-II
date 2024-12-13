
# Data Analysis Project 
Hey! Hope you are doing fine. Hmm... You've got some interesting data I see.  
Let's begin this journey with first identifying what your data is like.  
So, you have got 2363 rows and 11 columns in your data and as I can  
see this data is related to Well-being. Below are some key statistics  
about the data you provided  

## Key Statistics
|       |   year |   Life Ladder |   Log GDP per capita |   Social support |   Healthy life expectancy at birth |   Freedom to make life choices |   Generosity |   Perceptions of corruption |   Positive affect |   Negative affect |
|:------|-------:|--------------:|---------------------:|-----------------:|-----------------------------------:|-------------------------------:|-------------:|----------------------------:|------------------:|------------------:|
| count |   2363 |          2363 |                 2363 |             2363 |                               2363 |                           2363 |         2363 |                        2363 |              2363 |              2363 |
| mean  |   2014 |             5 |                    9 |                0 |                                 63 |                              0 |            0 |                           0 |                 0 |                 0 |
| std   |      5 |             1 |                    1 |                0 |                                  6 |                              0 |            0 |                           0 |                 0 |                 0 |
| min   |   2005 |             1 |                    5 |                0 |                                  6 |                              0 |            0 |                           0 |                 0 |                 0 |
| 25%   |   2011 |             4 |                    8 |                0 |                                 59 |                              0 |            0 |                           0 |                 0 |                 0 |
| 50%   |   2015 |             5 |                    9 |                0 |                                 64 |                              0 |            0 |                           0 |                 0 |                 0 |
| 75%   |   2019 |             6 |                   10 |                0 |                                 68 |                              0 |            0 |                           0 |                 0 |                 0 |
| max   |   2023 |             8 |                   11 |                0 |                                 74 |                              0 |            0 |                           0 |                 0 |                 0 |  
  
Let's move a little deeper and see what wonders the data is yet to reveal.
  
## Visualizing Data
Let's see how numerical columns correlate with each other  
  
![Figure](./corr_hmap.png)

  
Once upon a time in a land rich with data, a group of researchers sought to understand the intricate relationships between the various facets of human well-being and prosperity. They gathered a treasure trove of numerical features and created a colorful correlation heatmap to find hidden stories within the numbers.

As they gazed upon the heatmap, the first thing that caught their eye was the strong bond between **Log GDP per capita** and **Life Ladder**, represented by a robust correlation of 0.77. This indicated that as the economic wealth of a country increased, so too did the perceived quality of life among its citizens. It suggested that prosperity nurtured happiness.

Next, they noticed the interconnections between personal freedoms and well-being. The **Freedom to make life choices** had a positive correlation with **Life Ladder** (0.60) and a hint of connection with **Generosity** (0.34). This hinted that when individuals felt empowered in their choices, they were not only likely to thrive but also engage in acts of kindness towards others, enriching their communities.

However, the journey wasn’t without its shadows. The researchers observed that **Negative affect**, a measure of emotional distress, enjoyed a strong negative correlation with **Life Ladder** (-0.73). This made it clear that the more individuals experienced negative emotions, the less joy they found in their lives. It underscored the importance of mental health for overall happiness.

In the corner of the heatmap, the researchers noted the curious dance of **Generosity** and **Perceptions of Corruption**. The correlation between these two was surprising; a negative relationship (-0.54) suggested that as perceptions of corruption increased, the spirit of generosity waned. People tended to lose faith in sharing and caring when trust in their institutions faltered.

As they concluded their analysis, the researchers felt a sense of fulfillment. This vibrant heatmap had illuminated the complex tapestry of life experiences. It told a tale where wealth and freedom intertwined to create happiness, but where emotional well-being and trust in society remained crucial for flourishing. With their findings, they hoped to inspire policies that could nurture a world where happiness blossomed for all. And so, armed with data-driven insights, they set forth to make a difference, one correlation at a time. 

Now in the second figure we'll see numerical columns spread themselves.  
  
![Figure](./histogram.png)

  
In the bustling world of data, we find ourselves amidst a vibrant tapestry woven from various aspects of human experience. As we delve into the histograms laid before us, each subplot tells a unique story, encapsulating the essence of societal factors and individual well-being.

### Year: The Passage of Time
The journey begins with the histogram of the **year**, where we see a steady increase in data points from 2005 onward. This upward trajectory reflects ongoing progress and the accumulation of experiences across time, hinting at the evolving narrative of societal conditions.

### Life Ladder: Climbing High
Next, we encounter the **Life Ladder** histogram, a symbol of aspiration. The distribution is notably skewed to the right, indicating that a significant portion of individuals reports higher life satisfaction. However, the tail on the left suggests that while many thrive, a considerable number struggle, reminding us of the disparities that persist in our world.

### Log GDP per Capita: The Wealth Equation
In the **Log GDP per Capita** plot, we observe a bell-shaped curve, pointing to a concentration of data around the middle. This highlights economic strengths as well as inequalities, where wealth is abundant, yet not universally enjoyed. The distribution speaks to the story of prosperity, but also to the barriers faced by those on the lower end of the economic spectrum.

### Social Support: A Helping Hand
The histogram of **Social Support** portrays a hopeful scene. Most individuals rate their sense of community positively, suggesting that relational bonds are a source of strength. Yet, the slight leftward skew prompts us to reflect on those who feel isolated—a quiet call to action for enhancing community connections.

### Healthy Life Expectancy at Birth: A Healthier Tomorrow
Turning to **Healthy Life Expectancy at Birth**, we see another right-skewed distribution that paints a picture of longevity and wellness. Many experience a fulfilling life, yet a noticeable number are deprived of this basic joy, urging us to work towards health equity for all.

### Freedom to Make Life Choices: Empowerment
The **Freedom to Make Life Choices** histogram reveals a profoundly empowering narrative. Most people feel they have control over their lives, suggesting an environment that encourages autonomy, critical for personal growth and societal progress. However, the occasional dips remind us that freedom is not uniformly experienced.

### Generosity: The Giving Spirit
With **Generosity**, the histogram echoes a heartwarming trend—a significant number of people engage in altruistic behaviors. The sharp drop-off on the left side illustrates that while many contribute, a few do not engage in giving, highlighting potential areas for fostering empathy and kindness.

### Perceptions of Corruption: Trust in Society
The depiction of **Perceptions of Corruption** unnervingly clusters toward lower perceptions, suggesting a widespread distrust in institutions. This histogram acts as a mirror for societies grappling with transparency issues, urging a collective need for accountability.

### Positive Affect: The Joyful Moments
In the subplot of **Positive Affect**, we observe a healthy distribution showcasing a majority indulging in positive emotions. This histogram tells a tale of joy and contentment, yet the slight dip hints at the challenges some face in finding happiness amidst life's pressures.

### Negative Affect: The Balancing Act
Finally, the **Negative Affect** histogram, with its pronounced left skew, illustrates that while many experience minimal negativity, there exists a portion still battling tough emotions. It serves as a reminder of the psychological struggles that often go unnoticed.

### Conclusion
These histograms collectively frame a narrative of human experience—where progress is celebrated, yet challenges persist. They beckon us to delve deeper, fostering understanding and inspiring action towards a more equitable and joyful society. Each plot is a chapter in a broader story, urging us to listen, learn, and strive for improvement.

Lastly, we'll see some mischievous datapoints that don't follow the trend (Outliers!).  
  
![Figure](./box_plot.png)

  
Once upon a time in the land of data, our curious analyst stumbled upon a treasure trove of box plots, each telling a unique story about key variables of happiness and well-being.

In the first plot, **Year**, the data resembled a steady progression over time. With values clustering in the middle, our analyst noted how stability often leads to contentment, but a few outliers hinted at years of significant change.

Next, the **Life Ladder** plot stood tall and proud. Most values nestled comfortably in the box, suggesting that people felt relatively happy. Yet, the whiskers extended, indicating there's always room for improvement for some souls, while a few points drifted away, reminding us that happiness can be fleeting.

When it came to **Log gdp per capita**, the analyst noticed a healthy range, with a tight central box indicating that wealth does influence happiness. However, lurking at the edges were outliers, suggesting that even in affluence, some individuals might feel left behind.

The **Social Support** box plot revealed a high level of connectedness among the majority, with values clumped together, but a few lonely points indicated that not everyone has access to this crucial lifeline. This whispered tales of loneliness in a bustling world.

The next plot displayed **Healthy Life Expectancy at Birth**. Here, most values soared, promising a long and hearty existence for many. However, the presence of outliers captured the analyst's attention, illustrating disparities in health that often dictate one's quality of life.

Last but not least was the **Freedom to Make Life Choices**, which told a compelling tale of empowerment. With a robust central box, it painted a picture of a society where people generally felt free to choose their paths. Yet, again, those outliers served as powerful reminders that for some, choices still feel limited.

Together, these plots wove a narrative of contrasts—between happiness and sorrow, health and struggle, freedom and confinement. The analyst closed the book on this chapter, realizing that behind every number lies a unique story waiting to be told.

