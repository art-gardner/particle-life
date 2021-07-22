data = {
    "Red":
        {"colour": (255, 0, 0),
         "relations":
             {"Red":
                  {"attraction": -0.1,
                   "range": 300},
              "Blue":
                  {"attraction": 1,
                   "range": 150},
              "Green":
                  {"attraction": -2,
                   "range": 100}
              }},
    "Blue":
        {"colour": (0, 0, 255),
         "relations":
             {"Red":
                  {"attraction": 0.1,
                   "range": 150},
              "Blue":
                  {"attraction": 1,
                   "range": 50},
              "Green":
                  {"attraction": 0.1,
                   "range": 150}
              }},
    "Green":
        {"colour": (0, 255, 0),
         "relations":
             {"Red":
                  {"attraction": 1,
                   "range": 50},
              "Blue":
                  {"attraction": 1,
                   "range": 150},
              "Green":
                  {"attraction": 0.1,
                   "range": 150}
              }}
}

hexes = {'Blue': {'colour': (0, 0, 255),
          'relations': {'Blue': {'attraction': 1, 'range': 96},
                        'Green': {'attraction': 1, 'range': 140},
                        'Red': {'attraction': 1, 'range': 75}}},
 'Green': {'colour': (0, 255, 0),
           'relations': {'Blue': {'attraction': -1, 'range': 78},
                         'Green': {'attraction': 1, 'range': 121},
                         'Red': {'attraction': 1, 'range': 131}}},
 'Red': {'colour': (255, 0, 0),
         'relations': {'Blue': {'attraction': -1, 'range': 107},
                       'Green': {'attraction': 1, 'range': 141},
                       'Red': {'attraction': -1, 'range': 104}}}}

nuclei = {'Blue': {'colour': (0, 0, 255),
          'relations': {'Blue': {'attraction': -0.03, 'range': 148},
                        'Green': {'attraction': -0.55, 'range': 98},
                        'Purple': {'attraction': 0.07, 'range': 133},
                        'Red': {'attraction': -0.49, 'range': 149},
                        'Yellow': {'attraction': 0.57, 'range': 147}}},
 'Green': {'colour': (0, 255, 0),
           'relations': {'Blue': {'attraction': 0.41, 'range': 76},
                         'Green': {'attraction': 0.42, 'range': 111},
                         'Purple': {'attraction': 0.36, 'range': 86},
                         'Red': {'attraction': -0.15, 'range': 97},
                         'Yellow': {'attraction': -0.67, 'range': 120}}},
 'Purple': {'colour': (255, 0, 255),
            'relations': {'Blue': {'attraction': 0.13, 'range': 120},
                          'Green': {'attraction': -0.81, 'range': 130},
                          'Purple': {'attraction': -0.5, 'range': 115},
                          'Red': {'attraction': 0.01, 'range': 132},
                          'Yellow': {'attraction': -0.98, 'range': 128}}},
 'Red': {'colour': (255, 0, 0),
         'relations': {'Blue': {'attraction': 0.58, 'range': 146},
                       'Green': {'attraction': 0.95, 'range': 87},
                       'Purple': {'attraction': -0.4, 'range': 91},
                       'Red': {'attraction': -0.18, 'range': 118},
                       'Yellow': {'attraction': 0.62, 'range': 123}}},
 'Yellow': {'colour': (255, 255, 0),
            'relations': {'Blue': {'attraction': -0.51, 'range': 136},
                          'Green': {'attraction': -0.46, 'range': 121},
                          'Purple': {'attraction': -0.45, 'range': 104},
                          'Red': {'attraction': -0.5, 'range': 150},
                          'Yellow': {'attraction': -0.18, 'range': 113}}}}
runners = {'Blue': {'colour': (0, 0, 255),
          'relations': {'Blue': {'attraction': -0.3, 'range': 148},
                        'Cyan': {'attraction': 0.27, 'range': 137},
                        'Green': {'attraction': 0.18, 'range': 80},
                        'Purple': {'attraction': -0.66, 'range': 88},
                        'Red': {'attraction': -0.69, 'range': 145},
                        'Yellow': {'attraction': -0.58, 'range': 118}}},
 'Cyan': {'colour': (0, 255, 255),
          'relations': {'Blue': {'attraction': -0.67, 'range': 112},
                        'Cyan': {'attraction': -0.42, 'range': 116},
                        'Green': {'attraction': -0.21, 'range': 77},
                        'Purple': {'attraction': 0.17, 'range': 125},
                        'Red': {'attraction': 0.2, 'range': 132},
                        'Yellow': {'attraction': 0.56, 'range': 133}}},
 'Green': {'colour': (0, 255, 0),
           'relations': {'Blue': {'attraction': 0.95, 'range': 128},
                         'Cyan': {'attraction': -0.25, 'range': 126},
                         'Green': {'attraction': -0.35, 'range': 83},
                         'Purple': {'attraction': -0.69, 'range': 84},
                         'Red': {'attraction': -0.67, 'range': 113},
                         'Yellow': {'attraction': -0.67, 'range': 133}}},
 'Purple': {'colour': (255, 0, 255),
            'relations': {'Blue': {'attraction': 0.37, 'range': 134},
                          'Cyan': {'attraction': -0.37, 'range': 132},
                          'Green': {'attraction': 0.38, 'range': 86},
                          'Purple': {'attraction': 0.43, 'range': 140},
                          'Red': {'attraction': -0.22, 'range': 140},
                          'Yellow': {'attraction': -0.69, 'range': 130}}},
 'Red': {'colour': (255, 0, 0),
         'relations': {'Blue': {'attraction': -0.15, 'range': 122},
                       'Cyan': {'attraction': 0.02, 'range': 146},
                       'Green': {'attraction': -1.0, 'range': 121},
                       'Purple': {'attraction': -0.1, 'range': 81},
                       'Red': {'attraction': -0.79, 'range': 109},
                       'Yellow': {'attraction': 0.65, 'range': 131}}},
 'Yellow': {'colour': (255, 255, 0),
            'relations': {'Blue': {'attraction': 0.45, 'range': 110},
                          'Cyan': {'attraction': 0.12, 'range': 140},
                          'Green': {'attraction': 0.16, 'range': 79},
                          'Purple': {'attraction': 0.87, 'range': 146},
                          'Red': {'attraction': 0.41, 'range': 135},
                          'Yellow': {'attraction': 0.52, 'range': 80}}}}