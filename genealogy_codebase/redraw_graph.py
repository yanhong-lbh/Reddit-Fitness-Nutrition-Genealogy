import pickle
import logging
import sys
import build_genealogy_graph
import pandas as pd

def redraw_graph(new_edge_threshold, interval = 0):
    
    if interval == 0:
        with open("filename.pkl", "rb") as f:
            filename = pickle.load(f)
    else:
        filename = f"data_{interval}/filename_{interval}.csv"
        
    logging.info("drawing genealogy graph with new edge threshold")
    build_genealogy_graph.draw_graph(filename, f"output_{interval}_{new_edge_threshold}.png", threshold = new_edge_threshold)


def main():
    # if len(sys.argv) != 2:
    #     print("Usage: python redraw_graph.py <new_edge_threshold>")
    #     sys.exit(1)
        
    if len(sys.argv) == 2:
        new_edge_threshold = float(sys.argv[1])
        redraw_graph(new_edge_threshold)
    elif len(sys.argv) == 3:
        new_edge_threshold = float(sys.argv[1])
        interval = sys.argv[2]
        redraw_graph(new_edge_threshold, interval = interval)
    else:
        print("Usage: python redraw_graph.py <new_edge_threshold> [<interval>]" )
        sys.exit(1)
        

if __name__ == "__main__":
    main()
