#

#pip install googlesearch-python

from googlesearch import search

# Define the query you want to search
query = "Python programming"

# Specify the number of search results you want to retrieve
num_results = 5

# Perform the search and retrieve the results
search_results = search(query, num_results=num_results, lang='en')

# Print the search results
for result in search_results:
    print(result)

