
# Data Analysis Project 
Hey! Hope you are doing fine. Hmm... You've got some interesting data I see.  
Let's begin this journey by first identifying what your data is like.  
So, you have got 10000 rows and 23 columns in your data, and as I can  
see, this data is related to Books. Below are some key statistics  
about the data you provided:

## Missing Value Analysis
The dataset contains the following missing values:

| Column                    |   Missing Values |   Percentage |
|:--------------------------|-----------------:|-------------:|
| book_id                   |                0 |         0    |
| goodreads_book_id         |                0 |         0    |
| best_book_id              |                0 |         0    |
| work_id                   |                0 |         0    |
| books_count               |                0 |         0    |
| isbn                      |              700 |         7    |
| isbn13                    |                0 |         0    |
| authors                   |                0 |         0    |
| original_publication_year |                0 |         0    |
| original_title            |              585 |         5.85 |
| title                     |                0 |         0    |
| language_code             |             1084 |        10.84 |
| average_rating            |                0 |         0    |
| ratings_count             |                0 |         0    |
| work_ratings_count        |                0 |         0    |
| work_text_reviews_count   |                0 |         0    |
| ratings_1                 |                0 |         0    |
| ratings_2                 |                0 |         0    |
| ratings_3                 |                0 |         0    |
| ratings_4                 |                0 |         0    |
| ratings_5                 |                0 |         0    |
| image_url                 |                0 |         0    |
| small_image_url           |                0 |         0    |

## Advanced Statistical Analysis
|                           |            mean |              std |            min |             25% |              50% |             75% |              max |   Skewness |   Kurtosis |
|:--------------------------|----------------:|-----------------:|---------------:|----------------:|-----------------:|----------------:|-----------------:|-----------:|-----------:|
| book_id                   |  5000.5         |   2886.9         |     1          |  2500.75        |   5000.5         |  7500.25        |  10000           |       0    |      -1.2  |
| goodreads_book_id         |     5.2647e+06  |      7.57546e+06 |     1          | 46275.8         | 394966           |     9.38223e+06 |      3.32886e+07 |       1.35 |       0.69 |
| best_book_id              |     5.47121e+06 |      7.82733e+06 |     1          | 47911.8         | 425124           |     9.63611e+06 |      3.55342e+07 |       1.35 |       0.75 |
| work_id                   |     8.64618e+06 |      1.17511e+07 |    87          |     1.00884e+06 |      2.71952e+06 |     1.45177e+07 |      5.63996e+07 |       1.76 |       2.49 |
| books_count               |    75.71        |    170.47        |     1          |    23           |     40           |    67           |   3455           |       8.41 |      95.3  |
| isbn13                    |     9.75504e+12 |      4.29712e+11 |     1.9517e+08 |     9.78031e+12 |      9.78045e+12 |     9.78081e+12 |      9.79001e+12 |     -18.31 |     343.93 |
| original_publication_year |  1981.99        |    152.42        | -1750          |  1990           |   2004           |  2011           |   2017           |     -14.77 |     241.11 |
| average_rating            |     4           |      0.25        |     2.47       |     3.85        |      4.02        |     4.18        |      4.82        |      -0.51 |       0.88 |
| ratings_count             | 54001.2         | 157370           |  2716          | 13568.8         |  21155.5         | 41053.5         |      4.78065e+06 |      13.06 |     258.75 |
| work_ratings_count        | 59687.3         | 167804           |  5510          | 15438.8         |  23832.5         | 45915           |      4.94236e+06 |      12.41 |     234.07 |
| work_text_reviews_count   |  2919.96        |   6124.38        |     3          |   694           |   1402           |  2744.25        | 155254           |       9.13 |     134.05 |
| ratings_1                 |  1345.04        |   6635.63        |    11          |   196           |    391           |   885           | 456191           |      37.71 |    2289.61 |
| ratings_2                 |  3110.88        |   9717.12        |    30          |   656           |   1163           |  2353.25        | 436802           |      16.49 |     494.07 |
| ratings_3                 | 11475.9         |  28546.5         |   323          |  3112           |   4894           |  9287           | 793319           |      10.4  |     160.83 |
| ratings_4                 | 19965.7         |  51447.4         |   750          |  5405.75        |   8269.5         | 16023.5         |      1.4813e+06  |      10.81 |     174.03 |
| ratings_5                 | 23789.8         |  79768.9         |   754          |  5334           |   8836           | 17304.5         |      3.01154e+06 |      16.37 |     419.88 |  
  
