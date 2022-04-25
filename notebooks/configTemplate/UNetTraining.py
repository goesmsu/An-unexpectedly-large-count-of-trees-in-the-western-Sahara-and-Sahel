import os

# Configuration of the parameters for the 2-UNetTraining.ipynb notebook
class Configuration:
    def __init__(self):
        # Initialize the data related variables used in the notebook
        # For reading the ndvi, pan and annotated images generated in the Preprocessing step.
        # In most cases, they will take the same value as in the config/Preprocessing.py
        self.base_dir = '../results'        # Do Not Change
        self.image_type = '.png'            # Same as self.extracted_file_type in Preprocessing.py
        self.ndvi_fn = 'ndvi'               # Do Not Change
        self.pan_fn = 'pan'                 # Do Not Change
        self.annotation_fn = 'annotation'   # Do Not Change
        self.weight_fn = 'boundary'         # Do Not Change
        
        # Patch generation; from the training areas (extracted in the last notebook), we generate fixed size patches.
        # random: a random training area is selected and a patch in extracted from a random location inside that training area. Uses a lazy stratergy i.e. batch of patches are extracted on demand.
        # sequential: training areas are selected in the given order and patches extracted from these areas sequential with a given step size. All the possible patches are returned in one call.
        self.patch_generation_stratergy = 'random' # 'random' or 'sequential'
        self.patch_size = (256,256,4) # Height * Width * (Input + Output) channels
        # # When stratergy == sequential, then you need the step_size as well
        # step_size = (128,128)
        
        # The training areas are divided into training, validation and testing set. Note that training area can have different sizes, so it doesn't guarantee that the final generated patches (when using sequential stratergy) will be in the same ratio. 
        self.test_ratio = 0.2
        self.val_ratio = 0.2
        
        # Probability with which the generated patches should be normalized 0 -> don't normalize, 1 -> normalize all
        self.normalize = 0.4 

        
        # The split of training areas into training, validation and testing set, is cached in patch_dir.
        self.patch_dir = './patches{}'.format(self.patch_size[0])               # Do Not Change
        self.frames_json = os.path.join(self.patch_dir,'frames_list.json')      # Do Not Change


        # Shape of the input data, height*width*channel; Here channels are NVDI and Pan
        self.input_shape = (256,256,2)         # Do Not Change
        self.input_image_channel = [0,1]       # Do Not Change
        self.input_label_channel = [2]         # Do Not Change
        self.input_weight_channel = [3]        # Do Not Change

        # CNN model related variables used in the notebook
        self.BATCH_SIZE = 1                        # Do Not Change
        self.NB_EPOCHS = 100

        # number of validation images to use
        self.VALID_IMG_COUNT = 192
        # maximum number of steps_per_epoch in training
        self.MAX_TRAIN_STEPS = 1000
        self.model_path = './saved_models/UNet/'   # Do Not Change

