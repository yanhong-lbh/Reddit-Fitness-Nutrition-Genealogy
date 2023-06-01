# Community Genealogy: Fitness and Nutrition Subreddits

This repository contains the code and data for the project "Genealogical Relations Between Fitness and Nutrition Communities". The project uses Reddit data to analyze the recent community dynamics between fitness and nutrition communities from 2023/01/01 to 2023/04/01. The main findings of the study are reported in `Community_genealogy_analysis.pdf`.

A substantial portion of the code for building genealogy graphs was adapted from this [repository](https://github.com/JasonDarkBlue/reddit_communities_genealogy). 

## Usage

To generate a graph based on full three-month data, set `interval = 0` in `main.py`.
To generate a graph based on one-month data, set `interval = 1`, `2`, or `3` in `main.py`.
Then, run `python main.py`.

To change the edge threshold and redraw the graph, run:
`python redraw_graph.py <edge threshold> <interval>`

## Python File Descriptions

- `main.py`, `build_user_subreddit_history.py`, `build_genealogy_graph.py`, `download_subreddits`: Modified version of the original codes.
- `centrality_analysis.py`: Perform centrality analysis on full three-month data and interval data.
- `redraw_graph.py`: Allows users to redraw graphs by specifying new edge thresholds and interval.
- `prettier_graph.ipynb`: Use two methods to draw visually appealing graphs.

## Important Directories and Files

- `data`: Data from January 1, 2023, to April 1, 2023.
- `data_1`: Data from January 1, 2023, to February 1, 2023.
- `data_2`: Data from February 1, 2023, to March 1, 2023.
- `data_3`: Data from March 1, 2023, to April 1, 2023.
- `data/parent_child_weights.csv`: Full list of edge weights for the entire interval (used in Section 2: Edge Weight Analysis, Section 3: Centrality Analysis of `Community_genealogy_analysis.pdf`).
- `data_[1/2/3]/filename_[1/2/3]`: Full list of edge weights for each interval (used in Section 4: Temporal Analysis of `Community_genealogy_analysis.pdf`).

## Credits

A lot of the code used to build genealogy graphs was adapted from this [repository](https://github.com/JasonDarkBlue/reddit_communities_genealogy). Special thanks to the author of the original repository for providing a starting point for this analysis. 

## Contact

If you have any questions about the repository or want to report issues, please contact me.


