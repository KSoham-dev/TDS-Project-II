
# Data Analysis Project

Hey! Hope you are doing fine. Hmm... You've got some interesting data I see.  
Let's begin this journey by first identifying what your data is like.  
So, you have 2652 rows and 8 columns in your data, and as I can  
see, this data is related to Reviews. Below are some key statistics  
about the data you provided:

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
### Correlation Heatmap
Understanding how numerical columns correlate with each other can provide insights into potential relationships and dependencies between variables. Here's a heatmap showing these correlations:

![Correlation Heatmap](./corr_hmap.png)

**Analysis for Correlation Heatmap:**

Analyzing the correlation heatmap of numerical features can reveal significant patterns and relationships between different variables. Let's break down the information presented.

### Overview of the Heatmap

The heatmap uses a color gradient to represent correlation coefficients, where:
- **1.0** signifies a perfect positive correlation (both variables move in the same direction).
- **-1.0** denotes a perfect negative correlation (one variable increases while the other decreases).
- **0.0** indicates no correlation.

### Correlation Values

1. **Overall vs. Quality**:
   - **Correlation Coefficient: 0.83**
   - This strong positive correlation indicates that as the overall score increases, the quality score also tends to increase significantly. This relationship suggests that improvements in overall metrics are inherently linked to enhancements in quality.

2. **Quality vs. Repeatability**:
   - **Correlation Coefficient: 0.31**
   - The moderate positive correlation here shows that there is some interdependence between quality and repeatability. However, the correlation is weaker than the previous pair, indicating that while they do influence each other to some extent, there are additional factors affecting quality and repeatability.

3. **Overall vs. Repeatability**:
   - **Correlation Coefficient: 0.51**
   - This indicates a modest positive correlation. It suggests that higher overall scores may lead to better repeatability scores, but the relationship is not as strong as that between overall and quality.

### Visual Analysis

- The **color gradient** from deep red (indicating strong correlations) to light blue (indicating weaker or no correlations) allows for quick visual inference.
- The cells with stronger correlations (especially between overall and quality) stand out prominently, while those with weaker correlations are visibly cooler in tone.

### Insights and Implications

- **Focus on Quality**: Given the strong correlation with the overall score, prioritizing quality improvement initiatives could yield significant benefits across the board.
- **Repeatability as an Area for Growth**: With a weaker correlation to overall metrics, there may be underlying factors affecting repeatability that need attention. Exploring the processes and practices related to repeatability might reveal avenues for improvement.
- **Balanced Approach**: Striking a balance between improving overall, quality, and repeatability will likely yield the best results. Investing resources in quality enhancements could naturally elevate overall performance without neglecting the need for consistent repeatability.

### Conclusion

In summary, this correlation heatmap provides essential insights into how key numerical features are interrelated. Making data-driven decisions based on these correlations can help streamline strategies for enhancing performance and efficiency within the examined area. Leveraging the strong relationship between overall performance and quality, while addressing repeatability, can pave the way for more robust outcomes.

### Histograms
Histograms help us understand the distribution of numerical columns. They can reveal patterns such as skewness, modality, and the presence of outliers. Here's a look at the histograms for the numerical columns:

![Histograms](./histogram.png)

**Analysis for Histograms:**

### Detailed Analysis of Histograms

The presented histograms provide insights into the distributions of several numerical features of a dataset—namely, "overall," "quality," and "repeatability." Below is a more detailed examination of each histogram:

#### 1. Overall Feature Distribution
- **Distribution Shape**: The histogram for the "overall" feature exhibits a highly concentrated distribution around a specific value, suggesting that most observations fall within a narrow range. This may indicate a commonality in the data or a potential limitation on values.
- **Peaks and Troughs**: A pronounced peak signifies that a particular score (presumably around 3) is predominant among the values. This might reflect a common rating, possibly indicative of average quality or acceptance in whatever context this dataset is derived from.
- **Implications**: The concentration could point to a need for more varied outcomes; either the scoring system is limited, or the sampled items tend to perform similarly.

#### 2. Quality Feature Distribution
- **Distribution Shape**: Similar to the "overall" feature, the "quality" histogram shows a skewed distribution with a pronounced peak, likely at 3.5. This reveals that most items in the dataset are perceived similarly well concerning quality.
- **Visual Gap**: The histogram displays multiple bars at equal intervals (1 to 5), which may imply rounding in ratings. For example, it seems many observations could not reach extreme values (like 1 or 5), suggesting a possible bias toward moderate evaluations.
- **Implications**: Consistent quality ratings may need further investigation; it would be beneficial to assess whether these ratings are impacted by external factors or if they're inherently limited by the evaluation criteria.

#### 3. Repeatability Feature Distribution
- **Distribution Shape**: The "repeatability" feature histogram indicates a wider spread with fewer items concentrated in lower scores compared to the other two features.
- **Skewness**: The distribution shows a heavy left skew, implying that very few instances achieve the higher, more favorable scores (likely in the 3 to 3.6 range), but it certainly depicts repeated observations with a significant cluster around the 1 to 2 range.
- **Implications**: This aspect could indicate issues with consistency in measurements or experiences. If higher repeatability is desired, this may constitute a challenge, as lower repeatability could result in variability in outcomes, potentially undermining reliability.

### Conclusion
Overall, the histograms reveal a dataset with notable concentration around specific ratings, particularly in "overall" and "quality," while "repeatability" shows more variation with potential reliability issues. These patterns suggest further exploration is warranted to understand the fundamental reasons behind the distributions. The strong contrition in ratings also raises questions regarding the evaluation methods and the criteria used, hinting that the ratings might benefit from a review or a more nuanced assessment approach. 

