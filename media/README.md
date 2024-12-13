
# Data Analysis Project 
Hey! Hope you are doing fine. Hmm... You've got some interesting data I see.  
Let's begin this journey with first identifying what your data is like.  
So, you have got 2652 rows and 8 columns in your data and as I can  
see this data is related to Reviews. Below are some key statistics  
about the data you provided  

## Key Statistics
|       |   overall |   quality |   repeatability |
|:------|----------:|----------:|----------------:|
| count |      2652 |      2652 |            2652 |
| mean  |         3 |         3 |               1 |
| std   |         0 |         0 |               0 |
| min   |         1 |         1 |               1 |
| 25%   |         3 |         3 |               1 |
| 50%   |         3 |         3 |               1 |
| 75%   |         3 |         4 |               2 |
| max   |         5 |         5 |               3 |  
  
Let's move a little deeper and see what wonders the data is yet to reveal.
  
## Visualizing Data
Let's see how numerical columns correlate with each other  
  
![Figure](./corr_hmap.png)

  
In the vibrant world of data analysis, a correlation heatmap emerges as a storyteller, revealing the intricate relationships between numerical features. Picture a canvas painted in shades of red and blue, where each color conveys the strength of connections.

At the center of this tableau is the "overall" feature, standing tall with a perfect correlation of 1.00 with itself—an expected certainty. Yet, it shares an impressive bond with "quality," boasting a correlation of 0.83. This strong association suggests that as the overall performance improves, quality likely follows suit, hinting at a symbiotic relationship where excellence in one aspect elevates the other.

Meanwhile, "overall" also dances with "repeatability," displaying a moderate correlation of 0.51. This indicates that while there is a connection, it may not be as robust as with "quality." It suggests that consistent performance may be influenced by other factors that do not fully align with overall excellence.

Next, "quality" and "repeatability" share a weaker yet noteworthy connection of 0.31. This relationship reveals that while there is some interplay between how often results can be reproduced and the quality perceived, it's not particularly strong. There could be other underlying factors affecting repeatability that are distinct from quality metrics.

As we take a step back, this heatmap serves as a guide, illuminating the pathways between various features. By understanding these correlations, we can better predict outcomes, enhance performance, and uncover deeper insights in the data landscape. Each connection tells part of a larger narrative, inviting analysts to explore, question, and ultimately transform the raw data into actionable insights. 

Now in the second figure we'll see numerical columns spread themselves.  
  
![Figure](./histogram.png)

  
Once upon a time in the land of data, three key characters emerged from a mystical dataset: Overall, Quality, and Repeatability. Each character had their own unique story to tell through the colorful histograms that depicted their existence.

In the first story, **Overall** stood tall in the histogram, revealing a concentration of values hovering around the lower end of the spectrum, predominantly at 1 and 2. The scene was quite sparse on higher values, suggesting that most observations fell short of excellence. This hinted that perhaps the measures of success in this realm were an uphill battle.

Next came **Quality**, who mirrored Overall in spirit but painted a clearer picture. Here, the histogram showed a distinct spike at around 2, suggesting that this was a common state for many subjects in the dataset. The significant drop-off in higher values indicated that while some strived for excellence, many others settled for mediocrity, reinforcing the challenges faced in achieving superior quality.

Finally, the quiet figure of **Repeatability** emerged, a rather peculiar character with almost all values tightly clustered at around 1.75. This intriguing distribution not only showed a notable lack of variation but also hinted at a reliability that could be both a boon and a bane—consistently repetitive but perhaps lacking the flexibility necessary for adaptation.

As the stories unfolded, they painted a vivid narrative of a dataset rife with challenges and opportunities. The quest for excellence in Overall and Quality remained elusive, while Repeatability's steady hand provided a foundation for future adventures in improvement. In this land, the characters would need to forge paths toward transformation, seeking insights that could guide them to a brighter, higher-stakes future.

Lastly, we'll see some mischievous datapoints that don't follow the trend (Outliers!).  
  
![Figure](./box_plot.png)

  
Once upon a time in the realm of data analysis, three distinct characters emerged, each represented by a box plot: Overall, Quality, and Repeatability. 

First, the Overall character stood tall and proud, with a broad range of values stretching from 1 to 5. The middle line of the box, at around 3.5, hinted at a stable heart, suggesting that while there were occasional outliers — the little circles at both ends — the majority thrived comfortably in the 2 to 4 range.

Next, Quality stepped forward. Its box was shorter and more robust, encapsulating values predominantly between 3 and 4. The median sat slightly above 3.5, indicating that most of the data aligned closely around that mark. However, a notable absence of lower values hinted that Quality had a consistently high standard, with no room for mediocrity.

Finally, the shy character of Repeatability emerged. Unlike the others, Repeatability's box was much shorter, confined between 1.25 and 2.5. Its median was relatively low at 1.75, suggesting that while it had some highs, it often struggled to reach the standards set by Overall and Quality. 

The story woven through these box plots tells of a world where Overall shows a promising landscape, Quality maintains a commendable standard, but Repeatability seems to grapple with consistency. As they each navigate their journeys, the insights gleaned from these plots pave the way for future endeavors, encouraging a focus on enhancing Repeatability while building on the strengths of its companions.

