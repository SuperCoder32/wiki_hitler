This is a program intended to find out whether Hitler's Wikipedia article(or any specific Wikipedia artice for that matter) can or cannot be reached in x clicks through hyperlinks from any Wikipedia aritcle.

Let an article be a node.
Let number of clicks be degrees.
Let all the articles that reference another be its neighbours.

Thus we have a graph and we can use a Graph traversal algorithm.

The algorithm that is best suited for the task is BFS(Breadth First Search).
It ensures that all pages at a certain degree from Hitler's page get iterated and their neighbours added before it goes to the next degree. Thus if the algorithm takes an article from the queue, which is degree x from Hitler and this articles has any unvisited neighbours then we can state that that Hitler's page cannot be reached in x clicks or less from any wiki article.

The source of the information is the "Links Here" section on Wikipedia under Namespace: (Article).
To extract it I used Wikimedia's API.

In this project you can see another slower version of the  

The final result is in:
link_extractor_final.py
proof_final.py

If you want to run the program yourselves, you're welcome to. But beware that it might take a lot of time to finish.
You can Ctrl-C during the execution of the program and it will save its state and when you run it again on the same root article and specify the "load" argument it will continue executing from where it left off.

It might take a couple weeks to execute on an article that has a lot of hyperlinks pointing to it such as Hitler. One reason for that is that Wikimedia's API doesn't allow large queries for Wikimedia users. For users the limit of listed articles in the response they get is 500 and for bots it is 5000. I'm struggling to register my bot, so that it is recognised as a bot rather than a user while making requests. If you can offer any assistance please contact me(pgpetrov2001@gmail.com) or make a pull request as this simple change will make the program run much faster. 

To get it running you only need a working Python installation and an internet connection.

After downloading the scripts you can open a shell(or CMD) and run proof_final.py with the proper argument format.
You can run: python3 proof_final.py --help, to see what it is.

If you want to see the script finish you have to keep your computer from going into Sleep mode or Suspend or Hibernate.
To do this you can find a mouse jiggler program or script for your OS.
