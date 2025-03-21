import cv2
import numpy as np


def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def window_based_matching_cs(left_img, right_img, disparity_range = 64, kernel_size = 3, save_result = True):
    # Read left , right images then convert to grayscale
    left = cv2.imread(left_img, 0)
    right = cv2.imread(right_img, 0)

    left = left.astype(np.float32)
    right = right.astype(np.float32)

    height, width = left.shape[:2]

    # Create blank disparity map
    depth = np.zeros((height, width), np.uint8)

    kernel_half = int((kernel_size - 1)/2)
    scale = 3

    for y in range(kernel_half, height - kernel_half):
        for x in range(kernel_half, width - kernel_half):
            # Find j where cost has minimum value
            disparity = 0
            cost_optimal = -1

            for j in range(disparity_range):
                d = x - j
                cost = -1
                if(d - kernel_half) > 0:
                    wp = left[(y-kernel_half):(y+kernel_half)+1, (x-kernel_half):(x+kernel_half)+1]
                    wqd = right[(y-kernel_half):(y+kernel_half)+1, (d-kernel_half):(d+kernel_half)+1]

                    wp_flattened = wp.flatten()
                    wqd_flattened = wqd .flatten()

                    cost = cosine_similarity(wp_flattened, wqd_flattened)

                if cost > cost_optimal :
                    cost_optimal = cost
                    disparity = j

            # Let depth at (y, x) = j ( disparity ) multiply by a scale factor for visualization purpose
            depth[y, x] = disparity * scale

    if save_result == True :
        print('Saving result ...')
        # Save results
        cv2.imwrite('window_based_cs.png', depth)
        cv2.imwrite('window_based_cs_color.png', cv2.applyColorMap(depth, cv2. COLORMAP_JET))

    print('Done.')

    return depth