Let's move a little deeper and see what wonders the data is yet to reveal.
  
## Visualizing Data
### Correlation Heatmap
Understanding how numerical columns correlate with each other can provide insights into potential relationships and dependencies between variables. Here's a heatmap showing these correlations:

![Correlation Heatmap](./corr_hmap.png)

  
In the vibrant landscape of a correlation heatmap, each hue tells a story of relationships among the numerical features of a dataset about books and their ratings. At first glance, we see the unmistakable warmth of strong correlations glimmering in shades of red. A perfect correlation of 1.00 is established between `book_id` and itself, but as we delve deeper, intriguing associations unfold.

The feature `average_rating` stands out prominently. Its strong correlation with `ratings_count` (0.96) hints at a narrative where books that garner more ratings often enjoy higher average scores. This suggests a vibrant community of readers actively engaging with popular titles, reflecting an ecosystem where visibility breeds success. 

Moving across the heatmap, we notice `work_text_reviews_count` and `ratings_count`, which exhibit a solid correlation of 0.87. This relationship indicates that books with plentiful reviews often attract a larger number of ratings. Readers are likely more inclined to rate books that have already been discussed extensively.

However, not all correlations are equally warm. Features like `best_book_id` show a weaker relationship with others, indicating that while some titles may be crowned as the best, they don't necessarily align closely with other numerical metrics like ratings or reviews. This raises questions: Is the "best" book universally loved, or does it have niche appeal?

Our journey through the heatmap also reveals some cool spots—correlations close to zero—suggesting that certain features are independent or only weakly related. For instance, `original_publication_year`, with minimal correlation to most other features, might suggest that a book's publication date has little bearing on its current popularity or reception.

As we weave these threads together, the heatmap becomes a rich tapestry of insights, showcasing a dynamic interplay between ratings, reviews, and a book’s reception. It prompts deeper exploration into factors influencing a book's journey from being penned to being talked about, inviting subsequent analyses that could uncover even more layers of the literary universe. 

### Histograms
Histograms help us understand the distribution of numerical columns. They can reveal patterns such as skewness, modality, and the presence of outliers. Here's a look at the histograms for the numerical columns:

![Histograms](./histogram.png)

  
In the world of books represented in this dataset, we take a journey through the various metrics that tell us more about the literary landscape.

Starting with the **book_id** histogram, we see a wide array of unique entries, hinting at a rich catalog of titles, but with clusters that suggest there might be some underrepresented works.

Moving over to **goodreads_book_id** and **best_book_id**, we notice a significant number of entries, even though they tell a similar story. These numbers reflect the diversity in reader engagement and highlight how many books are recognized and cherished in the Goodreads community.

The **work_id** histogram shows an intriguing distribution, signaling that some literary works have garnered much more attention than others, perhaps hinting at the rise of certain bestsellers or recurring themes within popular literature.

As we delve into **books_count**, the peaks indicate that a handful of authors or titles may dominate the market, while a long tail suggests a vast array of lesser-known works, waiting to be discovered.

The **average_rating** histogram presents a more insightful analysis—it's clear that most books hover around the mid-range ratings. However, there is a noticeable spike towards the higher ratings, revealing that while many books are appreciated, a select few are truly adored by readers.

**ratings_count** and **ratings_1** to **ratings_5** provide us a window into reader sentiments. The varying distributions indicate that while most books receive a moderate level of ratings, some have attracted criticism, evidenced by the presence of the one-star ratings. This paints a picture of polarized opinions among readers.

