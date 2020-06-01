import glassdoor_scraper as gs
import pandas as pd 
path = "/usr/local/share/chromedriver"
df = gs.get_jobs('India','data scientist',5, False, path, 15)
df.to_csv('glassdoor_jobs.csv', index = False)

