PYSVM
=====

Introduction
------------

Simple picture verify code manager implemented by python.

Install
-------

2 ways to install **PYSVM**

1. clone the repo to your machine and run

.. code:: bash

    $ python setup.py install

2. using pip

.. code:: bash

    $ pip install -e git+https://github.com/streethacker/pysvm@0.1#egg=pysvm

Try It!
-------

Simply try **PYSVM**'s functionality!

.. code:: bash

    $ cd /your/path/to/pysvm
    $ make test
    $ python example/test.py

Then visit `http://127.0.0.1:5000/retrieve` from your webbrowser.

Quick Start
-----------

.. code:: python

    >>> from pysvm.svm import VerifyCodeManager
    >>> manager = VerifyCodeManager()
    >>> img_buf, img_hash = manager.verify_code_create()

More details, ref to `__doc__`

.. code:: python

    >>> print manager.__doc__

        Create verify code image.

        :param charset: Character collection in which verify code symbols choose
            from, default `CHARSET`.
        :param width: Width of the verify code picture, in pixels, default 120.
        :param height: Height of the verify code picture, in pixels, default 30.
        :param mode: Colour mode of the verify code picture, default 'RGB'.
        :param bg_color: A 3-elements tuple, containing (R, G, B) three integers
            which describes the background colour of the verify code picture.
        :param font_size: Font size of the verify code, default 22.
        :param font_face: Font face of the verify code, default 'Arial.ttf'.
        :param text_length: Length of characters which compose the verify code,
            default 4.
        :param noise_coverage: Probability of noise points, default 0.3.
        :param redis_dsn: Redis DSN(data source name), e.g.
            redis://[:password]@localhost:6379/0.
        :param ttl: Redis sotrage expiration time, count on seconds.
        :param max_try: Trials limit for verify code, if try counts exceeded, the
            current verify code would be expired, default 3.
        :param redis_factory: Factory function to create redis client.

    >>>
