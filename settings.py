import os

# Options
# Files in here won't be symlinked. Assumes unique directory names
IGNORE = (
    'priv',
)
# Symlinked files will be placed in this directory
TARGET =  os.path.expanduser('~')
# Don't overwrite local files
SKIP_ALL = False
