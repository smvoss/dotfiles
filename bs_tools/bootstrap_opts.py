import os


def opt_install_dir(filename, install_dir):
    expander = lambda x: x

    if "$HOME" in install_dir:
        expander = os.path.expandvars
    elif "~" in install_dir:
        expander = os.path.expanduser

    return expander(install_dir) + "/" + filename


def opt_hidden(filename, hidden):
    if hidden.lower() == "true":
        filename = os.path.dirname(filename) + "/." + os.path.basename(filename)
    return filename


BOOTSTRAP_OPTS = [
    ['install-dir', opt_install_dir],  # where to install the file
    ['hidden', opt_hidden]  # should the file be hidden (prepended with .)
]


def parse_opts(dotfile):
    opts = dict()
    opts_found = 0
    with open(dotfile) as f:
        for line in f:
            for opt in BOOTSTRAP_OPTS:
                if opt[0] in line:
                    opts[opt[0]] = line.split(opt[0])[1].strip()
                    opts_found += 1
                    break

            # once all options are found stop looping
            if opts_found == len(BOOTSTRAP_OPTS):
                break

    if not opts:
        # no options found, default to home directory and hidden
        opts = {
            "install-dir": "$HOME",
            "hidden": "true"
        }

    return opts
