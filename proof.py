import sys
from link_extractor import Parser


def get_neighbours(title):
	parser = Parser(title)
	return parser.get_all_articles()


def main(root_article):

	toVisit = [(root_article, 0)]
	visited = set()
	proven = True

	while len(toVisit) > 0:

		label, depth = toVisit.pop()

		print(label, depth)

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



	success = "{} is reachable in {} clicks from any wiki article".format(root_article, depth)
	failure = "{} cannot be reached in 5 clicks or less from any wiki article".format(root_article)

	print(success if proven else failure)


if __name__ == "__main__":
	main(sys.argv[1])