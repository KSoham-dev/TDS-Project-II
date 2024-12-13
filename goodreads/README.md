
# Data Analysis Project 
Hey! Hope you are doing fine. Hmm... You've got some interesting data I see.  
Let's begin this journey with first identifying what your data is like.  
So, you have got 10000 rows and 23 columns in your data and as I can  
see this data is related to Books. Below are some key statistics  
about the data you provided  

## Key Statistics
|       |   book_id |   goodreads_book_id |     best_book_id |         work_id |   books_count |          isbn13 |   original_publication_year |   average_rating |    ratings_count |   work_ratings_count |   work_text_reviews_count |   ratings_1 |   ratings_2 |   ratings_3 |      ratings_4 |       ratings_5 |
|:------|----------:|--------------------:|-----------------:|----------------:|--------------:|----------------:|----------------------------:|-----------------:|-----------------:|---------------------:|--------------------------:|------------:|------------:|------------:|---------------:|----------------:|
| count |     10000 |     10000           |  10000           | 10000           |         10000 | 10000           |                       10000 |            10000 |  10000           |      10000           |                     10000 |       10000 |       10000 |       10000 | 10000          | 10000           |
| mean  |      5000 |         5.2647e+06  |      5.47121e+06 |     8.64618e+06 |            75 |     9.75504e+12 |                        1981 |                4 |  54001           |      59687           |                      2919 |        1345 |        3110 |       11475 | 19965          | 23789           |
| std   |      2886 |         7.57546e+06 |      7.82733e+06 |     1.17511e+07 |           170 |     4.29712e+11 |                         152 |                0 | 157369           |     167803           |                      6124 |        6635 |        9717 |       28546 | 51447          | 79768           |
| min   |         1 |         1           |      1           |    87           |             1 |     1.9517e+08  |                       -1750 |                2 |   2716           |       5510           |                         3 |          11 |          30 |         323 |   750          |   754           |
| 25%   |      2500 |     46275           |  47911           |     1.00884e+06 |            23 |     9.78031e+12 |                        1990 |                3 |  13568           |      15438           |                       694 |         196 |         656 |        3112 |  5405          |  5334           |
| 50%   |      5000 |    394965           | 425123           |     2.71952e+06 |            40 |     9.78045e+12 |                        2004 |                4 |  21155           |      23832           |                      1402 |         391 |        1163 |        4894 |  8269          |  8836           |
| 75%   |      7500 |         9.38222e+06 |      9.63611e+06 |     1.45177e+07 |            67 |     9.78081e+12 |                        2011 |                4 |  41053           |      45915           |                      2744 |         885 |        2353 |        9287 | 16023          | 17304           |
| max   |     10000 |         3.32886e+07 |      3.55342e+07 |     5.63996e+07 |          3455 |     9.79001e+12 |                        2017 |                4 |      4.78065e+06 |          4.94236e+06 |                    155254 |      456191 |      436802 |      793319 |     1.4813e+06 |     3.01154e+06 |  
  
Let's move a little deeper and see what wonders the data is yet to reveal.
  
## Visualizing Data
Let's see how numerical columns correlate with each other  
  
![Figure](./corr_hmap.png)

  
Once upon a time in the realm of literature, a wise librarian decided to explore the relationships between various numerical features of books to uncover hidden stories within the data. To do this, she turned to a correlation heatmap, a colorful tapestry that depicted how each feature connected with the others.

As she studied the heatmap, the librarian noticed a strong bond between the "average_rating" and the "ratings_count." This deep crimson connection suggested that books with high average ratings often enjoyed a large number of ratings, hinting at their popularity and quality. Readers were drawn to these well-rated books like moths to a flame.

Further down the map, a gentle blue hue emerged between "original_publication_year" and "work_text_reviews_count." This cooler relationship indicated that older books tended to garner fewer reviews, perhaps due to changing tastes and the passage of time. It was a reminder that while classics might still hold value, they often lack the vibrant discussions of newer releases.

The librarian also spotted a curious relationship between "goodreads_book_id" and "best_book_id." Though they shared a moderate positive correlation, it was clear they were distinct entities, each representing a facet of the book's identity in the vast Goodreads universe. This intrigued her, making her wonder about the nuances of what it meant to be a “best book.”

