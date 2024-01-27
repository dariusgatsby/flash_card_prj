import pandas as pd
import re

data = pd.read_csv('Untitled spreadsheet - Sheet1.csv')
words = data.Spanish.to_string(header=False,
                               index=False,
                               ).split('\n')


def remove_numbers(input_string):
    return re.sub(r'\d+', ' ', input_string)


fixed_words = [remove_numbers(i).strip() for i in words]

# print(fixed_words)

fixed_words = pd.DataFrame(fixed_words).to_csv("Spanish_words.csv", index=False, header='Spanish')