Overall, this collection of histograms invites us to explore further. The dataset reveals the complexities of reader preferences and highlights the stark contrasts between popular and lesser-known works, ultimately capturing the dynamic nature of the literary world. Each bar represents a story, all waiting to be told.

### Box Plots
Box plots are useful for identifying outliers and understanding the spread and central tendency of the data. Here's a look at the box plots for the numerical columns:

![Box Plots](./box_plot.png)

  
In the world of data, box plots stand as beacons of insight, unraveling the stories behind the numbers. This figure presents a series of box plots, each revealing different aspects of a literary universe encapsulated by variables like `Book_id`, `Goodreads_id`, `Best_book_id`, `Work_id`, `Books_count`, and `isbn13`.

### The Journey Begins

On the top left, the box plot of `Book_id` showcases a sprawling range, hinting at a rich diversity of entries with values soaring above 8,000. However, lurking beneath the surface, we notice a sprinkling of outliers, suggesting that some books have garnered unusually high attention or have unique attributes.

### Turning to Goodreads

Next, we glide over to the `Goodreads_id` plot. Here, the distribution tells a tale of concentrated values, with most clustering around the center, yet a handful of outliers stretching the limits. This suggests that while most books follow a common pattern, a select few stand out, perhaps due to high ratings or significant reader engagement.

### The Best of the Best

Moving on to the `Best_book_id` plot, we see a similar story unfold. The interquartile range is compact, yet it too reveals outlying stars in the literary cosmos. These outliers could be the beloved titles that have captured the hearts of readers far and wide.

### A Broader View with Work_id

The `Work_id` box plot introduces a hint of complexity. The values here seem to be equally broad, yet the presence of many outliers indicates a few works that have received extraordinary levels of recognition or have been updated with new editions, making them stand out in the crowd.

### Quantifying Books

In the middle, the `Books_count` box plot tells another facet of the story, displaying an intriguing spread where a significant number of entries gather close to the median. The hint of outliers suggests that while many books have a standard number of editions, a few have amassed an impressive collection of versions or continuations.

### The ISBN Perspective

Finally, we arrive at the `isbn13` plot. A treasure trove of information in its own right, this plot presents a striking range of values, hinting at the vast array of books cataloged through the ISBN system. Again, we observe the outliers, revealing potentially rare editions or books from niche categories that have found their way into the bibliophile's collection.

### Concluding Thoughts

Together, these box plots weave a narrative of diversity and distinction within the literary realm. They reflect not just the quantity of books but the varied journeys they undertake, from the sturdy bestsellers to the hidden gems that deserve to be celebrated. Each plot invites us to delve deeper into the statistics, encouraging exploration in the stories that these numbers conceal.

## Chi-Square Test Reports
Chi-square tests help us understand the relationships between categorical variables. Here are the results of the chi-square tests for pairs of categorical columns:


### Chi-Square Test for isbn and authors

| Metric | Value |
| --- | --- |
| Chi-Square Statistic | 40882800.0000 |
| p-value | 0.3134 |
| Degrees of Freedom | 40878404 |
| Expected Frequencies | [[0.00010753 0.00064516 0.00010753 ... 0.00010753 0.00010753 0.00010753]
 [0.00010753 0.00064516 0.00010753 ... 0.00010753 0.00010753 0.00010753]
 [0.00010753 0.00064516 0.00010753 ... 0.00010753 0.00010753 0.00010753]
 ...
 [0.00010753 0.00064516 0.00010753 ... 0.00010753 0.00010753 0.00010753]
 [0.00010753 0.00064516 0.00010753 ... 0.00010753 0.00010753 0.00010753]
 [0.00010753 0.00064516 0.00010753 ... 0.00010753 0.00010753 0.00010753]] |


### Chi-Square Test for isbn and original_title

