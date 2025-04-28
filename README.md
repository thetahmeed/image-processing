## Create and activate the env

```bash
python3 -m venv .venv
```

```bash
source .venv/bin/activate
```

## Install dependencies

```bash
pip3 install -r requirments.txt
```

## For compariasm

```bash
pip3 install numpy
pip3 install matplotlib
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

#### 1. cropped_image

![cropped_image](https://github.com/thetahmeed/image-processing/blob/main/output/cv2/cropped_image.png?raw=true)

#### 2. gray_image

![gray_image](https://github.com/thetahmeed/image-processing/blob/main/output/cv2/gray_image.png?raw=true)

#### 3. log_transformed_image

![log_transformed_image](https://github.com/thetahmeed/image-processing/blob/main/output/cv2/log_transformed_image.png?raw=true)

#### 4. negative_image

![negative_image](https://github.com/thetahmeed/image-processing/blob/main/output/cv2/negative_image.png?raw=true)

#### 5. piecewise_transformed_image

![piecewise_transformed_image](https://github.com/thetahmeed/image-processing/blob/main/output/cv2/piecewise_transformed_image.png?raw=true)

#### 6. power_law_transformed_image

![power_law_transformed_image](https://github.com/thetahmeed/image-processing/blob/main/output/cv2/power_law_transformed_image.png?raw=true)

#### 7. resized_image_244x244

![resized_image_244x244](https://github.com/thetahmeed/image-processing/blob/main/output/cv2/resized_image_244x244.png?raw=true)

#### 8. threshold_image

![threshold_image](https://github.com/thetahmeed/image-processing/blob/main/output/cv2/threshold_image.png?raw=true)

### Enhancement using Pillow:

#### 1. cropped_image

![cropped_image](https://github.com/thetahmeed/image-processing/blob/main/output/pillow/cropped_image.jpg?raw=true)

#### 2. hsv_image

![hsv_image](https://github.com/thetahmeed/image-processing/blob/main/output/pillow/hsv_image.jpg?raw=true)

#### 3. resized_image_244x244

![resized_image_244x244](https://github.com/thetahmeed/image-processing/blob/main/output/pillow/resized_image_244x244.jpg?raw=true)

### Docs

[OpenCV documentation](https://docs.opencv.org/master/)

[Pillow documentation](https://pillow.readthedocs.io/en/latest/handbook/index.html)