As she examined the various correlations further, the librarian found that certain ratings and review metrics danced closely together, showcasing how engagement in the Goodreads community reflected readers' experiences. The heatmap told a fascinating story of interconnectedness, revealing that in the world of books, every number had its narrative—each rating, review, and publication year echoing the whispers of readers past and present.

In this data-driven tale, the librarian realized that understanding these relationships could help her curate better recommendations, ensuring that each book found its perfect audience in the grand library of human experience. And so, she continued her journey through the data, eager to uncover more stories waiting to be told. 

Now in the second figure we'll see numerical columns spread themselves.  
  
![Figure](./histogram.png)

  
In the realm of data, our journey begins with a visual tale told through a tapestry of histograms. Each subplot captures a distinct story woven from the numerical threads of our dataset.

Starting with **book_id**, we notice a clustering at the lower end, suggesting that most books in our collection are relatively new to the scene, while a few trail off into the depths of obscurity.

Next, the histogram for **goodreads_book_id** paints a similar picture, revealing that there are plentiful entries but also some unique outliers, each representing cherished titles that have made a significant mark on readers’ hearts.

As we turn to **ratings_count** and **average_rating**, a more engaging narrative unfolds. The **average_rating** histogram glimmers with peaks, indicating that readers often gravitate toward favorite books, whether they aim for exceptional or below-average experiences. Books that resonate widely with audiences are clearly reflected, seen in the distinct alignment of ratings toward the higher end.

In the realm of **work_ratings_count** and **ratings_1** through **ratings_5**, we observe a balanced distribution. The scale narrates tales of numerous opinions—both critiques and praises—creating a complex mosaic of reader experiences that bring characters and stories to life in diverse ways. Higher ratings are abundant, showcasing a strong preference among readers for certain works that may offer rich narratives or engaging plots.

Lastly, the **original_publication_year** and **isbn13** histograms stand as a testament to the evolution of literature. They hint at the blossoming of modern storytelling while reflecting a decline in the prevalence of older titles, perhaps an indication of shifting literary trends and preferences as new voices emerge.

Together, these histograms encapsulate a vibrant world of literature. They invite us to explore, discover, and engage with books that resonate across generations—each histogram a chapter in the unfolding story of our dataset.

Lastly, we'll see some mischievous datapoints that don't follow the trend (Outliers!).  
  
![Figure](./box_plot.png)

  
In the bustling world of literature and readers' interactions, our box plots present a fascinating narrative about the dynamics among various book-related variables. 

Starting with the **Goodreads Book ID**, the box plot reveals a wide range of values, indicating a rich diversity in book IDs; however, it's the presence of several outliers that suggests a few books might have garnered extraordinary attention or a unique classification within the platform. This indicates not just popularity but perhaps interesting anomalies in user ratings or reviews.

Next, we glance at the **Best Book ID** plot, which mirrors the diversity seen in the Goodreads data but with different intensity. Not only does it show a similar spread, but the outliers here tell the story of certain books being recognized as the best among many, suggesting they are landmarks in readers’ experiences.

Diving into the **Work ID**, the box plot narrates a more compact story. The interquartile range here is tighter, hinting that most works share similarities in their identifiers, signifying a more uniform cataloging of literature, possibly pointing to a well-structured classification system in libraries or databases.

The **Books Count** box plot reveals a wide spread, with a high median. This suggests that while many books are published in certain ranges, there are remarkable standouts, with some titles receiving an overwhelming number of counts. This likely reflects varying reader engagement levels, where a few books are read widely, creating a large disparity compared to others.

Lastly, the **ISBN13** plot provides an eye-catching conclusion. This box plot shows the widest range of values, indicating a vast selection of books identifiable by their ISBN numbers. The outliers here signify landmark publications that perhaps achieve fame well beyond their immediate category or genre, making them memorable pillars in the realm of literature.

Together, these box plots weave a complex tale of the literary landscape, showcasing the interplay of popularity, diversity, and engagement in readers’ journeys through the world of books.

