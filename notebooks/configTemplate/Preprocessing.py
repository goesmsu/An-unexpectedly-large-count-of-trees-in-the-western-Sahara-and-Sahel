
import os


# Configuration of the parameters for the 1-Preprocessing.ipynb notebook
class Configuration:
    '''
    Configuration for the first notebook.
    Copy the configTemplate folder and define the paths to input and output data. Variables such as raw_ndvi_image_prefix may also need to be corrected if you are use a different source.
    '''
    def __init__(self):
        self.training_base_dir = '../data'       # Do Not Change
        self.training_area_fn = 'polygons.shp'   # Do Not Change
        self.training_polygon_fn = 'trees.shp'   # Do Not Change

        # For reading the VHR images
        self.bands = [0]
        self.raw_image_base_dir = '../data'      # Do Not Change
        self.raw_image_file_type = '.tif'        # Do Not Change
        self.raw_ndvi_image_prefix = 'ndvi_'     # Do Not Change
        self.raw_pan_image_prefix = 'pan_'       # Do Not Change

        # For writing the extracted images and their corresponding annotations and boundary file
        self.path_to_write = '../results'        # Do Not Change
        self.show_boundaries_during_processing = False
        self.extracted_file_type = '.png'
        self.extracted_ndvi_filename = 'ndvi'             # Do Not Change
        self.extracted_pan_filename = 'pan'               # Do Not Change
        self.extracted_annotation_filename = 'annotation' # Do Not Change
        self.extracted_boundary_filename = 'boundary'     # Do Not Change
