import cv2
import time
import os

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 171

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k % 256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif img_counter == 250:
        break
    else:
        print(img_counter)
        img_name = "test_local{}.jpg".format(img_counter)
        save_path = 'C:/Users/cpreg/PycharmProjects/InfinityGrade/FotosLocal/images'
        cv2.imwrite(os.path.join(save_path, img_name), frame)
        img_counter += 1
        time.sleep(1.5)


cam.release()

cv2.destroyAllWindows()