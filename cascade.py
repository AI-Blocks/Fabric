"""
https://github.com/jsongraph/json-graph-specification

                 |-> Age/Gender
Person -> Face ->|
                 |-> Emotions
"""


{
  "graph": {
    "directed": True,
    "type": "graph type",
    "label": "graph label",
    "metadata": {
      "description": "Get age, gender and emotions from an image."
    },
    "nodes": {
      "0": {
        "label": "Person detection", #
        "metadata": {
          "external_id": "123210",
          "source": "Intel",
          "type": {
            "name": "Object Detector"
          },
          "objects": ["person", "bus"],
          "selected": ["person"]
        }
      },
      "1": {
        "label": "Face detection",
        "metadata": {

          "type": {
            "name": "object_detector"
          },
          "user-defined": "values"
        }
      }
    },
    "edges": [
      {
        "source": "0",
        "relation": "edge relationship",
        "target": "1",
        "directed": False,
        "label": "edge label",
      }
    ]
  }
}
