import download_subreddits
import logging
import build_user_subreddit_history
import build_genealogy_graph
import pickle

logging.basicConfig(level=logging.INFO)

def main(subs, directory, start_date, end_date, num_founders = 50, edge_threshold = 0.1, 
                        days_diff = 7, is_comments = False, interval = 0):
    
    print(start_date)
    print(end_date)
  
    logging.info("downloading Reddit data from Pushshift")
    for sub in subs:
        download_subreddits.crawl_subreddit(sub, directory, start_date, end_date, comments = is_comments)
    
    logging.info("building user subreddit history")
    author_sub_timestamps_dic, sub_author_timestamps_dic, sub_founders_dic = \
            build_user_subreddit_history.build_user_subreddit_history(subs, 
                    founders = num_founders, comments = is_comments, interval = interval)
    
    # filenames are stored so that redrawing graphs (by changing edge threshhold) becomes easy
    # for full three-month data, use filename
    # for one-month data, use filename_1, filename_2 or filename_3
    
    
    if interval > 0:
        filename = f"filename_{interval}"
    else:
        filename = "filename"

    logging.info("building genealogy graph")
    build_genealogy_graph.get_parent_subs(sub_founders_dic, author_sub_timestamps_dic, directory=directory, days_diff=days_diff, filename=filename)

    logging.info("drawing genealogy graph")
    build_genealogy_graph.draw_graph(f"{directory}{filename}.csv", f"output_{interval}.png", threshold=edge_threshold)

    
    
#     if interval > 0:
#         filename = f"filename_{interval}"
#     else:
#         filename = "filename"

#     logging.info("building genealogy graph")
#     filename_df = build_genealogy_graph.get_parent_subs(sub_founders_dic, author_sub_timestamps_dic, directory=directory, days_diff=days_diff)

#     filename_df.to_csv(f"{filename}.csv", index=False)

#     logging.info("drawing genealogy graph")
#     build_genealogy_graph.draw_graph(f"{filename}.csv", f"output_{interval}.png", threshold = edge_threshold)

    
    
#     if interval > 0:
#         filename = f"filename_{interval}"
#     else:
#         filename = "filename"

#     logging.info("building genealogy graph")
#     filename_pkl = build_genealogy_graph.get_parent_subs(sub_founders_dic, author_sub_timestamps_dic, directory=directory, days_diff=days_diff)

#     with open(f"{filename}.pkl", "wb") as f:
#         pickle.dump(filename_pkl, f)

#     logging.info("drawing genealogy graph")
#     build_genealogy_graph.draw_graph(f"{filename}.pkl", f"output_{interval}.png", threshold = edge_threshold)

#     logging.info("building genealogy graph")
#     filename = build_genealogy_graph.get_parent_subs(sub_founders_dic, 
#                         author_sub_timestamps_dic, directory = directory, days_diff = days_diff)
    
#     logging.info("drawing genealogy graph")
#     build_genealogy_graph.draw_graph(filename, "output.png", threshold = edge_threshold)
    

if __name__ == "__main__":
    
    # interval = 0: getting data from '20230101' to '20230401' (entire three months)
    # interval = 1: getting data from '20230101' to '20230201' (first month)
    # interval = 2: getting data from '20230201' to '20230301' (second month)
    # interval = 3: getting data from '20230301' to '20230401' (third month)

    interval = 3
    num_founders = 50    
    edge_threshold = 0.01
    days_diff = 7
    
    if interval == 1:
        start_date = '20230101'
        end_date = '20230201'
    elif interval == 2:
        start_date = '20230201'
        end_date = '20230301'
    elif interval == 3:
        start_date = '20230301'
        end_date = '20230401'
    else:
        start_date = '20230101'
        end_date = '20230401'
    
    if interval > 0:
        directory = f"data_{interval}/"
    else:
        directory = "data/"
    
    Fitness_and_Nutrition = [
        # fitness
        'Fitness',
        'bodybuilding',
        'running',
        'yoga',
        'crossfit',
        'weightlifting',
        'naturalbodybuilding',
        'powerlifting',
        'jumprope',
        'bodyweightfitness',
        # nutrition
        'nutrition',
        'keto',
        'vegan',
        'paleo',
        'intermittentfasting',
        'plantbaseddiet',
        'lowcarb',
        'whole30',
        '1200isplenty',
        'mealprepsunday' 
        ]

    
    main(Fitness_and_Nutrition, directory = directory, start_date = start_date, end_date = end_date, num_founders = num_founders, 
        edge_threshold = edge_threshold, days_diff = days_diff, is_comments = False, interval = interval)
    