
# Data Analysis Project 
Hey! Hope you are doing fine. Hmm... You've got some interesting data I  
see. Let's begin this journey with fist identifying what your data is like.  
So, you have got 10000 rows and 23 columns in your data and  
as I can see this data this data is related to Books. Below are some key  
statistics about the data you provided

## Key Statistics
|       |   book_id |   goodreads_book_id |     best_book_id |         work_id |   books_count |         isbn13 |   original_publication_year |   average_rating |    ratings_count |   work_ratings_count |   work_text_reviews_count |   ratings_1 |   ratings_2 |   ratings_3 |      ratings_4 |       ratings_5 |
|:------|----------:|--------------------:|-----------------:|----------------:|--------------:|---------------:|----------------------------:|-----------------:|-----------------:|---------------------:|--------------------------:|------------:|------------:|------------:|---------------:|----------------:|
| count |     10000 |     10000           |  10000           | 10000           |         10000 | 9415           |                        9979 |            10000 |  10000           |      10000           |                     10000 |       10000 |       10000 |       10000 | 10000          | 10000           |
| mean  |      5000 |         5.2647e+06  |      5.47121e+06 |     8.64618e+06 |            75 |    9.75504e+12 |                        1981 |                4 |  54001           |      59687           |                      2919 |        1345 |        3110 |       11475 | 19965          | 23789           |
| std   |      2886 |         7.57546e+06 |      7.82733e+06 |     1.17511e+07 |           170 |    4.42862e+11 |                         152 |                0 | 157369           |     167803           |                      6124 |        6635 |        9717 |       28546 | 51447          | 79768           |
| min   |         1 |         1           |      1           |    87           |             1 |    1.9517e+08  |                       -1750 |                2 |   2716           |       5510           |                         3 |          11 |          30 |         323 |   750          |   754           |
| 25%   |      2500 |     46275           |  47911           |     1.00884e+06 |            23 |    9.78032e+12 |                        1990 |                3 |  13568           |      15438           |                       694 |         196 |         656 |        3112 |  5405          |  5334           |
| 50%   |      5000 |    394965           | 425123           |     2.71952e+06 |            40 |    9.78045e+12 |                        2004 |                4 |  21155           |      23832           |                      1402 |         391 |        1163 |        4894 |  8269          |  8836           |
| 75%   |      7500 |         9.38222e+06 |      9.63611e+06 |     1.45177e+07 |            67 |    9.78083e+12 |                        2011 |                4 |  41053           |      45915           |                      2744 |         885 |        2353 |        9287 | 16023          | 17304           |
| max   |     10000 |         3.32886e+07 |      3.55342e+07 |     5.63996e+07 |          3455 |    9.79001e+12 |                        2017 |                4 |      4.78065e+06 |          4.94236e+06 |                    155254 |      456191 |      436802 |      793319 |     1.4813e+06 |     3.01154e+06 |  
  
Let's move a little deeper and see what wonders the data is yet to reveal.
  
## Visualizing Data
Let's see how numerical columns correlate with each other  
  
![Figure](./goodreads/corr_hmap.png)

  
In the realm of the data universe, the correlation heatmap unveils intriguing connections among various aspects of books and their reception. 

As we delve into the matrix, we notice a strong bond between the **average_rating** and **work_ratings_count**, with a correlation of 0.92. This suggests that higher ratings typically attract more reviews, showcasing a dynamic relationship where popularity begets visibility.

Meanwhile, the **best_book_id** and **work_id** hold a moderate correlation of 0.37, hinting at a shared narrative of quality and audience recognition. It's as if the identifiers of these books collaborate to tell a story of literary excellence.

Curiously, the **original_publication_year** shows a weak negative correlation with the **average_rating** (-0.32), portraying a possible trend where older titles might receive less favorable ratings in the modern context, reflecting evolving reader preferences over time.

As we skim over the **ratings_1** to **ratings_5**, a tapestry of relationships unfolds. Notably, the counts of lower ratings (ratings_1 and ratings_2) exhibit a negative correlation with **average_rating**, while the higher ratings (ratings_4 and ratings_5) are positively correlated. This indicates that as a book garners more high ratings, its overall average rating ascends, further reinforcing the impact of reader sentiment.

