import pdb
from data_utils import load_data, drop_meaningless
from data_utils import text_cleaning, EDA


def generate_wordcloud():
    papers = load_data()
    papers = drop_meaningless(papers)
    papers = text_cleaning(papers)
    papers = EDA(papers)