### What is JpegOptim?

JpegOptim is a utility for optimizing JPEG files.
It provides lossless optimization (based on optimizing the Huffman tables) and "lossy" optimization based on setting a maximum quality factor.

### Installation

You need to install libjpeg first, To install JpegOptim:

Debian:

    apt-get install libjpeg-dev -y

FreeBSD:

    cd /usr/ports/graphics/jpeg
    make install clean

To install JpegOptim:

    pip install jpegoptim

### How to use it?

Following is a simple example:

    # -*- coding: utf8 -*-
    from jpegoptim import JpegOptim
    t = JpegOptim('/tmp/test.jpg', quality=80)
    t.save('/tmp/test_optim.jpg')
    t.close()
