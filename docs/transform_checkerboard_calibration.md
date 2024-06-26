## Checkerboard calibration

This function uses images of checkerboards to correct distortions introduced by cameras. The checkerboard calibration works best with > 10 checkerboard images at different angles to the camera and in different areas of the field of view. 

**plantcv.transform.checkerboard_calib**(*img_path, col_corners, row_corners, out_dir*)

**returns** mtx, dist

- **Parameters:**
    - img_path - a path to a directory of checkerboard images
    - col_corners - the number of *inner* corners in a column of the checkerboard
    - row_corners - the number of *inner* corners in a row of the checkerboard
    - out_dir - directory where the output files will be saved

- **Context:**
    - Used to create calibration matrices for camera calibration
    - Outputs can be passed to [**plantcv.transform.calibrate_camera**](transform_calibrate_camera.md) for distortion corrections

- **Example use:**

**Checkerboard image example**

![Screenshot](img/documentation_images/transform_camera_calibration/checkerboard_example.png)

**Checkerboard calibration**

![Screenshot](img/documentation_images/transform_camera_calibration/corners_registered_checkerboard.png)

```python

from plantcv import plantcv as pcv

# Set global debug behavior to None (default), "print" (to file), or "plot" (Jupyter Notebooks or X11)
pcv.params.debug = "plot"

# Create calibration matrices with checkerboard images
mtx, dist = pcv.transform.checkerboard_calib(img_path = "./img_files/", col_corners = 13, row_corners = 19, out_dir = "./output/")

# Correct distortions using the outputs from checkerboard calibration
corrected_img = pcv.transform.calibrate_camera(rgb_img = img, mtx_filename = "./output/mtx.npz", dist_filename = "./output/dist.npz")

```

**Source Code:** [Here](https://github.com/danforthcenter/plantcv/blob/main/plantcv/plantcv/transform/checkerboard_calib.py)
