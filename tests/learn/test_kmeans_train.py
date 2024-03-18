import numpy as np
import cv2
import os
from joblib import load
from plantcv.learn.train_kmeans import train_kmeans, patch_extract


def test_train_kmeans(learn_test_data, tmpdir):
    """Test for PlantCV."""
    # Create a test tmp directory
    cache_dir = tmpdir.mkdir("cache")
    training_dir = learn_test_data.kmeans_train_dir
    outfile_subset = os.path.join(str(cache_dir), "kmeansout_subset.fit")
    outfile_full = os.path.join(str(cache_dir), "kmeansout_full.fit")
    # Train full model and partial model 
    fit_subset = train_kmeans(img_dir=training_dir, prefix="kmeans_train", 
                              out_path=outfile_subset, K=5, num_imgs=3)
    fit_full = train_kmeans(img_dir=training_dir, prefix="kmeans_train", 
                            out_path=outfile_full, K=5)    
    assert os.path.exists(outfile_subset)
    assert os.path.exists(outfile_full)
    