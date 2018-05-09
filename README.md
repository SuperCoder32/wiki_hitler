This is a simple proof that Hitler's Wikipedia article can or cannot be reached in 6 clicks through references(hyperlinks) from any Wikipedia aritcle.

Let an article be a node.
Let number of clicks be degrees.
Let all the articles that reference another be its neighbours.

Thus we have a graph and we can use a Graph traversal algorithm.

The algorithm that is best suited for the task is BFS(Breadth First Search).
It ensures that all pages at a certain degree from Hitler's page get iterated and their neighbours added before it goes to the next degree. Thus if the algorithm takes an article from the queue, which is degree 6 from Hitler and this articles has any unvisited neighbours then we can state that that Hitler's page cannot be reached in 6 clicks or less from any wiki article.

The source of the information is the Links Here section on Wikipedia under Namespace: (Article).
To extract it I used Wikimedia's API.

In this project you can see leftovers from my struggle to get to the point of a working solution that would take less than an year to execute. 

The final result is in:
link_extractor_final.py
proof_final.py

If you want to run the proof yourselves, you're welcome to. But beware that it might take a lot of time.
It is currently running on my computer and hasn't finished yet. One reason for that is that Wikimedia's API
doesn't allow large queries for users. For users the result limit is 500 and for bots it is 5000. I'm struggling to log my bot in(or to register it if I have to) and if you can offer any assistance please contact me(pietarcho@gmail.com) or make a pull request as this simple thing could make the proof run much faster. 

To get it running you only need a working Python installation and an internet connection.
If you're on Windows you can download it from the official Python website.
If you're on Linux Python usually comes preinstalled with the distribution.

After downloading the scripts you can open a shell(or CMD) and run the proof_final.py with a first argument the root article and a second argument wether to log additional information(verbose).

So on Windows:
cd directory_where_you_downloaded_scripts
python proof_final.py Adolf_Hitler -v

And on Linux:
cd directory_where_you_downloaded_scripts
python3 proof_final.py Adolf_Hitler -v

If you want to see the script finish you have to keep your computer from going into Sleep mode or Suspend or Hibernate.
To do this you can find a mouse jiggler program or script for your OS.
