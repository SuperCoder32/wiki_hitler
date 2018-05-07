This is a simple proof that Hitler's wikipedia page can or cannot be reached in 5 clicks on references to other wiki aritcles from any wiki article.
The only problem is it would take years to complete.

  The thing I'm working on currently is to speed up this process a whole lot by using wikimedia queries with a registered bot. But this errand brings on its own set of problems.

The algorithm used is BFS. It ensures that all pages at a certain "distance" from Hitler's page get iterated and their "neighbours" added before it goes to the "next distance"(prevdist + 1)
