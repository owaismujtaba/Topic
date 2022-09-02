import pdb
from data_utils import load_data, drop_meaningless
from data_utils import text_cleaning, EDA

def get_data():
    papers = load_data()
    papers = drop_meaningless(papers)
    papers = text_cleaning(papers)
    
    return papers


def generate_wordcloud():
    
    papers = get_data()
    papers = EDA(papers)
