# name_args — Accepts any number of named arguments
# and prints them in the pattern key : value one at a time.

def name_args(**kwargs):
    for k in kwargs.keys():
        print(f"{k}:{kwargs[k]}")

name_args(course="Python", enjoyment_level="high", difficulty="very")