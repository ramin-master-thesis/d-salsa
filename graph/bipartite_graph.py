import ast
import os

import click
import pandas as pd

from graph import current_directory

DATA_FOLDER = '../data'
ADJACENCY_LIST = "adjacency_list"
LEFT_INDEX = pd.DataFrame()
RIGHT_INDEX = pd.DataFrame()


def load_indexes(partition_method: str = "single_partition", partition_number: int = 0):
    global LEFT_INDEX
    global RIGHT_INDEX
    sides = ["left", "right"]
    partition_folder = f"partition_{partition_number}"
    for side in sides:
        index_file = f"{side}_index.csv"
        index_csv = os.path.join(current_directory, DATA_FOLDER, partition_method, partition_folder, index_file)
        side_index = pd.read_csv(index_csv, index_col=0)
        side_index[ADJACENCY_LIST] = side_index[ADJACENCY_LIST].map(ast.literal_eval)
        if side == "left":
            LEFT_INDEX = side_index
        else:
            RIGHT_INDEX = side_index
        click.echo(f"finish loading the {side} index")


def get_left_node_neighbors(node: int) -> list:
    try:
        values = LEFT_INDEX._get_value(node, ADJACENCY_LIST)
    except KeyError:
        return []
    return values


def get_right_node_neighbors(node) -> list:
    try:
        values = RIGHT_INDEX._get_value(node, ADJACENCY_LIST)
    except KeyError:
        return []
    return values