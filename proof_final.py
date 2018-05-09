import sys
from link_extractor_final import get_all_articles


def get_neighbours(title):
    return get_all_articles(title)


parent_of = dict()

def backtrack(node):
    degree = 0
    
    while node is not None:
        print(node, end='')
        node = parent_of[node]

        if node is not None:
            print('->', end='')
            degree += 1

    print('\n')
    return degree


def main(root_article, verbose):
    global parent_of
    parent_of = dict()

    toVisit = [root_article]
    parent_of[root_article] = None

    visited = set()
    proven = True
    steps = 0

    while len(toVisit) > 0 and proven:
        node = toVisit.pop() 

        if verbose:
            print("Added neighbours of", steps, "articles", end='; ')
            print("A total of", len(visited), "articles are visited", end='; ')
            print("There are", len(toVisit), "articles to add their neighbours in queue")
            
        degree = backtrack(node)
        neighbours = get_neighbours(node)

        if degree == 6 - 1 and len(neighbours) > 0:
            proven = False
            break

        for link in neighbours:
            if link in visited:
                continue

            toVisit.insert(0, link)
            parent_of[link] = node
            visited.add(link)
        
        steps += 1


    success = "{} is reachable in {} clicks from any wiki article".format(root_article, degree)
    failure = "{} cannot be reached in 6 clicks or less from any wiki article".format(root_article)

    print(success if proven else failure)


if __name__ == "__main__":
        root_article = sys.argv[1]

        try:
            verbose = sys.argv[2] == '-v'
        except IndexError:
            verbose = False            

        main(root_article, verbose)
