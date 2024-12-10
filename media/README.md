
# Data Analysis Project 
Hey! Hope you are doing fine. Hmm... You've got some interesting data I  
see. Let's begin this journey with fist identifying what your data is like.  
So, you have got 2652 rows and 8 columns in your data and  
as I can see this data this data is related to Reviews. Below are some key  
statistics about the data you provided

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

  
Once upon a time in the land of data, a vibrant correlation heatmap appeared, showcasing the relationships among three important variables: overall satisfaction, quality, and repeatability. 

As we peered into the depths of the map, we noticed that “overall” and “quality” were the brightest stars, shining with a strong correlation of 0.83. This indicates that higher quality often leads to greater overall satisfaction, hinting that crafting exceptional quality can enchant customers and keep them delighted.

Meanwhile, “overall” and “repeatability” only shared a moderate bond with a correlation of 0.51. This suggests that while repeatability plays a role in overall satisfaction, it’s not as profound as quality. It whispers that customers appreciate consistency, yet it’s the quality that truly speaks to their hearts.

Lastly, “quality” and “repeatability” shared a modest connection of 0.31, indicating that while repeatability does contribute to perceived quality, it wasn't the primary factor enhancing a customer's experience.

In summary, this heatmap tells a tale of interconnected relationships. To transform casual customers into loyal advocates, businesses should prioritize enhancing the quality of their offerings, while still valuing repeatability as a supportive ally. And thus, with this data in hand, they could strategize their way to greater success. 

Now in the second figure we'll see numerical columns spread themselves.  
  
![Figure](./histogram.png)

  
In a bustling data analysis room, three histograms stand proudly, each revealing its own story about a particular dataset. As we delve into their narratives, we notice the first histogram entitled "overall." Here, the distribution peaks dramatically between 1.5 and 2.0, indicating that a significant number of observations fall within this range. The elongated tail reaching toward 5.0 suggests a few standout cases—perhaps extraordinary performances that spark curiosity, yet they are just whispers in the grander scheme.

Next, we turn our attention to the "quality" histogram. Similar to its sibling, it showcases a robust concentration of values but centers around 1.5 to 2.5, with a notable absence of higher quality ratings. This pattern hints at a population that may struggle to attain high standards, igniting a quest for improvement among the subjects represented.

Finally, we encounter the "repeatability" histogram, a quieter silhouette in our trio. Most values cluster tightly around 1.5 to 1.75, while a few brave entries stretch toward 3.0. This suggests that while many instances can be reliably repeated, there are outliers that defy consistency. These rogue elements prompt questions: What accounts for their divergence?

Together, these histograms weave a narrative of a dataset rich in potential yet challenging in execution. They highlight both the strengths and weaknesses present, beckoning further exploration into the underlying factors that shape these distributions. The quest for improvement lies at the heart of this story, urging those involved to dig deeper, question assumptions, and strive for excellence.

Lastly, we'll see some mischievous datapoints that don't follow the trend (Outliers!).  
  
![Figure](./box_plot.png)

  
In the intriguing world of data, three box plots stand as storytellers, revealing the narratives behind the variables: Overall, Quality, and Repeatability. 

As we gaze at the first plot on Overall, we notice a sparse distribution. The whiskers indicate an array that stretches gracefully from slightly above 1 to around 5, but just a few outliers dare to step outside this range, hinting at a handful of extraordinary cases. Most values huddle around the lower end of the scale, suggesting a potential room for improvement.

Turning our attention to Quality, the plot presents a more balanced middle ground. With a median around 3.5, it showcases a more solid core of data. The interquartile range reveals that half of the observations are snugly situated between approximately 3 and 4. This cluster indicates that while there are some high-quality segments, there’s still a significant portion that may need attention, particularly those lingering just above the lower quartile.

Finally, we encounter Repeatability, which tells a tale of consistency but with a hint of caution. The median rests just above 2, and similar to Quality, we see a compact distribution. However, the whiskers reveal a wider spread in the values, hinting at variability that could impact reliability. The presence of outliers further emphasizes this inconsistency, suggesting some repeatability measures are far from the norm.

Together, these plots weave a narrative of insight, urging us to delve deeper into the data and foster improvements in the areas of overall performance, quality assurance, and consistency. The journey has just begun, and the exploration promises to uncover more valuable stories hidden within the numbers.

