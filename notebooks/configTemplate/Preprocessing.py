
import os


# Configuration of the parameters for the 1-Preprocessing.ipynb notebook
class Configuration:
    '''
    Configuration for the first notebook.
    Copy the configTemplate folder and define the paths to input and output data. Variables such as raw_ndvi_image_prefix may also need to be corrected if you are use a different source.
    '''
    def __init__(self):
        self.training_base_dir = '../data'
        self.training_area_fn = 'India_polygons_v3.shp'
        self.training_polygon_fn = 'india_trees_slice.shp'

        # For reading the VHR images
        self.bands = [0]
        self.raw_image_base_dir = '../data'
        self.raw_image_file_type = '.tif'
        self.raw_ndvi_image_prefix = 'wv03_20190407054002_1040010048338400_19apr07054002-m1bs-503158889080_01_p006_utm43n_b357_pan_ndvi'
        self.raw_pan_image_prefix = 'wv03_20190407054002_1040010048338400_19apr07054002-m1bs-503158889080_01_p006_utm43n_b357_pan_sub'

        # For writing the extracted images and their corresponding annotations and boundary file
        self.path_to_write = '../results'
        self.show_boundaries_during_processing = False
        self.extracted_file_type = '.png'
        self.extracted_ndvi_filename = 'ndvi'
        self.extracted_pan_filename = 'pan'
        self.extracted_annotation_filename = 'annotation'
        self.extracted_boundary_filename = 'boundary'
        

        # Path to write should be a valid directory
#         assert os.path.exists(self.path_to_write)

#         if not len(os.listdir(self.path_to_write)) == 0:
#             print('Warning: path_to_write is not empty! The old files in the directory may not be overwritten!!')