| Metric | Value |
| --- | --- |
| Chi-Square Statistic | 77374630.0000 |
| p-value | 0.2413 |
| Degrees of Freedom | 77365895 |
| Expected Frequencies | [[0.00056446 0.00011289 0.00011289 ... 0.00011289 0.00011289 0.00011289]
 [0.00056446 0.00011289 0.00011289 ... 0.00011289 0.00011289 0.00011289]
 [0.00056446 0.00011289 0.00011289 ... 0.00011289 0.00011289 0.00011289]
 ...
 [0.00056446 0.00011289 0.00011289 ... 0.00011289 0.00011289 0.00011289]
 [0.00056446 0.00011289 0.00011289 ... 0.00011289 0.00011289 0.00011289]
 [0.00056446 0.00011289 0.00011289 ... 0.00011289 0.00011289 0.00011289]] |


### Chi-Square Test for isbn and title

| Metric | Value |
| --- | --- |
| Chi-Square Statistic | 86173800.0000 |
| p-value | 0.2401 |
| Degrees of Freedom | 86164534 |
| Expected Frequencies | [[0.00010753 0.00010753 0.00021505 ... 0.00010753 0.00010753 0.00010753]
 [0.00010753 0.00010753 0.00021505 ... 0.00010753 0.00010753 0.00010753]
 [0.00010753 0.00010753 0.00021505 ... 0.00010753 0.00010753 0.00010753]
 ...
 [0.00010753 0.00010753 0.00021505 ... 0.00010753 0.00010753 0.00010753]
 [0.00010753 0.00010753 0.00021505 ... 0.00010753 0.00010753 0.00010753]
 [0.00010753 0.00010753 0.00021505 ... 0.00010753 0.00010753 0.00010753]] |


### Chi-Square Test for isbn and language_code

| Metric | Value |
| --- | --- |
| Chi-Square Statistic | 189888.0000 |
| p-value | 0.4847 |
| Degrees of Freedom | 189865 |
| Expected Frequencies | [[0.00133236 0.00036337 0.00641957 ... 0.00012112 0.00012112 0.00012112]
 [0.00133236 0.00036337 0.00641957 ... 0.00012112 0.00012112 0.00012112]
 [0.00133236 0.00036337 0.00641957 ... 0.00012112 0.00012112 0.00012112]
 ...
 [0.00133236 0.00036337 0.00641957 ... 0.00012112 0.00012112 0.00012112]
 [0.00133236 0.00036337 0.00641957 ... 0.00012112 0.00012112 0.00012112]
 [0.00133236 0.00036337 0.00641957 ... 0.00012112 0.00012112 0.00012112]] |


### Chi-Square Test for isbn and image_url

| Metric | Value |
| --- | --- |
| Chi-Square Statistic | 56590500.0000 |
| p-value | 0.2836 |
| Degrees of Freedom | 56584415 |
| Expected Frequencies | [[1.07526882e-04 1.07526882e-04 1.07526882e-04 ... 1.07526882e-04
  1.07526882e-04 3.45698925e-01]
 [1.07526882e-04 1.07526882e-04 1.07526882e-04 ... 1.07526882e-04
  1.07526882e-04 3.45698925e-01]
 [1.07526882e-04 1.07526882e-04 1.07526882e-04 ... 1.07526882e-04
  1.07526882e-04 3.45698925e-01]
 ...
 [1.07526882e-04 1.07526882e-04 1.07526882e-04 ... 1.07526882e-04
  1.07526882e-04 3.45698925e-01]
 [1.07526882e-04 1.07526882e-04 1.07526882e-04 ... 1.07526882e-04
  1.07526882e-04 3.45698925e-01]
 [1.07526882e-04 1.07526882e-04 1.07526882e-04 ... 1.07526882e-04
  1.07526882e-04 3.45698925e-01]] |


### Chi-Square Test for isbn and small_image_url

