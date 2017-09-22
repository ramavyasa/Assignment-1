# Assignment-1
There are 5 mappers and 5 reducers.(for MapReduce implementation)

1. mapper.py, reducer.py : These files are to be run first. They will do the word counting / training.
2. mapper_counter.py, reducer_counter.py : These files count the number of occurrences of each class and the number of words in them. Number of mappers should always be 1. Output of this should be stored locally with name "classes.txt".
3. mapper_test_counter.py, reducer_test_counter.py : These files create requirement set for test set. Number of mappers should always be 1.
4. mapper_final.py, reducer_final.py : These files merge the trained model and to be tested model. Number of reducers should always be 1.
5. NB_mapper.py, NB_reducer.py : These files implement the Naive Bayes algorithm. Number of reducers should always be 1. NB_mapper1 implements 1st algorithm and NB_mapper2 implements 2nd algorithm.

test1.py : Local Naive Bayes implementation of algorithm 1. test2.py : Local Naive Bayes implementation of algorithm 2.
