import cv2
import numpy as np

def distance(x, y):
    return abs(x - y)


def squared_distance(x, y):
    return (x - y)**2


def pixel_wise_matching_l1(left_img, right_img, disparity_range=16, save_result = True):
    # Read left , right images then convert to grayscale
    left = cv2.imread(left_img, 0)
    right = cv2.imread(right_img, 0)

    left = left.astype(np.float32)
    right = right.astype(np.float32)

    height, width = left.shape[:2]

    # Create blank disparity map
    depth = np.zeros((height, width), np.uint8)
    scale = int(255/(disparity_range)+0.5)
    max_value = 255

    for y in range(height) :
        for x in range(width):
        # Find j where cost has minimum value
            disparity = 0
            cost_min = max_value

            for j in range (disparity_range):
                cost = max_value if (x - j)<0 else distance(int(left[y, x]), int(right[y, x - j]))

                if cost < cost_min :
                    cost_min = cost
                    disparity = j

            # Let depth at (y, x) = j ( disparity ) multiply by a scale factor for visualization purpose
            depth[y, x] = disparity*scale

    if save_result == True :
        print ('Saving result ...')
        # Save results
        cv2.imwrite('pixel_wise_l1.png', depth)
        cv2.imwrite('pixel_wise_l1_color.png', cv2.applyColorMap(depth, cv2.COLORMAP_JET))

    print ('Done.')

    return depth


def pixel_wise_matching_l2(left_img, right_img, disparity_range=16, save_result = True):
    # Read left , right images then convert to grayscale
    left = cv2.imread(left_img, 0)
    right = cv2.imread(right_img, 0)

    left = left.astype(np.float32)
    right = right.astype(np.float32)

    height, width = left.shape[:2]

    # Create blank disparity map
    depth = np.zeros((height, width), np.uint8)
    scale = int(255/(disparity_range)+0.5)
    max_value = 255**2

    for y in range(height) :
        for x in range(width):
        # Find j where cost has minimum value
            disparity = 0
            cost_min = max_value

            for j in range (disparity_range):
                cost = max_value if (x - j)<0 else squared_distance(int(left[y, x]), int(right[y, x - j]))

                if cost < cost_min :
                    cost_min = cost
                    disparity = j

            # Let depth at (y, x) = j ( disparity ) multiply by a scale factor for visualization purpose
            depth[y, x] = disparity*scale

    if save_result == True :
        print ('Saving result ...')
        # Save results
        cv2.imwrite('pixel_wise_l2.png', depth)
        cv2.imwrite('pixel_wise_l2_color.png', cv2.applyColorMap(depth, cv2.COLORMAP_JET))

    print ('Done.')

    return depth