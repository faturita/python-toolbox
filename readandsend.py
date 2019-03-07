import pandas as pd
import numpy as np

import smtplib, ssl

article_read = pd.read_csv('https://docs.google.com/spreadsheets/d/1SCfZhq5OMcnhyWwhijPL2XaetzPXxBHY9VAT67tfhRs/export?format=csv&id=1SCfZhq5OMcnhyWwhijPL2XaetzPXxBHY9VAT67tfhRs', delimiter=',')

password = ''

server = smtplib.SMTP("smtp.office365.com", 587)
server.starttls()
server.login("rramele@baufest.com", password)


message = """\
Subject: Problema

Problema con los banios."""

server.sendmail("rramele@baufest.com","helpdeskbf@baufest.com",message)
