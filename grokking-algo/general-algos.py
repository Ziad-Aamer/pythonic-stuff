"""
*Binary search tree:
    -insert an item to its right position in the tree to stay sorted.
    -for every node, the nodes on the left are smaller, and the nodes on the right are larger.
*Balanced binary search trees: red-black trees, AVL-trees.
*Trees: B-trees, Heaps, Splay trees

*Inverted index: a hash that maps words to places where they appear. (used in search engines)

*Fourier transform: given a smoothie, the Fourier transform will tell you the ingredients in the smoothie.

*Parallel Programming: 
    -Overhead of managing the parallelism (dividing, sending, and merging the data) 
    -Load balancing: each core get an equal work to evenly distribute the work

*MapReduce:
    -Distributed algorithm that can be used through Apache Hadoop.
    -Why we need it? To run algorithms on distributed machines, to speed up the time required to do it.
    -Map: takes an array and applies the same function to each item in the array e.g. doubling every item
        arr1 = [1, 2, 3, 4, 5]
        >>> arr2 = map(lambda x: 2 * x, arr1)
        [2, 4, 6, 8, 10]

    -Reduce: reduce a whole list of items down to one item e.g. summing array items e.g.
        >>> arr1 = [1, 2, 3, 4, 5]
        >>> reduce(lambda x,y: x+y, arr1)
        15

    -When you have a large dataset (billions
    of rows), MapReduce can give you an answer in minutes where a
    traditional database might take hours

*Bloom filters and HyperLogLog
    -If you have a lot of data and satisfied with approximate answers, check out probabilistic algorithms!
    -Bloom filters: probabilistic data structures that
        -give an answer that could be wrong but is probably correct
        -take up very little space, but doesn't give exact answer.
    -HyperLogLog: approximates the number of unique elements in a set
        -Only take a fraction of the memory
        -It won't give you the exact answer, but it comes very close.

SHA:
    -Secure hash algorithm that has many uses cases e.g. comparing 2 files, checking if passwords match, ...
    -It is a one-way (we can't retrive the original string from the hash) that's why we store the hash of the passwords.
    -SHA is a family of algorithms, most secure SHA-3. Standard is bcrypt
    -It's localy insensitive (avalanche effect: changing one character of the string will generate a completely new hash)

Simhash:
    -it is localy-sensitive, that's why it is used to detect duplicates or check for similar items.

Diffie-Hellman:
    -Algorithm used to ecrypt/decrypt messages exchanged between 2.
    -It has 2 keys [public and private]:
        *The public is used to encrypt, and the encrypted message can only be decrypted using the private key
    -RSA is its successor.

Liner programming:
    -is used to maximize something given some constraints.
    -Can solve all the graph algorithms !!
    -uses the Simplex algorithm

"""