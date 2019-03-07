import pandas as pd
import numpy as np

article_read = pd.read_csv('pandas_tutorial_read.csv', delimiter=';', names = ['my_datetime','event','country','user_id','source','topic'])

article_read.head()

# Get the series
article_read['user_id']

# Filtering
article_read[article_read.source == 'SEO']

# you get the point....
