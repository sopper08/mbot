#!/usr/bin/env python3
import pandas as pd


def main():
    odom_pos = pd.read_json('./tmp_datas/odom_pos.json')
    real_pos = pd.read_json('./tmp_datas/real_pos.json')
    print(odom_pos.head())
    print(real_pos.head())

if __name__ == "__main__":
    main()