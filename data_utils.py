import pandas as pd
from wordcloud import WordCloud
from matplotlib import pyplot as plt
import os
import re
import pdb



DATA_PATH = os.getcwd()+'/Data/papers.csv'
DIR_PATH = os.getcwd()

def load_data(PATH=DATA_PATH):
    
    papers = pd.read_csv(PATH)
    
    return papers
    #pdb.set_trace()

    
def drop_meaningless(papers):
    
    meaningless_features = ['id', 'event_type', 'pdf_name']
    papers.drop(meaningless_features, axis=1, inplace=True)
    
    return papers



def text_cleaning(papers):
    
    papers['text_processed'] = papers['paper_text'].map(lambda x: re.sub('[,\.!?]', '', x))
    
    return papers


def EDA(papers):
    
    text = ','.join(list(papers['text_processed'].values))
    
    
    wordcloud = WordCloud(background_color="white", max_words=1000, contour_width=3, contour_color='steelblue')


    image = wordcloud.generate(text)
    
    image.to_file(DIR_PATH + 'Images/wordcloud.png')
    
    
