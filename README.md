## Create env

```bash
python3 -m venv .venv
```

## Activate env

```bash
source .venv/bin/activate
```

## Loading the image

## Way 1: Using OpenCV

Supperts: PNG, JPG, TIFF, and BMP

```bash
pip install opencv-python
```

```py
import cv2
image = cv2.imread("images/COVID19(387).jpg")
```

## Way 2: Using OpenCV

Support more like PSD, ICO, and WEBP

```bash
pip install pillow
```

```py
from PIL import Image
image = Image.open("images/COVID19(387).jpg")
```
