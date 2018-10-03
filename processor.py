# make stuff. do stuff. hack! fuck yeah

import os
import sys
import pandas as pd
from template import template, bbox
import imagesize

def build_annotation_dict(bounding_box_file):
    annotations_dict = dict()
    annotation_lines = open(bounding_box_file).readlines()
    header = annotation_lines[0].strip().split(',')
    annotation_lines = annotation_lines[1:]
    for line in annotation_lines:
        val = line.strip().split(',')
        key = val[0]
        if key not in annotations_dict.keys():
            annotations_dict[key] = []
        output = dict(zip(header[1:], val[1:]))
        annotations_dict[key].append(output)
    return annotations_dict

def extract(box, img_width, img_height):
    label = box['LabelName']
    xmin = int(float(box['XMin'])*img_width)
    ymin = int(float(box['YMin'])*img_height)
    xmax = int(float(box['XMax'])*img_width)
    ymax = int(float(box['YMax'])*img_height)
    isTruncated = box['IsTruncated']
    return label, xmin, ymin, xmax, ymax, isTruncated

def build_bbox_str(boxes, width, height):
    objectstr = ''
    for box in boxes:
        label, xmin, ymin, xmax, ymax, isTruncated = extract(box, width, height)
        objectstr += bbox.format(label=label,
                                 truncated=isTruncated,
                                 xmin=xmin,
                                 ymin=ymin,
                                 xmax=xmax,
                                 ymax=ymax)
    return objectstr

def build_xml(bbox_str, fname, width, height):
    return template.format(filename=fname,
                           width=width,
                           height=height,
                           objectstr=bbox_str)

def save_xml(xmlstr, key, savedir):
    fname = savedir + key + '.xml'
    with open(fname, "w") as fi:
        fi.write(xmlstr)

def analyze_images(images_direc, annotations_direc, annotations_dict):
    images = os.listdir(images_direc)
    for image in images:
        key = image.split('.')[0]
        width, height = imagesize.get(images_direc + image)
        boxes = annotations_dict[key]
        bbox_str = build_bbox_str(boxes, width, height)
        xml = build_xml(bbox_str, image, width, height)
        save_xml(xml, key, annotations_direc)


if __name__ == '__main__':
    annotations_dict = build_annotation_dict('./train_bounding_boxes.csv')
    analyze_images('/Users/bhu/work/darkflow/train_e/', '/Users/bhu/work/darkflow/annotations_train_e/', annotations_dict)
