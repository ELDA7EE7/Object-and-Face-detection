from os import path
import numpy as np
import cv2
from tkinter import filedialog
def UploadImage():
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if file_path:
        UploadTemplate(file_path)

def UploadTemplate(image_path: str):
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if file_path:
        ObjectDetection(image_path,file_path)
def ObjectDetection(image_path: str,template_path: str):
    img=cv2.imread(image_path, 0)
    display_img=cv2.imread(image_path)
    if img is None:
        print("img not found ",img)
        return
    
    img = cv2.resize(img, (0, 0), fx=0.8, fy=0.8)
    display_img = cv2.resize(display_img, (0, 0), fx=0.8, fy=0.8)
    template=cv2.imread(template_path, 0)

    if template is None:
        print("template not found ",template)
        return
    
    template = cv2.resize(template, (0, 0), fx=0.8, fy=0.8)
    h, w = template.shape

    methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
                cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

    for method in methods:
        img2 = img.copy()
        display_img2=display_img.copy()
        result = cv2.matchTemplate(img2, template, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            location = min_loc
        else:
            location = max_loc

        bottom_right = (location[0] + w, location[1] + h)    
        cv2.rectangle(display_img2, location, bottom_right, 255, 5)
        cv2.imshow('Match', display_img2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()