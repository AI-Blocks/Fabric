"""
Model metadeta

Metadeta format to standardize model inputs, outputs, labels and preprocessing.

Constraints: preprocessing and post processing steps are fully linear,
             and not generically based on graphs - opportunities to work
             with Azure Machine Learning.
Version: 1.0
Author: SQ Mah


CHANGELOG:

Aug 2nd, 2021
- Made model type a list to accomodate for multiple outputs
- Made confidence an explicit token in bounding boxes, instead of "P" to not
  conflate with argmax
"""

# MODEL TYPES

## Type NAME determines all other expected parameters of MODEL TYPE
## All keys are NOT OPTIONAL

object_detector_type = {
    "name": "object_detector",
    "objects": ["car", "bus", "person"]
}

classifier_type = {
    "name": "classifier",
    "objects": ["age"]
}

multiclassifier_type = {
    "name": "multiclassifier",
    "objects": ["dog", "cat"],
    "threshold": 0.7
}

# DATA TYPES

## Type NAME determines all other expected parameters of DATA TYPE
## All keys are NOT OPTIONAL
## All data

image_type = {
    "name": "image",
    "width": 500,
    "height": 500,
    "color_format": "RGB", # Num channels inferred from color_format
    "data_type": "FP32" # INT8, FP16, FP32
    "dims": ["B", "B", "H", "W"], # N: batch_size, C: channels, H: height, W: width
}

