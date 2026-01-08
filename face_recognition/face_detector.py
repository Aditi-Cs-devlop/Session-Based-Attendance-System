
import cv2


class FaceDetector:
    """
    Detects human faces using OpenCV Haar Cascade.
    """

    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        )

    def detect_faces(self, image):
        if image is None:
            return []

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces = self.face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.3,
            minNeighbors=5,
            minSize=(40, 40)
        )

        return faces


# ✅ TEST CODE MUST BE AT THE BOTTOM
if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    detector = FaceDetector()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        faces = detector.detect_faces(frame)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow("Face Detection Test", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