In practice, stakeholders might want to investigate why certain features score consistently low or highly, which could inform decisions for quality improvement or standardization of processes.

### Box Plots
Box plots are useful for identifying outliers and understanding the spread and central tendency of the data. Here's a look at the box plots for the numerical columns:

![Box Plots](./box_plot.png)

**Analysis for Box Plots:**

Let's dive into the box plots presented in the figure, each representing different variables: Overall, Quality, and Repeatability. 

### Overall Box Plot
- **Central Tendency**: The median appears to lie slightly above 3. This suggests a generally acceptable level of performance, but it may not be optimal.
- **Spread**: The interquartile range (IQR) is relatively small, indicating that most of the data points are closely grouped around the median, which is a sign of consistency.
- **Outliers**: There are a few outliers marked as points above the upper whisker. This could signify exceptional or problematic cases that warrant further investigation.

### Quality Box Plot
- **Central Tendency**: The median for Quality is around 3.5, which suggests a decent level of quality, although there is room for improvement.
- **Spread**: The IQR here seems to be larger than that in the Overall box plot. This indicates more variability in quality levels, suggesting that some units exhibit significantly higher or lower quality.
- **Outliers**: The plot shows a couple of significant outliers on the lower end. These outliers could represent instances of particularly low quality that may need addressing.

### Repeatability Box Plot
- **Central Tendency**: The median for Repeatability is notably lower, around 1.5, pointing to issues in consistency and reliability.
- **Spread**: The IQR is quite extensive, signifying a broad range of repeatability scores. This variability is concerning, as it indicates inconsistencies in how repeatable the measurements or processes are.
- **Outliers**: There are several outliers present at both the upper and lower ends, suggesting that some measurements are significantly different from the rest. This might indicate specific failures in repeatability that could affect overall performance.

### Comparative Insights
- **Overall Performance vs. Repeatability**: It’s interesting to note that despite a decent overall performance indicated by the Overall box plot, the repeatability issues highlighted in the Repeatability plot could undermine confidence in these results. Consistency is key, and if repeatability is lacking, it may impact the overall rating.
- **Quality Variability**: The wider spread in the Quality scores shows that while some instances deliver high quality, there are lower-quality outcomes that could be improved. This suggests a need for targeted interventions to elevate the overall quality experience.
- **Actionable Steps**: The presence of outliers across all plots suggests that a deeper dive into these specific cases could uncover insights that inform future improvements.

### Conclusion
These box plots effectively illustrate the distribution and central tendencies of the three variables. While overall performance seems acceptable, the issues with quality variability and repeatability signal a need for further examination and potential enhancement in processes to achieve higher consistency and quality. Addressing these outliers and inconsistencies could significantly boost overall performance and reliability.

## Chi-Square Test Reports
Chi-square tests help us understand the relationships between categorical variables. Here are the results of the chi-square tests for pairs of categorical columns:

### Chi-Square Test for date and language

| Metric               | Value               |
|----------------------|---------------------|
| Chi-Square Statistic | 20570.5270           |
| p-value              | 0.4389             |
| Degrees of Freedom   | 20540                |
| Interpretation       | Not Significant      |



### Chi-Square Test for date and type

| Metric               | Value               |
|----------------------|---------------------|
| Chi-Square Statistic | 15493.1025           |
| p-value              | 0.0000             |
| Degrees of Freedom   | 14378                |
| Interpretation       | Significant      |



### Chi-Square Test for date and title

| Metric               | Value               |
|----------------------|---------------------|
| Chi-Square Statistic | 4545618.8639           |
| p-value              | 1.0000             |
| Degrees of Freedom   | 4578366                |
| Interpretation       | Not Significant      |



### Chi-Square Test for date and by

| Metric               | Value               |
|----------------------|---------------------|
| Chi-Square Statistic | 2954953.2849           |
| p-value              | 0.0000             |
| Degrees of Freedom   | 2928632                |
| Interpretation       | Significant      |



### Chi-Square Test for language and type

| Metric               | Value               |
|----------------------|---------------------|
| Chi-Square Statistic | 829.0961           |
| p-value              | 0.0000             |
| Degrees of Freedom   | 70                |
| Interpretation       | Significant      |



### Chi-Square Test for language and title

| Metric               | Value               |
|----------------------|---------------------|
| Chi-Square Statistic | 26334.1340           |
| p-value              | 0.0000             |
| Degrees of Freedom   | 23110                |
| Interpretation       | Significant      |



### Chi-Square Test for language and by

| Metric               | Value               |
|----------------------|---------------------|
| Chi-Square Statistic | 18226.2025           |
| p-value              | 0.0000             |
| Degrees of Freedom   | 12216                |
| Interpretation       | Significant      |



### Chi-Square Test for type and title

| Metric               | Value               |
|----------------------|---------------------|
| Chi-Square Statistic | 18094.2420           |
| p-value              | 0.0000             |
| Degrees of Freedom   | 16177                |
| Interpretation       | Significant      |



### Chi-Square Test for type and by

| Metric               | Value               |
|----------------------|---------------------|
| Chi-Square Statistic | 15971.2574           |
| p-value              | 0.0000             |
| Degrees of Freedom   | 10689                |
| Interpretation       | Significant      |



### Chi-Square Test for title and by

| Metric               | Value               |
|----------------------|---------------------|
| Chi-Square Statistic | 3576819.2435           |
| p-value              | 0.0000             |
| Degrees of Freedom   | 3156309                |
| Interpretation       | Significant      |


