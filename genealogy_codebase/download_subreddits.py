from datetime import datetime
from pmaw import PushshiftAPI
import json, pickle
from multiprocessing import Process, Manager
import timeit, random, bz2, lzma
import gzip, os


api = PushshiftAPI()

def crawl_subreddit(sub, directory, start_date, end_date, comments = False):
    #Example:  start_epoch: '20200101', end_epoch '20200303'
    
    print(start_date)
    print(end_date)
    
    start_epoch = int(datetime.strptime(start_date, '%Y%m%d').timestamp())
    end_epoch = int(datetime.strptime(end_date, '%Y%m%d').timestamp())
    
    
    # start_epoch = datetime.strptime(start_date, '%Y%m%d')
    # end_epoch = datetime.strptime(end_date, '%Y%m%d')
    
    prefix = "posts"
    if comments:
        prefix = 'comments'
        
    directory = "{}{}/{}/".format(directory, prefix, sub)
    
    if not os.path.exists(directory):
        os.makedirs(directory)
        
    if comments:
        # gen = api.search_comments(subreddit = sub)
        gen = api.search_comments(subreddit = sub, after = start_epoch, before = end_epoch)
    else:
        # gen = api.search_submissions(subreddit = sub)
        gen = api.search_submissions(subreddit = sub, after = start_epoch, before = end_epoch)
        
    
    for dic in gen:
        # dic = dic.d_
        created_time = datetime.fromtimestamp(float(dic['created_utc']))
        year = created_time.year
        month = created_time.month
        month_str = str(month)
        if len(month_str) < 2:
            month_str = "0{}".format(month_str)
            
            
            
        file_path = "{}{}_jsonlists.gz".format(directory, prefix)
        if not os.path.exists(file_path):
            open(file_path, 'w').close()

        with gzip.open(file_path, "at") as fout:
            fout.write("%s\n" % json.dumps(dic))

        # with gzip.open("{}{}_jsonlists.gz".format(directory, prefix), "at") as fout:
        #     fout.write("%s\n" % json.dumps(dic))
            
if __name__ == "__main__":
    # crawl_subreddit('nba', 'data/', '20070101', '20210209', comments = False)
    # crawl_subreddit('nba', 'data/', '20070101', '20210209', comments = True)
    subreddits_to_crawl = []
    
    for sub in subreddits_to_crawl:
        crawl_subreddit(sub, 'data/', '20230208', '20230408', comments = False)
        crawl_subreddit(sub, 'data/', '20230208', '20230408', comments = True)