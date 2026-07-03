from pathlib import Path

VIDEO_EXTENSIONS = (".mp4", ".avi", ".mov")


class DatasetLoader:

    def __init__(self, dataset_dir):
        self.dataset_dir = Path(dataset_dir)

    def load_videos(self):

        videos = []

        for ext in VIDEO_EXTENSIONS:
            videos.extend(self.dataset_dir.rglob(f"*{ext}"))

        return sorted(videos)