import cv2
import mediapipe as mp
import pyautogui

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

cap = cv2.VideoCapture(0)

finger_tips = [4, 8, 12, 16, 20]
prev_gesture = None

def get_finger_status(hand_landmarks):
    fingers = []
    landmarks = hand_landmarks.landmark
    if landmarks[finger_tips[0]].x < landmarks[finger_tips[0] - 1].x:
        fingers.append(1)
    else:
        fingers.append(0)
    for tip in finger_tips[1:]:
        if landmarks[tip].y < landmarks[tip - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)
    return fingers

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            fingers = get_finger_status(hand_landmarks)
            gesture = None

            if fingers == [0, 1, 0, 0, 0]:
                gesture = "NEXT_SLIDE"
            elif fingers == [0, 1, 1, 0, 0]:
                gesture = "PREV_SLIDE"
            elif fingers == [0, 0, 0, 0, 0]:
                gesture = "PLAY_PAUSE"
            elif fingers == [1, 1, 1, 1, 1]:
                gesture = "VOLUME_UP"
            elif fingers == [0, 1, 1, 1, 1]:
                gesture = "VOLUME_DOWN"

            if gesture and gesture != prev_gesture:
                if gesture == "NEXT_SLIDE":
                    pyautogui.press("right")
                elif gesture == "PREV_SLIDE":
                    pyautogui.press("left")
                elif gesture == "PLAY_PAUSE":
                    pyautogui.press("space")
                elif gesture == "VOLUME_UP":
                    pyautogui.press("volumeup")
                elif gesture == "VOLUME_DOWN":
                    pyautogui.press("volumedown")
                prev_gesture = gesture

    cv2.imshow("Gesture Control", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