Each square in this heatmap narrates a subplot of literary appreciation, shedding light on how audiences interact with books and how their experiences create a rich, interconnected web of literary discourse. In this vibrant landscape, ratings, publication history, and reader engagement converge to guide future readers on their next literary adventure. 

Now in the second figure we'll see numerical columns spread themselves.  
  
![Figure](./goodreads/histogram.png)

  
Once upon a time in the world of literature, a data explorer embarked on a journey through a vast collection of books. Armed with a dataset, they utilized histograms to uncover the hidden stories behind the numbers.

In the first row of histograms, they observed the **book_id**, a seemingly innocuous identifier that, curiously, had a large number of entries clustered close together in a narrow range. It hinted at the existence of few extremely popular books while the rest quietly awaited their moment in the spotlight. The **goodreads_book_id** followed suit, showing a similar pattern, suggesting that many books had been processed or evaluated.

Moving to the **best_book_id**, our explorer noticed a much more varied distribution, sparking intrigue. Here lay the celebrated titles—those that had captured the hearts of readers, demanding attention amongst their peers.

As they ventured deeper into the second row, the **books_count** and **isbn13** histograms presented a fascinating contrast. The former exhibited a heavily skewed distribution, indicating that a handful of books had amassed significant counts, while most had seen little action. The **isbn13** revealed a more balanced frequency, hinting at a blend of old favorites and new contenders vying for affection.

The **original_publication_year** histogram painted a timeline of literary history, showing perhaps when the literary world had thrived with creativity. The peaks highlighted eras rich in storytelling, while the valleys suggested quieter times where fewer books found their way into readers’ hands.

In the realm of ratings, the **average_rating** histogram stood out, resembling a majestic bell curve. It indicated that most books received favorable reviews from readers, but a few outliers—both adored and despised—spurred any enthusiast’s curiosity.

The following row highlighted the **ratings_count** and **work_ratings_count**—two metrics that revealed how actively readers engaged with these literary works. The skewed distributions indicated a few books received an abundance of attention, while many remained in the shadows.

Lastly, the **ratings_x** columns—ratings from 1 to 5—unfurled the emotions attached to these books. Most ratings clustered at each end of the spectrum, speaking to passionate readers who either loved or loathed their reads.

Thus, through the lens of histograms, our explorer pieced together the narrative of a vibrant literary ecosystem—filled with celebrated titles and hidden gems, all waiting for the next reader to turn their pages.

Lastly, we'll see some mischievous datapoints that don't follow the trend (Outliers!).  
  
![Figure](./goodreads/box_plot.png)

  
In a land of literary treasures, our box plots tell the stories hidden within the vast amounts of book data gathered from a bustling library. 

**First up: the Box Plot of `Book_id`**. Here, the central box, stretching between the first and third quartiles, showcases the heart of our book collection, with most of the stories residing within a healthy range. However, isolated whiskers suggest there are some outlier numbers—perhaps rare tomes waiting to be rediscovered.

**Next, we venture into `Goodreads_Goodreads_id`**, another journey into the realm of reader ratings. The box serves as a diary of average experiences, while the long whiskers hint at the polar experiences — both love and disdain for specific reads — likely leading to spirited debates among bibliophiles.

**The `Best_book_id` plot** reveals the champion books that have captured readers’ hearts. Its narrow spread shows a consensus among readers about what makes a book great, though outliers whisper of hidden gems that didn’t achieve mainstream success.

Transitioning to the realm of works, the **`Work_id` box plot** illustrates a rich tapestry of creativity, with substantial variety among works. A few outliers, again, stand tall like skyscrapers in a thriving city, reminding us of the standout pieces that disrupt the norm.

**In `Books_count`**, the plot reveals the wealth of volumes some authors possess. This box stretches wide, reflecting prolific writers alongside those with a single grand narrative, showcasing the diversity in literary output.

Finally, the **`isbn13` plot** paints a picture of organization within chaos. Here, we see data that smoothly conveys the identifier codes, but the scattered outliers remind us of the unique paths books can take in their journey through time.

Together, these box plots offer a glimpse into the narrative of the literary world—a landscape filled with varied journeys, celebrated works, and stories waiting for eager readers to explore. Each plot, with its highs and lows, emphasizes the rich diversity and complexity of literature.

