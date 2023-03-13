#########################################################################
# Assignment 2 Question 4                                               *
#                                                                       #
# Implement the algorithm Randomized-Quicksort discussed in class       #
# and the variant of Randomized-Quicksort given in Question 3 by        #
# the same programming language (any language is OK) on the same        #
# computing platform. Report the running times of the two algorithms    #
# for sorting n numbers with n = 2^i × 1000, i = 0, 1, 2, 3, 4, 5.      #
#                                                                       #
# Give your suggestion on selecting k in practice (e.g., the k          #
# achieves the best running time in your implementation).               #
#                                                                       #
# You may not need to submit your program codes.                        #
#########################################################################

from QuickSort import quicksort, quicksort_hybrid, insertion_sort
import random
from timeit import default_timer as timer

def main():
    # Create arrays of random integer elements of size n = 2^i x 1000, i = 0, 1, 2, 3, 4, 5
    i = 5
    n = pow(2, i) * 1000
    elements = random.sample(range(0, n), n)
    elements2 = elements.copy()

    # Using randomized_quicksort WITHOUT insertion sort modfiication
    start = timer()
    quicksort(elements, 0, len(elements)-1 )
    end = timer()
    print ("Quicksort, " + str(n) + " elements. Time elapsed: " + str(end - start))

    # Using randomized_quicksort WITH insertion sort modfiication
    start = timer()
    quicksort_hybrid(elements2, 0, len(elements2)-1 )
    end = timer()
    print ("Quicksort hybrid, " + str(n) + " elements. K = 50. Time elapsed: " + str(end - start))



    # Using randomized quicksort with insertion sort on subarrays of < k elements

if __name__ == '__main__':
    main()
