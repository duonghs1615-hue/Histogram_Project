from pathlib import Path
import sys

import cv2

from histogram_equalization import (
    compare_images,
    equalize_histogram_manual,
)
from visualization import show_dashboard


DEFAULT_IMAGE_PATH = "images/image4.jpg"
RESULTS_DIR = Path("results")


def read_grayscale_image(path):
    """Read an image directly as an 8-bit grayscale image."""
    image = cv2.imread(str(path), cv2.IMREAD_GRAYSCALE)

    if image is None:
        raise FileNotFoundError(f"Cannot find or open image: {path}")

    return image


def print_summary(image_path, image, manual_data, exact_match):
    """Print only the information useful for the assignment."""
    used_levels = (manual_data["histogram"] > 0).sum()

    print("=" * 68)
    print("HISTOGRAM AND HISTOGRAM EQUALIZATION DEMO")
    print("=" * 68)
    print(f"Input image                : {image_path}")
    print(f"Image size                 : {image.shape[1]} x {image.shape[0]}")
    print(f"Total pixels               : {image.size}")
    print(f"Input gray-level range     : {image.min()} - {image.max()}")
    print(f"Gray levels actually used : {used_levels} / 256")
    print()
    print("MANUAL vs OPENCV")
    print(f"Exact match                : {exact_match:.2f}%")
    print("=" * 68)


def main():
    # Usage:
    #   python main.py
    #   python main.py images/dark.jpg
    image_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(DEFAULT_IMAGE_PATH)

    gray_image = read_grayscale_image(image_path)

    # Manual implementation: no cv2.equalizeHist() is used here.
    manual_data = equalize_histogram_manual(gray_image)
    manual_result = manual_data["image"]

    # Library implementation used only for comparison.
    opencv_result = cv2.equalizeHist(gray_image)

    exact_match = compare_images(
    manual_result,
    opencv_result
)
    print_summary(image_path, gray_image, manual_data, exact_match)

    RESULTS_DIR.mkdir(exist_ok=True)
    stem = image_path.stem

    manual_path = RESULTS_DIR / f"{stem}_manual.png"
    opencv_path = RESULTS_DIR / f"{stem}_opencv.png"

    cv2.imwrite(str(manual_path), manual_result)
    cv2.imwrite(str(opencv_path), opencv_result)

    show_dashboard(
    gray_image,
    manual_result,
    opencv_result,
    manual_data["cdf"],
    exact_match,
)

    print(f"Saved manual result : {manual_path}")
    print(f"Saved OpenCV result : {opencv_path}")


if __name__ == "__main__":
    main()
