from config import DATASET_DIR
from preprocessing.dataset import DatasetLoader
from utils.logger import logger


def main():

    loader = DatasetLoader(DATASET_DIR)

    videos = loader.load_videos()

    logger.info(f"Total videos : {len(videos)}")

    for video in videos:
        logger.info(video)


if __name__ == "__main__":
    main()