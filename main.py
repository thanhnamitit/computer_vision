import cv2
import time


def sliding_window(image, initial_window_size, step_size, scale_factor):
    (image_height, image_width) = image.shape[:2]

    window_size = initial_window_size

    while window_size[0] <= image_width and window_size[1] <= image_height:
        for y in range(0, image_height - window_size[1], step_size):
            for x in range(0, image_width - window_size[0], step_size):
                top_left = (x, y)
                bottom_right = (x + window_size[0], y + window_size[1])

                window_image = image.copy()
                cv2.rectangle(window_image, top_left, bottom_right, (0, 255, 0), 2)

                # Extract the image region within the window
                window_region = image[y:y + window_size[1], x:x + window_size[0]]

                # Display the image with the window
                cv2.imshow("Sliding Window", window_image)
                cv2.imshow("Cropped Window", window_region)
                cv2.waitKey(1)

        window_size = (int(window_size[0] * scale_factor), int(window_size[1] * scale_factor))

    cv2.destroyAllWindows()


image = cv2.imread("image.jpg")

initial_window_size = (100, 100)
scale_factor = 1.2
step_size = 50

sliding_window(image, initial_window_size, step_size, scale_factor)