| Metric | Value |
| --- | --- |
| Chi-Square Statistic | 56590500.0000 |
| p-value | 0.2836 |
| Degrees of Freedom | 56584415 |
| Expected Frequencies | [[1.07526882e-04 1.07526882e-04 1.07526882e-04 ... 1.07526882e-04
  1.07526882e-04 3.45698925e-01]
 [1.07526882e-04 1.07526882e-04 1.07526882e-04 ... 1.07526882e-04
  1.07526882e-04 3.45698925e-01]
 [1.07526882e-04 1.07526882e-04 1.07526882e-04 ... 1.07526882e-04
  1.07526882e-04 3.45698925e-01]
 ...
 [1.07526882e-04 1.07526882e-04 1.07526882e-04 ... 1.07526882e-04
  1.07526882e-04 3.45698925e-01]
 [1.07526882e-04 1.07526882e-04 1.07526882e-04 ... 1.07526882e-04
  1.07526882e-04 3.45698925e-01]
 [1.07526882e-04 1.07526882e-04 1.07526882e-04 ... 1.07526882e-04
  1.07526882e-04 3.45698925e-01]] |


### Chi-Square Test for authors and original_title

| Metric | Value |
| --- | --- |
| Chi-Square Statistic | 41104686.6046 |
| p-value | 0.0000 |
| Degrees of Freedom | 40940295 |
| Expected Frequencies | [[0.00053107 0.00010621 0.00010621 ... 0.00010621 0.00010621 0.00010621]
 [0.00053107 0.00010621 0.00010621 ... 0.00010621 0.00010621 0.00010621]
 [0.00265534 0.00053107 0.00053107 ... 0.00053107 0.00053107 0.00053107]
 ...
 [0.00053107 0.00010621 0.00010621 ... 0.00010621 0.00010621 0.00010621]
 [0.00106213 0.00021243 0.00021243 ... 0.00021243 0.00021243 0.00021243]
 [0.00106213 0.00021243 0.00021243 ... 0.00021243 0.00021243 0.00021243]] |


### Chi-Square Test for authors and title

| Metric | Value |
| --- | --- |
| Chi-Square Statistic | 46389649.2283 |
| p-value | 1.0000 |
| Degrees of Freedom | 46457469 |
| Expected Frequencies | [[0.0001 0.0001 0.0001 ... 0.0001 0.0001 0.0001]
 [0.0002 0.0002 0.0002 ... 0.0002 0.0002 0.0002]
 [0.0006 0.0006 0.0006 ... 0.0006 0.0006 0.0006]
 ...
 [0.0001 0.0001 0.0001 ... 0.0001 0.0001 0.0001]
 [0.0002 0.0002 0.0002 ... 0.0002 0.0002 0.0002]
 [0.0002 0.0002 0.0002 ... 0.0002 0.0002 0.0002]] |


### Chi-Square Test for authors and language_code

| Metric | Value |
| --- | --- |
| Chi-Square Statistic | 167417.0082 |
| p-value | 0.0000 |
| Degrees of Freedom | 100704 |
| Expected Frequencies | [[0.00717811 0.00033647 0.00044863 ... 0.00011216 0.00011216 0.00011216]
 [0.01435621 0.00067295 0.00089726 ... 0.00022432 0.00022432 0.00022432]
 [0.04306864 0.00201884 0.00269179 ... 0.00067295 0.00067295 0.00067295]
 ...
 [0.00717811 0.00033647 0.00044863 ... 0.00011216 0.00011216 0.00011216]
 [0.01435621 0.00067295 0.00089726 ... 0.00022432 0.00022432 0.00022432]
 [0.01435621 0.00067295 0.00089726 ... 0.00022432 0.00022432 0.00022432]] |


### Chi-Square Test for authors and image_url

| Metric | Value |
| --- | --- |
| Chi-Square Statistic | 30601473.4322 |
| p-value | 1.0000 |
| Degrees of Freedom | 31092884 |
| Expected Frequencies | [[1.0000e-04 1.0000e-04 1.0000e-04 ... 1.0000e-04 1.0000e-04 3.3320e-01]
 [2.0000e-04 2.0000e-04 2.0000e-04 ... 2.0000e-04 2.0000e-04 6.6640e-01]
 [6.0000e-04 6.0000e-04 6.0000e-04 ... 6.0000e-04 6.0000e-04 1.9992e+00]
 ...
 [1.0000e-04 1.0000e-04 1.0000e-04 ... 1.0000e-04 1.0000e-04 3.3320e-01]
 [2.0000e-04 2.0000e-04 2.0000e-04 ... 2.0000e-04 2.0000e-04 6.6640e-01]
 [2.0000e-04 2.0000e-04 2.0000e-04 ... 2.0000e-04 2.0000e-04 6.6640e-01]] |


