#!/bin/sh

VERSION=$(<VERSION)

package() {
    python setup.py bdist_wheel
}

upload() {
    twine upload dist/"cxc_django-$VERSION-py3-none-any.whl"
}

package
upload
