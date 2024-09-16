import numpy as np
import cv2


def compute_difference(bg_img, input_img):
    difference_single_channel = np.max(np.abs(bg_img - input_img), axis=2)
    return difference_single_channel


def compute_binary_mask(difference_single_channel):
    difference_binary = np.where(difference_single_channel > 0, 255, 0)
    difference_binary = np.repeat(
        difference_binary[:, :, np.newaxis], 3, axis=2)
    return difference_binary


def replace_background(bg1_image, bg2_image, ob_image):
    difference_single_channel = compute_difference(bg1_image, ob_image)
    difference_binary = compute_binary_mask(difference_single_channel)
    output = np.where(difference_binary == 255, ob_image, bg2_image)
    return output
