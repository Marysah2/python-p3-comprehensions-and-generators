def return_evens(num_list):
    """
    Returns a list of even numbers from num_list.
    If there are no even numbers, returns an empty list.
    """
    return [num for num in num_list if num % 2 == 0]


def make_exclamation(sentence_list):
    """
    Takes a list of sentences and returns a new list
    where each sentence ends with an exclamation mark.
    If the input list is empty, returns an empty list.
    """
    return [sentence + "!" for sentence in sentence_list]