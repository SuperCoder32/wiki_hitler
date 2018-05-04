This is a simple proof that Hitler's wikipedia page can or cannot be reached in 6 clicks on references to other wiki aritcles from any wiki article.
The only problem is it would take years to complete.
In the future I'll somehow parse Wikipedia and make a dictionary or a database to contain all the articles a certain article was referenced from,
which should speed up the process 10000-fold.

The algorithm used is BFS. It ensures that all pages at a certain "distance" from Hitler's page get iterated and their "neighbours" added before it goes to the "next distance"(prevdist + 1)