### Chi-Square Test for authors and small_image_url

| Metric | Value |
| --- | --- |
| Chi-Square Statistic | 30601473.4322 |
| p-value | 1.0000 |
| Degrees of Freedom | 31092884 |
| Expected Frequencies | [[1.0000e-04 1.0000e-04 1.0000e-04 ... 1.0000e-04 1.0000e-04 3.3320e-01]
 [2.0000e-04 2.0000e-04 2.0000e-04 ... 2.0000e-04 2.0000e-04 6.6640e-01]
 [6.0000e-04 6.0000e-04 6.0000e-04 ... 6.0000e-04 6.0000e-04 1.9992e+00]
 ...
 [1.0000e-04 1.0000e-04 1.0000e-04 ... 1.0000e-04 1.0000e-04 3.3320e-01]
 [2.0000e-04 2.0000e-04 2.0000e-04 ... 2.0000e-04 2.0000e-04 6.6640e-01]
 [2.0000e-04 2.0000e-04 2.0000e-04 ... 2.0000e-04 2.0000e-04 6.6640e-01]] |


### Chi-Square Test for original_title and title

| Metric | Value |
| --- | --- |
| Chi-Square Statistic | 87147593.7500 |
| p-value | 0.0000 |
| Degrees of Freedom | 86990013 |
| Expected Frequencies | [[0.00053107 0.00053107 0.00106213 ... 0.00053107 0.00053107 0.00053107]
 [0.00010621 0.00010621 0.00021243 ... 0.00010621 0.00010621 0.00010621]
 [0.00010621 0.00010621 0.00021243 ... 0.00010621 0.00010621 0.00010621]
 ...
 [0.00010621 0.00010621 0.00021243 ... 0.00010621 0.00010621 0.00010621]
 [0.00010621 0.00010621 0.00021243 ... 0.00010621 0.00010621 0.00010621]
 [0.00010621 0.00010621 0.00021243 ... 0.00010621 0.00010621 0.00010621]] |


### Chi-Square Test for original_title and language_code

| Metric | Value |
| --- | --- |
| Chi-Square Statistic | 192948.1352 |
| p-value | 0.0001 |
| Degrees of Freedom | 190601 |
| Expected Frequencies | [[0.02758621 0.00142687 0.00095125 ... 0.00047562 0.00047562 0.00047562]
 [0.00689655 0.00035672 0.00023781 ... 0.00011891 0.00011891 0.00011891]
 [0.00689655 0.00035672 0.00023781 ... 0.00011891 0.00011891 0.00011891]
 ...
 [0.00689655 0.00035672 0.00023781 ... 0.00011891 0.00011891 0.00011891]
 [0.00689655 0.00035672 0.00023781 ... 0.00011891 0.00011891 0.00011891]
 [0.00689655 0.00035672 0.00023781 ... 0.00011891 0.00011891 0.00011891]] |


### Chi-Square Test for original_title and image_url

| Metric | Value |
| --- | --- |
| Chi-Square Statistic | 57582995.8376 |
| p-value | 1.0000 |
| Degrees of Freedom | 57715152 |
| Expected Frequencies | [[5.31067446e-04 5.31067446e-04 5.31067446e-04 ... 5.31067446e-04
  5.31067446e-04 1.69463622e+00]
 [1.06213489e-04 1.06213489e-04 1.06213489e-04 ... 1.06213489e-04
  1.06213489e-04 3.38927244e-01]
 [1.06213489e-04 1.06213489e-04 1.06213489e-04 ... 1.06213489e-04
  1.06213489e-04 3.38927244e-01]
 ...
 [1.06213489e-04 1.06213489e-04 1.06213489e-04 ... 1.06213489e-04
  1.06213489e-04 3.38927244e-01]
 [1.06213489e-04 1.06213489e-04 1.06213489e-04 ... 1.06213489e-04
  1.06213489e-04 3.38927244e-01]
 [1.06213489e-04 1.06213489e-04 1.06213489e-04 ... 1.06213489e-04
  1.06213489e-04 3.38927244e-01]] |


