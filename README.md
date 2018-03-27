# Quickstart

```bash
git clone git@github.com:smvoss/dotfiles.git ~/.dotfiles
pushd ~/.dotfiles
chmod +x bootstrap
# Install the dotfiles by symlinking into correct location
./bootstrap --symlink
popd
```

# Installation options

Certain options may be provided as comments at the top of dotfiles. These options and their uses are as follows:

| Option Name   | Description     | Usage  |
| ------------- | --------------- | ------ |
| `install-dir` | Location to install dotfile. Will default to $HOME | `install-dir /path/to/file` |
| `hidden`      | Whether the file should be created as a hidden file | `hidden <true \| false>` |

## Example: fzf plugin

fzf plugins go in a subfolder, `~/.fzf`, and should be installed as such. This can be achieved by specifying the `install-dir` option in the file:

```
# Dotfile bootstrap arguments
#   install-dir $HOME/.fzf/shell
```

# Ignored files and folders

Not everything should be installed, so a blacklist is created. The default blacklist can be found in the bootstrap, defined as an array named `IGNORE`.
