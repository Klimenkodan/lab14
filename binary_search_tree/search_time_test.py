from linkedbst import LinkedBST
from time import time
from random import choice
FILE_NAME = 'words.txt'
RANGE = 10000


def preparation(file_name):
    """
    This function makes the list of the words
    :param file_name:
    :return:
    """
    file = open(file_name, 'r')
    lst_words = file.readlines()
    return lst_words


def random_word(lst_words):
    """
    This function generates random words from dictionary
    :param lst_words:
    :return:
    """
    random_words = []
    while len(random_words) != 10000:
        random_words.append(choice(lst_words))
    return random_words


def lst_search(random_words, words_lst):
    """
    This function determines how much time is needed to find some number random words using list
    :param random_words:
    :param words_lst:
    :return:
    """
    new_time = time()
    i = 0
    for item in random_words:
        if item in words_lst:
            i += 1
    return time() - new_time


def binary_outorder(random_words, words_lst):
    """
    This function determines how much time is needed to find some number random words using binary tree
    :param random_words:
    :param words_lst:
    :return:
    """
    binar = LinkedBST()
    for item in words_lst:
        binar.add(item)
    new_time = time()
    i = 0
    for item in random_words:
        if binar.find(item) is not None:
            i += 1
    return time() - new_time


def binary_balanced(random_words, words_lst):
    """
    This function determines how much time is needed to find some number random words using balanced binary tree
    :param random_words:
    :param words_lst:
    :return:
    """
    binar = LinkedBST()
    for item in words_lst:
        binar.add(item)
    binar.rebalance()
    new_time = time()
    i = 0
    for item in random_words:
        if binar.find(item) is not None:
            i += 1
    return time() - new_time


if __name__ == "__main__":
    new_lst = preparation(FILE_NAME)
    words_ls = random_word(new_lst)
    noorder_lst = list(set(new_lst))
    print(lst_search(words_ls, new_lst))
    print(binary_outorder(words_ls, noorder_lst))
    print(binary_balanced(words_ls, noorder_lst))



