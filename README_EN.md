# Histogram and Histogram Equalization

[Vietnamese](README.md) | English

A Digital Image Processing project that demonstrates Histogram Equalization on 8-bit grayscale images using Python.
## Features

- Read input images as 8-bit grayscale images.
- Manually calculate the histogram, normalized histogram, cumulative distribution function (CDF), gray-level mapping, and equalized image.
- Use OpenCV's `cv2.equalizeHist()` as a reference for comparison with the manual implementation.
- Calculate the **Exact Match** percentage between the two output images.
- Display the input image, both output images, the original and equalized histograms, and the CDF in a 2 × 3 dashboard.
- Save the Manual and OpenCV output images separately in the `results/` directory.

## Project Structure

```text
Histogram_Project/
├── main.py                    # Image loading and main program flow
├── histogram_equalization.py  # Manual algorithm and result comparison
├── visualization.py           # Image, histogram, and CDF display
├── images/                    # Input images
└── results/                   # Processed output images
```

## Installation

Install Python, then open a terminal in the project directory and install the required package:

```powershell
py -m pip install -r requirements.txt
```

To clone the repository:

```powershell
git clone https://github.com/duonghs1615-hue/Histogram_Project.git
cd Histogram_Project
```

## Usage

Place an input image in the `images/` directory and run:

```powershell
py main.py images/image1.jpg
```

To test another image, provide its path, for example:

```powershell
py main.py images/image3.tif
```

If you run `py main.py` without an image path, the program uses the path specified by `DEFAULT_IMAGE_PATH` in `main.py`.

## Output

The program prints image information and the Exact Match percentage in the terminal and opens a dashboard to show the results. The two processed images are saved as:

```text
results/<image_name>_manual.png
results/<image_name>_opencv.png
```

The dashboard is displayed on screen only; it is not automatically saved as an image.

**Note:** An Exact Match of 100% means that the two output images have identical pixel values. It does not necessarily mean that the processed image looks better than the original.

## Implementation Note

The manual Histogram Equalization algorithm is implemented in `histogram_equalization.py`. OpenCV's `cv2.equalizeHist()` is used only as a reference and does not replace the manual algorithm steps.
