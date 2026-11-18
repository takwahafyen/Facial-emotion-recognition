# ============================================================
#  emotions_advice.py
#  Psychological conseil for each detected emotion
# ============================================================

EMOTION_ADVICE = {
    "angry": {
        "emoji": "😠",
        "color": (0, 0, 220),          # BGR Red
        "title": "ANGRY",
        "conseil": [
            "Take 3 deep breaths slowly.",
            "Count to 10 before reacting.",
            "Step away & cool down first.",
        ],
        "tip": "Anger is energy — redirect it."
    },
    "disgust": {
        "emoji": "🤢",
        "color": (0, 128, 0),          # BGR Green
        "title": "DISGUST",
        "conseil": [
            "Acknowledge what bothers you.",
            "Ask: is this worth your energy?",
            "Set a healthy boundary calmly.",
        ],
        "tip": "Your values are speaking to you."
    },
    "fear": {
        "emoji": "😨",
        "color": (128, 0, 128),        # BGR Purple
        "title": "FEAR",
        "conseil": [
            "Ground yourself: name 5 things",
            "you can see around you right now.",
            "Breathe in 4s, hold 4s, out 4s.",
        ],
        "tip": "Fear is a signal, not a stop sign."
    },
    "happy": {
        "emoji": "😄",
        "color": (0, 215, 255),        # BGR Gold
        "title": "HAPPY",
        "conseil": [
            "Enjoy this moment fully.",
            "Share your positivity with someone.",
            "Note what made you happy today.",
        ],
        "tip": "Happiness shared is happiness doubled."
    },
    "neutral": {
        "emoji": "😐",
        "color": (200, 200, 200),      # BGR Light Gray
        "title": "NEUTRAL",
        "conseil": [
            "A calm mind is your superpower.",
            "Use this clarity to focus & plan.",
            "Check in: how do you really feel?",
        ],
        "tip": "Peace is productive."
    },
    "sad": {
        "emoji": "😢",
        "color": (220, 100, 0),        # BGR Blue-ish
        "title": "SAD",
        "conseil": [
            "It is okay to feel sad.",
            "Talk to someone you trust today.",
            "Be gentle with yourself right now.",
        ],
        "tip": "Every storm runs out of rain."
    },
    "surprise": {
        "emoji": "😲",
        "color": (0, 165, 255),        # BGR Orange
        "title": "SURPRISE",
        "conseil": [
            "Pause. Take a breath.",
            "Process before you react.",
            "Ask: what does this change for me?",
        ],
        "tip": "Life is full of unexpected gifts."
    },
}


def get_advice(emotion: str) -> dict:
    """
    Returns the advice dict for a given emotion string.
    Falls back to 'neutral' if emotion not recognized.
    """
    return EMOTION_ADVICE.get(emotion.lower(), EMOTION_ADVICE["neutral"])
