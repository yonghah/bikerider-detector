"""
mostly from:
    https://github.com/datitran/raccoon_dataset/blob/master/xml_to_csv.py
"""

import os
import glob
import xml.etree.ElementTree as ET
import pandas as pd


def main():
    '''main function'''
    anno_path = os.path.join("..", "..", "data", "training",
                             "annotation")
    csv_path = os.path.join("..", "..", "data", "training",
                            "data", "bikerider_labels.csv")
    xml_df = xml_to_csv(anno_path)
    xml_df.to_csv(csv_path, index=None)
    print('Successfully converted xml to csv.')


def xml_to_csv(path):
    '''merge xmls to csv'''
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text))
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin',
                   'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


if __name__ == "__main__":
    main()
