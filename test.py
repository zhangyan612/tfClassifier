import os

cmd = (
    "Python classifier.py --image_file {filePath} {option}").format(
        filePath ='D:\Work\projects/tfClassifier/images/putin.jpg',
        option='--num_top_predictions 5')
os.system(cmd)