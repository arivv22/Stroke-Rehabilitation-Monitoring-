from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

DATASET_DIR = ROOT_DIR / "datasets"

MODEL_DIR = ROOT_DIR / "models"

OUTPUT_DIR = ROOT_DIR / "outputs"

DEVICE = "cpu"

IMAGE_SIZE = 640

CONFIDENCE_THRESHOLD = 0.5