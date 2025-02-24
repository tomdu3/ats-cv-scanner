import docx2txt
import string

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

resume = docx2txt.process('./data/Tomislav Dukez - CV - Nov 2024.docx')
# change path to your cv file
print(resume)

# open file './data/job-descr.txt' -> change this with the right path/file name
# I used txt for simplicity,but it can be done in the same manner as for the cv
with open('./data/job-descr.txt', 'r') as f:
    job_descr = f.read()

print(job_descr)
data = [resume, job_descr]

# transform text into vectors
cv = CountVectorizer()
count_matrix = cv.fit_transform(data)

match = cosine_similarity(count_matrix)[0][1]
match = round(match*100)

# Keywords identifications and comparison
# import string, and stop words in english

english_stop_words = set(ENGLISH_STOP_WORDS)
# add to the list some words that are not stop words but are not important
# for resume matching
english_stop_words.add("experience")
english_stop_words.add("work")
english_stop_words.add("skills")
english_stop_words.add("skill")
english_stop_words.add("requirements")


def preprocess_text(text):
    """
    Convert text to lowercase, remove punctuation,
    and filter out common English stop words.
    """
    # convert to lowercase
    text = text.lower()
    # remove punctuation using str.translate
    text = text.translate(str.maketrans('', '', string.punctuation))
    # split text into tokens/words
    tokens = text.split()
    # filter stop words
    tokens = [word for word in tokens if word not in english_stop_words]
    return tokens


# Preprocess job description and resume texts
job_tokens = preprocess_text(job_descr)
resume_tokens = preprocess_text(resume)

# Convert job description tokens into a set of unique keywords
job_keywords = set(job_tokens)

# Prepare lists to store matched and unmatched keywords
matched_keywords = []
unmatched_keywords = []

for keyword in job_keywords:
    if keyword in resume_tokens:
        matched_keywords.append(keyword)
    else:
        unmatched_keywords.append(keyword)


def print_list(title, list):
    # print list elements in a table separated by |
    print()
    print(title.center(25, "*"))
    for element in list:
        print(element, end=" | ")
    print()

print('-'*45)
print("Keywords matching".center(45))
print_list("Matched keywords:", matched_keywords)
print_list("Unmatched keywords:", unmatched_keywords)
print()
print(f"Match percentage: {match}%")
print()
