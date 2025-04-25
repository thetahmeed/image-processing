## Create and activate the env

```bash
python3 -m venv .venv
```

```bash
source .venv/bin/activate
```

## Install dependencies

```bash
pip install -r requirments.txt
```

### Run

```bash
python3 processing_by_cv2.py
```

```bash
python3 processing_by_pillow.py
```

```bash
python3 equalization.py
```

### Histograms Equalization Output:

![Histograms Equalization Output](https://github.com/thetahmeed/image-processing/blob/main/output/equalization/histograms_equalization.png?raw=true)

### CLAHE Output:

![CLAHE Output](https://github.com/thetahmeed/image-processing/blob/main/output/equalization/clahe_equalization.png?raw=true)

### Enhancement using Cv2:

![cropped_image](https://github.com/thetahmeed/image-processing/blob/main/output/cv2/cropped_image.png?raw=true)

![gray_image](https://github.com/thetahmeed/image-processing/blob/main/output/cv2/gray_image.png?raw=true)

![log_transformed_image](https://github.com/thetahmeed/image-processing/blob/main/output/cv2/log_transformed_image.png?raw=true)

![negative_image](https://github.com/thetahmeed/image-processing/blob/main/output/cv2/negative_image.png?raw=true)

![piecewise_transformed_image](https://github.com/thetahmeed/image-processing/blob/main/output/cv2/piecewise_transformed_image.png?raw=true)

![power_law_transformed_image](https://github.com/thetahmeed/image-processing/blob/main/output/cv2/power_law_transformed_image.png?raw=true)

![Enhancement using Cv2 resized_image_244x244](https://github.com/thetahmeed/image-processing/blob/main/output/cv2/resized_image_244x244.png?raw=true)

![Enhancement using Cv2 threshold_image](https://github.com/thetahmeed/image-processing/blob/main/output/cv2/threshold_image.png?raw=true)

### Enhancement using Pillow:

![cropped_image](https://github.com/thetahmeed/image-processing/blob/main/output/pillow/cropped_image.jpg?raw=true)

![hsv_image](https://github.com/thetahmeed/image-processing/blob/main/output/pillow/hsv_image.jpg?raw=true)

![resized_image_244x244](https://github.com/thetahmeed/image-processing/blob/main/output/pillow/resized_image_244x244.jpg?raw=true)

### Docs

[OpenCV documentation](https://docs.opencv.org/master/)

[Pillow documentation](https://pillow.readthedocs.io/en/latest/handbook/index.html)
