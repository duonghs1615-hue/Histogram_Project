import numpy as np


GRAY_LEVELS = 256
MAX_GRAY = 255


def calculate_histogram(image):
    """Calculate the histogram manually."""
    hist = np.zeros(GRAY_LEVELS, dtype=np.int64)

    for pixel in image.flatten():
        hist[pixel] += 1

    return hist


def normalize_histogram(hist, total_pixels):
    """Normalize the histogram."""
    return hist / total_pixels


def calculate_cdf(probability):
    """Calculate the CDF manually."""
    cdf = np.zeros(GRAY_LEVELS, dtype=np.float64)
    running_sum = 0.0

    for gray_level in range(GRAY_LEVELS):
        running_sum += probability[gray_level]
        cdf[gray_level] = running_sum

    return cdf


def create_mapping(cdf, hist):
    """Create the gray-level mapping."""
    used_levels = np.where(hist > 0)[0]

    if len(used_levels) == 0:
        return np.arange(GRAY_LEVELS, dtype=np.uint8)

    cdf_min = cdf[used_levels[0]]

    # Constant image
    if np.isclose(cdf_min, 1.0):
        return np.arange(GRAY_LEVELS, dtype=np.uint8)

    mapping = np.zeros(GRAY_LEVELS, dtype=np.uint8)

    for gray_level in range(GRAY_LEVELS):
        mapped_value = (
            (cdf[gray_level] - cdf_min)
            / (1.0 - cdf_min)
            * MAX_GRAY
        )

        mapping[gray_level] = np.uint8(
            np.clip(np.round(mapped_value), 0, MAX_GRAY)
        )

    return mapping


def apply_mapping(image, mapping):
    """Apply the mapping to every pixel."""
    output = np.zeros_like(image)
    height, width = image.shape

    for row in range(height):
        for col in range(width):
            output[row, col] = mapping[image[row, col]]

    return output


def equalize_histogram_manual(image):
    """Perform Histogram Equalization manually."""
    hist = calculate_histogram(image)
    probability = normalize_histogram(hist, image.size)
    cdf = calculate_cdf(probability)
    mapping = create_mapping(cdf, hist)
    equalized_image = apply_mapping(image, mapping)

    return {
        "image": equalized_image,
        "histogram": hist,
        "probability": probability,
        "cdf": cdf,
        "mapping": mapping,
    }


def compare_images(manual_result, opencv_result):
    """Calculate the exact pixel match percentage."""
    matching_pixels = np.count_nonzero(
        manual_result == opencv_result
    )

    return 100.0 * matching_pixels / manual_result.size