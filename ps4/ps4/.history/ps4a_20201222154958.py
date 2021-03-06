# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    if len(sequence)==1:
        return [sequence]
    else:
        perm = []
        for each in get_permutations(sequence[1:]):
            for i in range(len(each)+1):
                perm.append(each[:i]+sequence[0]+each[i:])

        perm.sort()
        return list(set(perm))

if __name__ == '__main__':
    #EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    # Example test case 2
    example_input = 'ab'
    print('Input:', example_input)
    print('Expected Output:', ['ab', 'ba'])
    print('Output:', get_permutations(example_input))

    # Example test case 3
    example_input = 'abb'
    print('Input:', example_input)
    print('Expected Output:', ['abb', 'bab', 'bba'])
    print('Output:', get_permutations(example_input))

    # Example test case 4
    example_input = 'aaa'
    print('Input:', example_input)
    print('Expected Output:', ['aaa'])
    print('Output:', get_permutations(example_input))

    # Example test case 5
    example_input = 'ravi'
    print('Input:', example_input)
    print('Output:', get_permutations(example_input))
    print(len(get_permutations(example_input)))

