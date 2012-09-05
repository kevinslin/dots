import os

__all__ = ("_collect_files",)

def _collect_files(suffix, ignore_dirs = []):
    """
    Collect all files by searching recursively via current directory.
    Will ignore directories specified by ignore_dirs
    @params:
        suffix - suffix to search for
        ignore_dirs - list of directories to ignore
    @return:
        List of tuples (path, [files])
    eg.
        [(path, [ foo.symlink]), (...),...]
    """
    out = []
    walker = os.walk(".")
    for path, directory, files in walker:
        for inum, dname in enumerate(directory):
            # filter out all unwanted directories
            if (dname in ignore_dirs): del directory[inum]
        # gets all files that match the suffix
        match = filter(lambda x: x.endswith(suffix), files)
        # filter out unwanted suffix
        if (match):
            out.append((path, match))
    return out

def get_symlinks():
    """
    Get all files ending in .symlink
    @return:
    List of tuples (path, [files])
    eg.
    [(path, [ foo.symlink]), (...),...]
    """
    res = _collect_files("symlink")
    return res

