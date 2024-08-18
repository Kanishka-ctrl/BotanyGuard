import cv2

# Try different indices to find the correct one
for i in range(4):  # Test the first 4 indices (0, 1, 2, 3)
    cap = cv2.VideoCapture(i)
    if cap.isOpened():
        print(f"Webcam {i} works!")
        ret, frame = cap.read()
        if ret:
            cv2.imshow(f'Webcam {i} - Press any key to close', frame)
            cv2.waitKey(0)  # Wait for a key press to close the window
        cap.release()
        cv2.destroyAllWindows()
        break
    else:
        print(f"Webcam {i} does not work.")
    cap.release()
