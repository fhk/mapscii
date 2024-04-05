# MAPSCII

Lets create ascii maps!

Drawing inspiration from [pretty maps](https://github.com/marceloprates/prettymaps) this code creates map views in the terminal.

The goal is to be able to use this with Overture POI data.

Currently it uses static export from [here](https://figshare.com/articles/dataset/_b_City-Level_Overture_Global_Places_Dataset_b_/24031809),

And the US came from [here](https://github.com/PublicaMundi/MappingAPI/blob/master/data/geojson/us-states.json).

This code reads the data and makes some adjustment at the State level.

You can the run the main.py.

This yields:

```



                        ::.......              ::...
                        :       ..             ..
                        :       ..              :
                        :       .:              :
                        :          .......  ....:
                        :                      ..:
                        :                        :..
               .  ..   .:                        :
              .:.                                ..
                 ..                               :
                   ..                 .=          :
                    ..   .....                .:.:..
                      ...     ..             ..
                               ..        .:.
                                 .      ..
                                  :    ..
                                   ..  ..
                                      ...



```

You'll need to install - https://github.com/TheZoraiz/ascii-image-converter?tab=readme-ov-file#library-usage

As well as geopandas and matplotlib

Maybe in the future it can be tuned for mapping using - https://medium.com/analytics-vidhya/running-go-code-from-python-a65b3ae34a2d