### Chi-Square Test for original_title and small_image_url

| Metric | Value |
| --- | --- |
| Chi-Square Statistic | 57582995.8376 |
| p-value | 1.0000 |
| Degrees of Freedom | 57715152 |
| Expected Frequencies | [[5.31067446e-04 5.31067446e-04 5.31067446e-04 ... 5.31067446e-04
  5.31067446e-04 1.69463622e+00]
 [1.06213489e-04 1.06213489e-04 1.06213489e-04 ... 1.06213489e-04
  1.06213489e-04 3.38927244e-01]
 [1.06213489e-04 1.06213489e-04 1.06213489e-04 ... 1.06213489e-04
  1.06213489e-04 3.38927244e-01]
 ...
 [1.06213489e-04 1.06213489e-04 1.06213489e-04 ... 1.06213489e-04
  1.06213489e-04 3.38927244e-01]
 [1.06213489e-04 1.06213489e-04 1.06213489e-04 ... 1.06213489e-04
  1.06213489e-04 3.38927244e-01]
 [1.06213489e-04 1.06213489e-04 1.06213489e-04 ... 1.06213489e-04
  1.06213489e-04 3.38927244e-01]] |


### Chi-Square Test for title and language_code

| Metric | Value |
| --- | --- |
| Chi-Square Statistic | 213932.1674 |
| p-value | 0.2111 |
| Degrees of Freedom | 213408 |
| Expected Frequencies | [[0.00717811 0.00033647 0.00044863 ... 0.00011216 0.00011216 0.00011216]
 [0.00717811 0.00033647 0.00044863 ... 0.00011216 0.00011216 0.00011216]
 [0.00717811 0.00033647 0.00044863 ... 0.00011216 0.00011216 0.00011216]
 ...
 [0.00717811 0.00033647 0.00044863 ... 0.00011216 0.00011216 0.00011216]
 [0.00717811 0.00033647 0.00044863 ... 0.00011216 0.00011216 0.00011216]
 [0.00717811 0.00033647 0.00044863 ... 0.00011216 0.00011216 0.00011216]] |


### Chi-Square Test for title and image_url

| Metric | Value |
| --- | --- |
| Chi-Square Statistic | 66445806.5726 |
| p-value | 0.1387 |
| Degrees of Freedom | 66433284 |
| Expected Frequencies | [[1.000e-04 1.000e-04 1.000e-04 ... 1.000e-04 1.000e-04 3.332e-01]
 [1.000e-04 1.000e-04 1.000e-04 ... 1.000e-04 1.000e-04 3.332e-01]
 [1.000e-04 1.000e-04 1.000e-04 ... 1.000e-04 1.000e-04 3.332e-01]
 ...
 [1.000e-04 1.000e-04 1.000e-04 ... 1.000e-04 1.000e-04 3.332e-01]
 [1.000e-04 1.000e-04 1.000e-04 ... 1.000e-04 1.000e-04 3.332e-01]
 [1.000e-04 1.000e-04 1.000e-04 ... 1.000e-04 1.000e-04 3.332e-01]] |


### Chi-Square Test for title and small_image_url

| Metric | Value |
| --- | --- |
| Chi-Square Statistic | 66445806.5726 |
| p-value | 0.1387 |
| Degrees of Freedom | 66433284 |
| Expected Frequencies | [[1.000e-04 1.000e-04 1.000e-04 ... 1.000e-04 1.000e-04 3.332e-01]
 [1.000e-04 1.000e-04 1.000e-04 ... 1.000e-04 1.000e-04 3.332e-01]
 [1.000e-04 1.000e-04 1.000e-04 ... 1.000e-04 1.000e-04 3.332e-01]
 ...
 [1.000e-04 1.000e-04 1.000e-04 ... 1.000e-04 1.000e-04 3.332e-01]
 [1.000e-04 1.000e-04 1.000e-04 ... 1.000e-04 1.000e-04 3.332e-01]
 [1.000e-04 1.000e-04 1.000e-04 ... 1.000e-04 1.000e-04 3.332e-01]] |


