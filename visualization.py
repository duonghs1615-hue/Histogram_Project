import matplotlib.pyplot as plt

from histogram_equalization import calculate_histogram


def show_dashboard(
    original,
    manual_result,
    opencv_result,
    cdf,
    exact_match,
):
    """Display all important results in one 2x3 dashboard."""

    hist_original = calculate_histogram(original)
    hist_equalized = calculate_histogram(manual_result)

    fig, axes = plt.subplots(2, 3, figsize=(16, 9))
    fig.suptitle("Histogram and Histogram Equalization", fontsize=18)

    # Original image
    axes[0, 0].imshow(original, cmap="gray", vmin=0, vmax=255)
    axes[0, 0].set_title("Original Image")
    axes[0, 0].axis("off")

    # Manual result
    axes[0, 1].imshow(manual_result, cmap="gray", vmin=0, vmax=255)
    axes[0, 1].set_title("Manual Histogram Equalization")
    axes[0, 1].axis("off")

    # OpenCV result
    axes[0, 2].imshow(opencv_result, cmap="gray", vmin=0, vmax=255)
    axes[0, 2].set_title("OpenCV Histogram Equalization")
    axes[0, 2].axis("off")

    # Original histogram
    axes[1, 0].plot(range(256), hist_original)
    axes[1, 0].set_title("Original Histogram")
    axes[1, 0].set_xlabel("Gray Level")
    axes[1, 0].set_ylabel("Number of Pixels")
    axes[1, 0].set_xlim(0, 255)
    axes[1, 0].grid(alpha=0.3)

    # Equalized histogram
    axes[1, 1].plot(range(256), hist_equalized)
    axes[1, 1].set_title("Equalized Histogram")
    axes[1, 1].set_xlabel("Gray Level")
    axes[1, 1].set_ylabel("Number of Pixels")
    axes[1, 1].set_xlim(0, 255)
    axes[1, 1].grid(alpha=0.3)

    # CDF
    axes[1, 2].plot(range(256), cdf)
    axes[1, 2].set_title("Cumulative Distribution Function (CDF)")
    axes[1, 2].set_xlabel("Gray Level")
    axes[1, 2].set_ylabel("CDF")
    axes[1, 2].set_xlim(0, 255)
    axes[1, 2].set_ylim(0, 1)
    axes[1, 2].grid(alpha=0.3)

    # Exact Match
    fig.text(
        0.5,
        0.01,
        f"Manual vs OpenCV: Exact Match = {exact_match:.2f}%",
        ha="center",
        fontsize=10,
    )

    fig.subplots_adjust(
    left=0.055,
    right=0.985,
    top=0.91,
    bottom=0.10,
    hspace=0.08,
    wspace=0.12
)
    plt.show()