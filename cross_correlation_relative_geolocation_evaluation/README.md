# Cross Correlation of Relative Geolocation Evaluation.

** Within OpenSARLab, it is best to run the notebooks on the SAR 2 profile **

Two scenes in a prepared stack have cross correlation (using https://scikit-image.org/docs/stable/api/skimage.registration.html#skimage.registration.phase_cross_correlation) applied to them. 

## Prepare environment

1. The following system libraries are required:
    - wget
    - unzip


1. Create a new conda environment (preferably via mamba) using the `opera_rtc_cross_corr.yaml` file.

    `mamba env create -f opera_rtc_cross_corr.yaml`

## Prepare Data

Scenes stacks need to be prepared. There are two ways to do this:

1. Using ASF Vertex, create a RTC stack. Once done processing, add the Hyp3 products to your Vertex download and copy the download URLs. Within `1a_prepare_data_from_hyp3.ipynb`, add the URLs to the list found in _List of Hyp3 product urls to download_. Run the notebook. This will download the stack into the proper place.

1. (Preferred) Save the stack inside AWS S3. Within `1b_get_prepared_data_from_s3.ipynb`, add the S3 path to the dictionary (with a nice short name) in the second cell. Run the notebook. This will download the stack into the proper place (`./data/s3/`).


## Analyze Data

Once data has been prepared, there are two notebook options:

1. (Preferred) `2b_check_cross_correlation_on_VVs.ipynb` which will apply the cross correlation to a stack of scenes. Basic analysis is provided.

1. `2a_check_cross_correlation_on_two_scenes.ipynb` which will apply the cross correlation to two scenes. Basic analysis is not provided. However, the scenes are displayed at each step. This could be useful if one wants a graphical display of intermediate results.

