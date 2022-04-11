# Configuration of the parameters for the 3-FinalRasterAnalysis.ipynb notebook
class Configuration:
    '''
    Configuration for the notebook where objects are predicted in the image.
    Copy the configTemplate folder and define the paths to input and output data.
    '''
    def __init__(self):
        
        # Input related variables
        self.input_image_dir = '../data'
        self.input_image_type = '.tif'
        self.ndvi_fn_st = 'wv03_20190407054002_1040010048338400_19apr07054002-m1bs-503158889080_01_p006_utm43n_b357_pan_ndvi'
        self.pan_fn_st = 'wv03_20190407054002_1040010048338400_19apr07054002-m1bs-503158889080_01_p006_utm43n_b357_pan_sub'
        self.trained_model_path = './saved_models/UNet/'

        # Output related variables
        self.output_dir = '../results'
        self.output_image_type = '.tif'
        self.output_prefix = self.ndvi_fn_st + '_predict'
        self.output_shapefile_type = '.shp'
        self.overwrite_analysed_files = True
        self.output_dtype='uint8'

        # Variables related to batches and model
        self.BATCH_SIZE = 200 # Depends upon GPU memory and WIDTH and HEIGHT (Note: Batch_size for prediction can be different then for training.
        self.WIDTH=256 # Should be same as the WIDTH used for training the model
        self.HEIGHT=256 # Should be same as the HEIGHT used for training the model
        self.STRIDE=128 #224 or 196   # STRIDE = WIDTH means no overlap, STRIDE = WIDTH/2 means 50 % overlap in prediction
