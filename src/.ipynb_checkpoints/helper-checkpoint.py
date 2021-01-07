from html.parser import HTMLParser
from nltk.corpus import stopwords
from io import StringIO
import imblearn
import re

class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.text = StringIO()
    def handle_data(self, d):
        self.text.write(d)
    def get_data(self):
        return self.text.getvalue()

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

def preprocess(raw_text):
    stopwords_set = set(stopwords.words('english'))
    #Remove punctuations and stopwords
    cleaned = " ".join([i for i in re.sub(r'[^\w\s]', " ", raw_text).lower().split() if i not in stopwords_set])
    #Remove prefixed 'b'
    cleaned = re.sub(r'^b\s+', "", cleaned)
    #Remove retweet 'rt'
    cleaned = re.sub(r'^rt\s+', "", cleaned)
    # Remove single characters from the start
    cleaned = re.sub(r'\^[a-zA-Z]\s+', ' ', cleaned) 
    # Remove single characters
    cleaned = re.sub(r'\s+[a-zA-Z]\s+', ' ', cleaned)
    # Remove _ characters from the start
    cleaned = re.sub('\w*\_\w*', ' ', cleaned)
    #Remove URLs
    cleaned = re.sub(r'http\S+', "", cleaned) 
    # Remove words with containing numbers
    cleaned = re.sub('\w*\d\w*', '', cleaned)
    # Substituting multiple spaces with single space
    cleaned= re.sub(r'\s+', ' ', cleaned, flags=re.I)
    # Remove ome random letters

    return cleaned
