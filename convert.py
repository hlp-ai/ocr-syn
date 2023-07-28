import os

image_dir = r"d:\kidden\mt\open\tr\default"
label_file = os.path.join(image_dir, "labels.txt")
labels = open(label_file, encoding="utf-8").readlines()
labels = [label.strip() for label in labels]

files = os.listdir(image_dir)
files = list(filter(lambda f:f.endswith(".jpg"), files))


new_label_file = open("syn_labels.txt", "w", encoding="utf-8")


for f, t in zip(files, labels):
    img = os.path.join(image_dir, f)
    new_label_file.write(img + "\t" + t + "\n")
