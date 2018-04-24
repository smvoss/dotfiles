import os
import fnmatch
import glob2 as glob


def filter_files(file, filter_arr):
    for ex in filter_arr:
        if fnmatch.fnmatch(file, ex):
            return False
    return True


def validating_user_input(question, options=['y', 'n', 'a']):
    valid_option_chosen = False

    while not valid_option_chosen:
        user_input = input("{question} [{opts}]:".format(
            question=question, opts="/".join(options)
        ))

        if user_input in options:
            valid_option_chosen = True

    return user_input


def load_dotfiles(filter_arr):
    files = [x for x in glob.iglob("**", recursive=True)
             if os.path.isfile(x) and filter_files(x, filter_arr)]
    return files
