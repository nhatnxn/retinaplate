import os
import json
import pandas
import cv2

if __name__ == '__main__':

    data = pandas.read_csv("plate_seg_csv.csv", sep=",")
    root_data = '/home/buithoai/Downloads/Plate_seg_data/plate_images'
    out_json = 'out_json'

    # print(data['region_shape_attributes'].values)
    # print(data['filename'].values)

    shapes = data['region_shape_attributes'].values 
    filename = data['filename'].values

    set_file = set()
    null = None
    
    for i, fi in enumerate(filename):
        name = fi.replace(".jpg", '')
        if fi not in set_file:
            set_file.add(fi)
            img = cv2.imread(os.path.join(root_data, fi))
            h, w = img.shape[:2]
            result = {
                "version" : "TThoai",
                "flags" : {},
                "shapes" : [], 
                "imagePath" : fi,
                "imageHeight" : h,
                "imageWidth" : w
            }

            shape = json.loads(shapes[i])


            xs = shape['all_points_x']
            ys = shape['all_points_y']

            point = {
                "label" : "lpn",
                "points" : [
                    [xs[0], ys[0]], 
                    [xs[1], ys[1]], 
                    [xs[2], ys[2]], 
                    [xs[3], ys[3]]
                ],
                "group_id" : null,
                "shape_type" : "polygon",
                "flags": {}
            }
            result["shapes"].append(point)
            with open(os.path.join(out_json, name + '.json'), 'a') as js:
                json.dump(result, js)


        else:
            with open(os.path.join(out_json, name + '.json'), 'r') as jr:
                result = json.load(jr)

            shape = json.loads(shapes[i])


            xs = shape['all_points_x']
            ys = shape['all_points_y']

            point = {
                "label" : "lpn",
                "points" : [
                    [xs[0], ys[0]], 
                    [xs[1], ys[1]], 
                    [xs[2], ys[2]], 
                    [xs[3], ys[3]]
                ],
                "group_id" : null,
                "shape_type" : "polygon",
                "flags": {}
            }

            result['shapes'].append(point)

            with open(os.path.join(out_json, name + '.json'), 'w') as js:
                json.dump(result, js)

            

        




   