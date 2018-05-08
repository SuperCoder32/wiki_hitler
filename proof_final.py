import sys
from link_extractor_final import get_all_articles


def get_neighbours(title):
	return get_all_articles(title)


def main(root_article):

	toVisit = [(root_article, 0)]
	visited = set()
	proven = True
        steps = 0

	while len(toVisit) > 0:

		label, depth = toVisit.pop()

		print(steps, len(visited), label, depth)

		neighbours = get_neighbours(label)

		if depth > 5:
			proven = False
			break

		for link in neighbours:
			if link in visited:
				continue

			newNode = (link, depth + 1)
			toVisit.insert(0, newNode)
			visited.add(link)
                
                steps += 1


	success = "{} is reachable in {} clicks from any wiki article".format(root_article, depth)
	failure = "{} cannot be reached in 5 clicks or less from any wiki article".format(root_article)

	print(success if proven else failure)


if __name__ == "__main__":
	main(sys.argv[1])
