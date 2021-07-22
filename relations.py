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