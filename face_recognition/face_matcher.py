import cv2
import os
import sys
sys.path.append(os.path.dirname(__file__))

from attendance_processor import mark_attendance



# Load face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "lbph_model.yml")

print("Using model path:", MODEL_PATH)

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read(MODEL_PATH)

cap = cv2.VideoCapture(0)

print("🎥 Face matcher started. Press Q to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Camera not accessible")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        face = gray[y:y+h, x:x+w]
        label, confidence = recognizer.predict(face)

        if confidence < 80:
            mark_attendance(label)

        confidence_percent = max(0, min(100, int(100 - confidence)))

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(
            frame,
            f"ID: {label} | Confidence: {confidence_percent}%",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

    cv2.imshow("Face Matcher", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
