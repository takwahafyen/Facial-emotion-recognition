# ============================================================
#  realtime.py
#  Real-time facial emotion detection with psychological advice
#  Usage: python src/realtime.py
# ============================================================

import cv2
import numpy as np
from keras.models import load_model
from emotions_advice import get_advice

# ── Config ───────────────────────────────────────────────────
MODEL_PATH   = "models/emotion_model.h5"
CASCADE_PATH = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
IMG_SIZE     = 48
EMOTIONS     = ["angry", "disgust", "fear", "happy", "neutral", "sad", "surprise"]

# UI settings
PANEL_WIDTH  = 320          # Right sidebar width for advice
FONT         = cv2.FONT_HERSHEY_SIMPLEX
# ─────────────────────────────────────────────────────────────


def draw_advice_panel(frame, emotion_data: dict, panel_width: int = PANEL_WIDTH):
    """Draw a styled sidebar panel with the psychological conseil."""
    h, w = frame.shape[:2]
    # Extend canvas to the right
    canvas = np.zeros((h, w + panel_width, 3), dtype=np.uint8)
    canvas[:, :w] = frame

    color  = emotion_data["color"]
    title  = emotion_data["title"]
    lines  = emotion_data["conseil"]
    tip    = emotion_data["tip"]

    # Panel background
    cv2.rectangle(canvas, (w, 0), (w + panel_width, h), (30, 30, 30), -1)
    cv2.rectangle(canvas, (w, 0), (w + panel_width, 60), color, -1)

    # Emotion title
    cv2.putText(canvas, title, (w + 10, 42),
                FONT, 1.0, (255, 255, 255), 2, cv2.LINE_AA)

    # Section: Psychological Conseil
    cv2.putText(canvas, "Psychological Conseil:", (w + 10, 100),
                FONT, 0.5, color, 1, cv2.LINE_AA)
    cv2.line(canvas, (w + 10, 110), (w + panel_width - 10, 110), color, 1)

    for i, line in enumerate(lines):
        cv2.putText(canvas, line, (w + 10, 140 + i * 28),
                    FONT, 0.45, (230, 230, 230), 1, cv2.LINE_AA)

    # Divider
    cv2.line(canvas, (w + 10, 240), (w + panel_width - 10, 240), (80, 80, 80), 1)

    # Motivational tip
    cv2.putText(canvas, "Mindset Tip:", (w + 10, 268),
                FONT, 0.45, color, 1, cv2.LINE_AA)
    # Word-wrap the tip across two lines if needed
    words = tip.split()
    line1, line2 = " ".join(words[:5]), " ".join(words[5:])
    cv2.putText(canvas, line1, (w + 10, 295),
                FONT, 0.42, (200, 200, 200), 1, cv2.LINE_AA)
    if line2:
        cv2.putText(canvas, line2, (w + 10, 318),
                    FONT, 0.42, (200, 200, 200), 1, cv2.LINE_AA)

    # Footer
    cv2.putText(canvas, "Press Q to quit", (w + 10, h - 15),
                FONT, 0.38, (100, 100, 100), 1, cv2.LINE_AA)
    return canvas


def predict_emotion(face_roi, model):
    """Preprocess face ROI and return predicted emotion string."""
    gray_face = cv2.cvtColor(face_roi, cv2.COLOR_BGR2GRAY)
    resized   = cv2.resize(gray_face, (IMG_SIZE, IMG_SIZE))
    normalized = resized / 255.0
    input_arr  = np.expand_dims(np.expand_dims(normalized, -1), 0)
    prediction = model.predict(input_arr, verbose=0)
    return EMOTIONS[np.argmax(prediction)], float(np.max(prediction))


def run():
    model    = load_model(MODEL_PATH)
    detector = cv2.CascadeClassifier(CASCADE_PATH)
    cap      = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("[ERROR] Cannot open webcam.")
        return

    print("[INFO] Starting real-time emotion detection. Press Q to quit.")

    current_emotion = "neutral"   # default on startup

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces      = detector.detectMultiScale(
            gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(48, 48)
        )

        for (x, y, w, h) in faces:
            face_roi         = frame[y:y+h, x:x+w]
            emotion, conf    = predict_emotion(face_roi, model)
            current_emotion  = emotion
            advice           = get_advice(emotion)
            color            = advice["color"]

            # Draw bounding box + label on main frame
            cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
            label = f"{emotion.upper()}  {conf*100:.0f}%"
            cv2.putText(frame, label, (x, y - 10),
                        FONT, 0.65, color, 2, cv2.LINE_AA)

        # Always show advice panel (last detected emotion)
        advice_data = get_advice(current_emotion)
        output      = draw_advice_panel(frame, advice_data)

        cv2.imshow("Facial Emotion Recognition  |  Psychological Conseil", output)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run()
