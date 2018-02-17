"""
split dataset into train and test set.
Usage:
    python split_train_test.py --test_ratio=0.3
"""


import os
import argparse

import numpy as np
import pandas as pd
np.random.seed(1)


def main():
    '''main function'''
    parser = argparse.ArgumentParser()
    parser.add_argument("--test_ratio", type=float, default=0.2,
                        help="ratio of test set")
    args = parser.parse_args()
    split(args.test_ratio)


def split(test_ratio):
    '''split function'''
    print(test_ratio)
    csv_dir = "../data/training/data"
    full_labels = pd.read_csv(os.path.join(csv_dir, 'bikerider_labels.csv'))
    gb = full_labels.groupby('filename')
    grouped_list = [gb.get_group(x) for x in gb.groups]
    size_train_set = int(len(grouped_list) * (1-test_ratio))
    print("train image {} out of total {}".format(size_train_set,
                                                  len(grouped_list)))

    train_index = np.random.choice(len(grouped_list), size=size_train_set,
                                   replace=False)
    test_index = np.setdiff1d(list(range(len(grouped_list))), train_index)
    train = pd.concat([grouped_list[i] for i in train_index])
    test = pd.concat([grouped_list[i] for i in test_index])
    print(len(train), len(test))
    train.to_csv(os.path.join(csv_dir, 'train_labels.csv'), index=None)
    test.to_csv(os.path.join(csv_dir, 'test_labels.csv'), index=None)


if __name__ == "__main__":
    main()
