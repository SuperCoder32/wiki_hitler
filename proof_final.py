import sys
import os
import shelve
import argparse
from link_extractor_final import get_all_articles


def get_neighbours(title):
    return get_all_articles(title)


parent_of = dict()
toVisit = list()
visited = set()
steps = int()
proven = bool()
degree = 0

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


def save_data(root_article):
    with shelve.open(root_article + "-graph") as db:
        db["tree"] = parent_of
        db["toVisit"] = toVisit
        db["visited"] = visited
        db["steps"] = steps
        db["proven"] = proven
        db["degree"] = degree


def load_data(root_article):
    with shelve.open(root_article + "-graph") as db:
        return {
            "tree": db["tree"],
            "toVisit": db["toVisit"],
            "visited": db["visited"],
            "steps": db["steps"],
            "proven": db["proven"],
            "degree": db["degree"]
        }


def main(root_article, max_degree, verbose, save, load):
    global parent_of
    global toVisit, visited
    global proven, steps, degree

    if load and os.path.exists(root_article + "-graph.db"):
        data = load_data(root_article)

        parent_of = data["tree"]
        toVisit = data["toVisit"]
        visited = data["visited"]
        steps = data["steps"]
        proven = data["proven"]
        degree = data["degree"]

        del data
    else:
        parent_of = dict()

        toVisit = [root_article]
        parent_of[root_article] = None

        visited = set([root_article])
        proven = True
        steps = 0

    try:
        while len(toVisit) > 0:
            node = toVisit.pop(0) 

            if verbose:
                print("Added neighbours of", steps, "articles")
                print("A total of", len(visited), "articles are covered")
                print("There are", len(toVisit), "articles in queue")
                
            degree = backtrack(node)
            neighbours = get_neighbours(node)

            visited_len_before = len(visited)

            for link in neighbours:
                if link in visited:
                    continue

                toVisit.append(link)
                parent_of[link] = node
                visited.add(link)
            
            visited_len_after = len(visited)

            if degree == max_degree and visited_len_after - visited_len_before > 0:
                proven = False
                break
            
            steps += 1

    except KeyboardInterrupt as exc:
        print(exc)
        if save:
            print("Saving...")
            save_data(root_article)
            exit(0)
    else:
        if save:
            print("Saving...")
            save_data(root_article)


    success = "{num} wiki articles have at most degree {deg} to {ra}".format(ra=root_article, num=len(visited), deg=degree)
    failure = "There are wiki articles with a larger degree than {md} to {ra}".format(ra=root_article, md=max_degree)

    print(success if proven else failure)



def parse_args():
    parser = argparse.ArgumentParser(prog='proof_final', description='Find about the max degree to a wiki article.',
        usage='proof_final -ra arg1 -md arg2 [-v] [-s] [-l]')

    parser.add_argument('-ra', help='Root Article - where to start')
    parser.add_argument('-md', help='Maximum Degree - The maximum degree to the Root Article allowed(terminates after it exceeds it)')
    parser.add_argument('-v', help='Verbosity - whether to log extensive info about progress', dest='verbose', action='store_true')
    parser.add_argument('-s', help='Save - whether to save progress after termination', dest='save', action='store_true')
    parser.add_argument('-l', help='Load - whether to load progress on specified Root Article', dest='load', action='store_true')

    args = parser.parse_args()

    if args.ra is None or args.md is None:
        parser.print_help()
        exit(0)

    return args.ra, args.md, args.verbose, args.save, args.load


if __name__ == "__main__":    
    args = parse_args()
    print(args)
    main(*args)
