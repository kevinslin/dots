Overview:
---------
Dots is a portable way to manage dotfiles across multiple machines

Suffixes:
-----------
.symlink
  These files are hardlinked to the designated <target> directory after
  having the suffix striped.

  By default, this is the user's home folder.
  eg.
    .bashrc.symlink -> .bashrc


File Structure:
---------------

dotfiles
    # normal files
    vim/
      vimrc.symlink
    bash
      bashrc.symlink
    ec2
      ...
    # not uploaded
    protected
      secretrc.symlink

API:
----
dots install  # install all dotsfiles

#TODO:
dots collect <dotsfile> <program_name>  # create a new dotsfile
    eg. dots collect ~/.vimrc vim

dots list  # show existing dotsfiles

dots upload  # check for git, upload dotfiles to github

My Dotfiles
-----------
etc
  - screenrc.symlink
  - tmux.conf.symlink

python
  - pdbrc.symlink
  - pylint.custom

vim
  - gvimrc.symlink
  - vimrc.symlink