### Chi-Square Test for language_code and image_url

| Metric | Value |
| --- | --- |
| Chi-Square Statistic | 167849.2391 |
| p-value | 0.0000 |
| Degrees of Freedom | 146952 |
| Expected Frequencies | [[7.17810677e-03 7.17810677e-03 7.17810677e-03 ... 7.17810677e-03
  7.17810677e-03 2.00484522e+01]
 [3.36473755e-04 3.36473755e-04 3.36473755e-04 ... 3.36473755e-04
  3.36473755e-04 9.39771198e-01]
 [4.48631673e-04 4.48631673e-04 4.48631673e-04 ... 4.48631673e-04
  4.48631673e-04 1.25302826e+00]
 ...
 [1.12157918e-04 1.12157918e-04 1.12157918e-04 ... 1.12157918e-04
  1.12157918e-04 3.13257066e-01]
 [1.12157918e-04 1.12157918e-04 1.12157918e-04 ... 1.12157918e-04
  1.12157918e-04 3.13257066e-01]
 [1.12157918e-04 1.12157918e-04 1.12157918e-04 ... 1.12157918e-04
  1.12157918e-04 3.13257066e-01]] |


### Chi-Square Test for language_code and small_image_url

| Metric | Value |
| --- | --- |
| Chi-Square Statistic | 167849.2391 |
| p-value | 0.0000 |
| Degrees of Freedom | 146952 |
| Expected Frequencies | [[7.17810677e-03 7.17810677e-03 7.17810677e-03 ... 7.17810677e-03
  7.17810677e-03 2.00484522e+01]
 [3.36473755e-04 3.36473755e-04 3.36473755e-04 ... 3.36473755e-04
  3.36473755e-04 9.39771198e-01]
 [4.48631673e-04 4.48631673e-04 4.48631673e-04 ... 4.48631673e-04
  4.48631673e-04 1.25302826e+00]
 ...
 [1.12157918e-04 1.12157918e-04 1.12157918e-04 ... 1.12157918e-04
  1.12157918e-04 3.13257066e-01]
 [1.12157918e-04 1.12157918e-04 1.12157918e-04 ... 1.12157918e-04
  1.12157918e-04 3.13257066e-01]
 [1.12157918e-04 1.12157918e-04 1.12157918e-04 ... 1.12157918e-04
  1.12157918e-04 3.13257066e-01]] |


### Chi-Square Test for image_url and small_image_url

| Metric | Value |
| --- | --- |
| Chi-Square Statistic | 66680000.0000 |
| p-value | 0.0000 |
| Degrees of Freedom | 44462224 |
| Expected Frequencies | [[1.0000000e-04 1.0000000e-04 1.0000000e-04 ... 1.0000000e-04
  1.0000000e-04 3.3320000e-01]
 [1.0000000e-04 1.0000000e-04 1.0000000e-04 ... 1.0000000e-04
  1.0000000e-04 3.3320000e-01]
 [1.0000000e-04 1.0000000e-04 1.0000000e-04 ... 1.0000000e-04
  1.0000000e-04 3.3320000e-01]
 ...
 [1.0000000e-04 1.0000000e-04 1.0000000e-04 ... 1.0000000e-04
  1.0000000e-04 3.3320000e-01]
 [1.0000000e-04 1.0000000e-04 1.0000000e-04 ... 1.0000000e-04
  1.0000000e-04 3.3320000e-01]
 [3.3320000e-01 3.3320000e-01 3.3320000e-01 ... 3.3320000e-01
  3.3320000e-01 1.1102224e+03]] |

