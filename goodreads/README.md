
# Data Analysis Project 
Hey! Hope you are doing fine. Hmm... You've got some interesting data I see.  
Let's begin this journey with fist identifying what your data is like.  
So, you have got 100 rows and 500 columns in your data and as I can  
see this data is related to Books. Below are some key statistics  
about the data you provided  

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
  
![Figure](./corr_hmap.png)

  
Imagine you’re a wise librarian in a vibrant library filled with countless stories, each represented by colorful books. You have a special tool— a correlation heatmap— that reveals hidden connections between these books and their readers. 

As you gaze at the heatmap, you notice strong bonds forming between certain features. For instance, the **average rating** appears to be a glowing beacon of importance, closely linked with **ratings count** and **work ratings count**. This suggests that not only do readers express their love through ratings, but those with more ratings tend to shine brighter in their overall appeal.

Interestingly, the **original publication year** shows a moderate connection with **average rating**. This points to a possible trend: older books have timeless qualities that resonate with readers, maintaining a steady popularity despite the passage of time. 

However, not all relationships are harmonious. The **best book id** ends up on a lonely island, with weak correlations to other features, hinting that being labeled as the “best” may not always translate to wider acclaim among readers.

As you explore deeper, you find surprising twists— the connections between **work ratings count** and various *ratings categories*. The first ratings have stronger ties, revealing a dynamic where initial impressions often shape the book's reputation. 

In summary, this heatmap is like a treasure map, guiding you through the intricate web of book popularity and reader engagement, uncovering stories about timeless classics, the impact of initial ratings, and the often overwhelming quest for the “best” in literature. Each shade tells a tale of connection, illustrating not just numbers, but the rich narrative of readers' experiences. 

Now in the second figure we'll see numerical columns spread themselves.  
  
![Figure](./histogram.png)

  
In a quiet library filled with countless stories, a collection of data sits patiently, eager to share its secrets. The histograms, each a chapter in this tale, reveal the hidden patterns and narratives woven throughout the dataset.

As we embark on our journey, the first subplot introduces us to the mysterious “book_id,” largely uniform across the x-axis, suggesting a well-organized collection where each story finds its rightful place. Next, “goodreads_book_id” appears almost like a whisper, with few entries, hinting at a lesser-known selection that remains untouched by many readers.

Our exploration continues with the “best_book_id,” illuminating the favorites among readers. A peak here signals a handful of titles that have captured hearts, suggesting a few standout stories in a sea of options. The “work_id” histogram, dense and sprawling, tells us of a diverse array of works, each with its own tale waiting to unfold.

In the heart of our journey, we encounter “average_rating,” a friendly mountain rising gracefully to the occasion. This reveals the collective appreciation of books—a significant number of titles swaying between moderate and high ratings, revealing both critic acclaim and reader affection.

As we meander deeper, the “isbn13” and “ratings_count” histograms emerge with more complexity, suggesting a wealth of books that are both recognized and rated by enthusiastic readers. The patterns signify a passionate community discussing and critiquing their favorite reads.

“Original_publication_year” reflects a timeline, unraveling the history of storytelling, where older classics find themselves mingling with contemporary favorites, reinforcing the timeless nature of good literature. Meanwhile, the ratings from one to five offer another layer, revealing that while many readers have high praise, some titles have stiffer critics, illustrating the duality of taste in literature.

Finally, “work_text_reviews” stands before us like a treasure chest, overflowing with insights and opinions, urging readers to dive in and explore the collective voices of the community. 

In sum, this visual journey through histograms not only showcases the structure of a literary dataset but also tells a rich story of reader preference, engagement, and the evolving landscape of books cherished over time. Each histogram, a window into the vibrant world of reading, invites us to explore further, to read between the lines, and to discover the narratives waiting to be told.

Lastly, we'll see some mischievous datapoints that don't follow the trend (Outliers!).  
  
![Figure](./box_plot.png)

  
Once upon a time in the land of data, a wise analyst sought to understand the stories told by various box plots representing books and their attributes. Each plot served as a window into the characteristics of a different aspect of these literary treasures.

**The Books Plot** revealed an intriguing range, showcasing that most books had a page count clustering between 2,000 and 7,500 pages. Yet, lurking in the shadows were a handful of outliers, suggesting some epic tales stretched far beyond the norm.

Next, **Goodreads and Best Book ID** provided insights into user engagement. The plots illustrated that while most books received moderate attention, a select few captured the hearts of readers, indicated by noticeable peaks. These outliers shone like stars, drawing readers into their unique narratives.

In the **Work ID** plot, it became evident that the diversity of works published was vast, yet most id numbers were closely packed, indicating that many works had similar publication details. The few outliers hinted at rare and extraordinary creations, worthy of curiosity.

**Books Count** showed the total number of titles under various work categories. Here, the middle range suggested a healthy variety, while a few prominent outliers stood tall, signifying a select few authors who had produced numerous works, perhaps turning them into literary empires.

Finally, the **ISBN13** plot revealed the backbone of book identification. Most ISBNs were useful and commonly clustered around a range, but again some stood apart, hinting at unique publications that deviated from standard patterns.

As the analyst pieced together these tales from the plots, it became clear: within these numbers lay the stories of creativity, passion, and the enduring love for books that transcend typical limits, reminding us all of the vast and diverse world of literature. And so, the analysis came to life, a tale of numbers transformed into a narrative of literary exploration.

