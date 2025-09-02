# Computer Vision Gesture Control System

A real-time computer vision project that allows hands-free control of **PowerPoint slides** and **media playback** using hand gestures.

## 🚀 Features
- **Gesture Recognition** using MediaPipe
- **PowerPoint Controller**: Next/Previous slides
- **Media Controller**: Play/Pause, Volume Up/Down
- Runs at ~30 FPS on standard webcam

## 🛠 Tech Stack
- Python
- OpenCV
- MediaPipe
- PyAutoGUI

## ⚡ Setup Instructions
```bash
git clone https://github.com/your-username/gesture-control-system.git
cd gesture-control-system
pip install -r requirements.txt
python gesture_control.py
```

## ✋ Gesture Mappings
| Gesture                  | Action             |
|--------------------------|-------------------|
| Index finger up          | Next Slide        |
| Index + Middle up        | Previous Slide    |
| Fist (all fingers down)  | Play/Pause Media  |
| Open Palm (all up)       | Volume Up         |
| Four Fingers (no thumb)  | Volume Down       |
