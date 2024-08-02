# MBUtil ZYX

MBUtil ZYX is a fork of the MBUtil utility for importing and exporting the [MBTiles](http://mbtiles.org/) format including the ZYX scheme from `vips dzsave --google`.
This fork was created and [published to PyPI](https://pypi.org/project/mbutil-zyx) because the currently published version of `mbutil` on PyPI does not include the ZYX scheme.

## Installation

Git checkout (requires git)

    git clone https://github.com/larsmaxfield/mbutil_zyx.git
    cd mbutil_zyx
    # get usage
    ./mb-util-zyx -h

Then to install the mb-util-zyx command globally:

    sudo python setup.py install
    # then you can run:
    mb-util-zyx

Python installation (requires easy_install)

    easy_install mbutil_zyx
    mb-util-zyx -h

## Usage

    $ mb-util-zyx -h
    Usage: mb-util-zyx [options] input output

    Examples:

        Export an mbtiles file to a directory of files:
        $ mb-util-zyx world.mbtiles tiles # tiles must not already exist

        Import a directory of tiles into an mbtiles file:
        $ mb-util-zyx tiles world.mbtiles # mbtiles file must not already exist

    Options:
      -h, --help            Show this help message and exit
      --scheme=SCHEME       Tiling scheme of the tiles. Default is "xyz" (z/x/y),
                            other options are "tms" which is also z/x/y
                            but uses a flipped y coordinate, and "wms" which replicates
                            the MapServer WMS TileCache directory structure "z/000/000/x/000/000/y.png"''',
                            and "zyx" which is the format vips dzsave --layout google uses.
      --image_format=FORMAT
                            The format of the image tiles, either png, jpg, webp or pbf
      --grid_callback=CALLBACK
                            Option to control JSONP callback for UTFGrid tiles. If
                            grids are not used as JSONP, you can
                            remove callbacks specifying --grid_callback=""
      --do_compression      Do mbtiles compression
      --silent              Dictate whether the operations should run silently


    Export an `mbtiles` file to files on the filesystem:

        mb-util-zyx World_Light.mbtiles adirectory


    Import a directory into a `mbtiles` file

        mb-util-zyx directory World_Light.mbtiles

## Requirements

* Python `>= 2.6`

## Metadata

MBUtil ZYX imports and exports metadata as JSON, in the root of the tile directory, as a file named `metadata.json`.

```javascript
{
    "name": "World Light",
    "description": "A Test Metadata",
    "version": "3"
}
```

## Testing

This project uses [nosetests](http://readthedocs.org/docs/nose/en/latest/) for testing. Install nosetests:

    pip install nose
or

    easy_install nose
    
Then run:

    nosetests

## See Also

* [node-mbtiles provides mbpipe](https://github.com/mapbox/node-mbtiles/wiki/Post-processing-MBTiles-with-MBPipe), a useful utility.
* [mbliberator](https://github.com/calvinmetcalf/mbliberator) a similar program but in node.

## License

BSD - see LICENSE.md

## Authors

- Tom MacWright (tmcw)
- Dane Springmeyer (springmeyer)
- Mathieu Leplatre (leplatrem)