bounding_box_type = {
    "name": "bounding_box",
    "dims": ["N", ["I", "L", "P", "x_min", "y_min", "x_max", "x_min"]]
    # N: output, "I": image_id, L: labels, Conf: confidence, x_min, x_max, y_min,
    # y_max, H: height, W: width
    # Can also accomodate combination of H, W

classification_type = {
    "name": "classification",
    "dims": ["N", ["P"], 1, 1]
    # N: batch_size, "P": probabilities
}

regression_type = {
    "name": "regression",
    "dims": ["N", "V", 1, 1]
    # "V": value (i.e. age classifier gives [N, V, 1, 1])
}
## Example metadeta
### -- FACE DETECTION --


face_detection = {
    "name": "Face Detection",
    "source": "Intel",
    "metadata_version": 1.0,
    # OPTIONAL, for INCLUDED models in model zoo.
    # Suggestion for id: name+source+metadata_version
    "external_id": "4fadd3b8b75d44de02e0c60ece57f4447c19a166",
    "max_batch": -1,
    "trainable": False,
    "type": [{
        "name": "object_detector",
        "objects": ["background", "face"]
    }],
    # Additional parameters for preprocessing and postprocessing.
    "params": {
    },
    "block_inputs": [
        {
            "name": "image",
            "width": 300,
            "height": 300,
            "data_type": "FP32", # INT8, FP16, FP32
            "dims": ["B", "C", "H", "W"], # Batch size, channels, height, width
            "color_format": "BGR", # Num channels inferred from color_format
        }
    ],
    "preprocess": [
    # Will likely need to be a graph structure - opportunities to work with AML on this
        {
            "name": "divide"
            "axis": [2, 3],
            "value": 255,
        }
    ],
    "model_inputs": [
        ["B", "C", "H", "W"]
    ]
    "raw_outputs": [
        [1, 1, "N", 7]
    ],
    "postprocess": [
    # Will likely too need to be graph-based, should work with AMl on this
    ],
    "block_outputs": [
        {
            "name": "bounding_box",
            "dims": [1, 1, "N", ["I", "L", "Conf", "x_min", "y_min", "x_max", "x_min"]]
        }
    ]
}

### -- EMOTION RECOGNITION --

emotion_recognition = {
    "name": "Emotion recognition",
    "source": "Intel",
    "metadata_version": 1.0,
    # OPTIONAL, for INCLUDED models in model zoo.
    "external_id": "2F83D4DD657501AB81C727C586A6C5231349DF816",
    "max_batch": -1,
    "trainable": False,
    "type": [{
        "name": "classifier",
        "objects": ["neutral", "happy", "sad", "surprise", "anger"]
    }],
    # Additional parameters for preprocessing and postprocessing.
    "params": {
    },
    "block_inputs": [
        {
            "name": "image",
            "width": 64,
            "height": 64,
            "data_type": "FP32", # INT8, FP16, FP32
            "dims": ["B", "C", "H", "W"], # Batch size, channels, height, width
            "color_format": "BGR", # Num channels inferred from color_format
        }
    ],
    "preprocess": [
    # Will likely need to be a graph structure - opportunities to work with AML on this
        {
            "name": "normalize",
            "axis": [1],
        },
        {
            "name": "subtract_mean",
            "axis": [1],
        },
        {
            "name": "divide",
            "axis": [2, 3],
            "value": 255
        }
    ],
    "model_inputs": [
        ["B", "C", "H", "W"]
    ]
    "raw_outputs": [
        ["B", 5, 1, 1]
    ],
    "postprocess": [
    # Will likely too need to be graph-based, should work with AMl on this
    ]
    "block_outputs": [
        {
            "name": "classification",
            "dims": ["B", ["P"], 1, 1]
        }
    ]
}

### -- AGE & GENDER DETECTION --

age_recognition = {
    "name": "Age and gender recognition",
    "source": "Intel",
    "metadata_version": 1.0,
    # OPTIONAL, for INCLUDED models in model zoo.
    "external_id": "D13084F4B7ACD5DAC82B41D3435730B4DCDF89AF",
    "max_batch": -1,
    "trainable": False,
    "type": [{
        "name": "classifier",
        "objects": ["age"]
    },
    {
        "name": "classifier",
        "objects": ["female", "male"]
    }],
    # Additional parameters for preprocessing and postprocessing.
    "params": {
    },
    "block_inputs": [
        {
            "name": "image",
            "width": 62,
            "height": 62,
            "data_type": "FP32", # INT8, FP16, FP32
            "dims": ["B", "C", "H", "W"], # Batch size, channels, height, width
            "color_format": "BGR", # Num channels inferred from color_format
        }
    ],
    "preprocess": [
    # Will likely need to be a graph structure - opportunities to work with AML on this
        {
            "name": "normalize",
            "axis": [1],
        },
        {
            "name": "subtract_mean",
            "axis": [1],
        },
        {
            "name": "divide",
            "axis": [2, 3],
            "value": 255
        }
    ],
    "model_inputs": [
        ["B", "C", "H", "W"]
    ]
    "raw_outputs": [
        ["N", 1, 1, 1],
        ["N", 2, 1, 1]
    ],
    "postprocess": [
    # Will likely too need to be graph-based, should work with AMl on this
        [{
            "name": "multiply",
            "value": 100,
            "axis": 1
        }],
        []
    ],
    "block_outputs": [
        {
            "name": "classification",
            "dims": ["N", 1, "V", 1] # NEED TO VERIFY FIRST DIM IS BATCH
        },
        {
            "name": "classification",
            "dims": ["N", 1, ["P"], 1]
        }
    ]
}


data = {
    "name": "YOLO",
    "source": "Custom Vision",
    "metadata_version": 1.0,
    # OPTIONAL, for INCLUDED models in model zoo.
    "external_id": "4fadd3b8b75d44de02e0c60ece57f4447c19a166",
    "max_batch": -1,
    "trainable": False,
    "type": [{
        "name": "object_detector",
        "objects": ["person", "bus"]
    }],
    # Additional parameters for preprocessing and postprocessing.
    "params": {
        "anchors": [[0.573, 0.677], [1.87, 2.06], [3.34, 5.47], [7.88, 3.53], [9.77, 9.17]],
    },
    "block_inputs": [
        {
            "name": "image",
            "width": 500,
            "height": 500,
            "dims": ["N", "C", "H", "W"], # Batch size, channels, height, width
            "color_format": "RGB", # Num channels inferred from color_format
        }
    ],
    "preprocess": [
    # Will likely need to be a graph structure - opportunities to work with AML on this
        # {
        #     "name": "normalize",
        #     "axis": [1],
        # },
        # {
        #     "name": "subtract_mean",
        #     "axis": [1],
        # },
        {
            "name": "divide",
            "axis": [2, 3],
            "value": 255
        }
    ],
    "model_inputs": [
        ["N", 3, 500, 1000]
    ]
    "raw_outputs": [
        ["N", x, x, x]
    ],
    "postprocess": [
    # Will likely too need to be graph-based, should work with AMl on this
        {
            "name": "yolov2",
            "uses": ["anchors"]
        }
    ]
    "block_outputs": [
        {
            "name": "bounding_box",
            "dims": [1, 1, "N", ["I", "L", "C", "x_min", "y_min", "x_max", "x_min"]]
        }
    ]
}
