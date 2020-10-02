# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    list_paths = {}
    result = []

    # we first want to iterate over all the paths to determine all the files to search against
    for path in files:
        # since we know that the file will be the last thing on the path, we'll split up the path at every / and just store the final result of that as our path end.
        p_end = path.split('/')[-1]
        # now we can check if that file name is in our dictionary yet
        # if it is, we'll add the new path to the end of the list at that index, if it's not we'll create a new slot.
        if p_end in  list_paths:
            list_paths[p_end].append(path)
        else:
            list_paths[p_end] = [path]

    # now that all paths are accounted for we can check our queries against our dict and return any results that we find at each index
    for q in queries:
        # if we find the query in our dict
        if q in list_paths:
            # then for each path at that index, append it on to our results
            for path in list_paths[q]:
                result.append(path)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
