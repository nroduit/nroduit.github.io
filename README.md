## Weasis Documentation Source ##

This is the repository for the [Weasis website](https://nroduit.github.io) containing the documentation for installation, configuration, and more.

### Scripts ###
setup.sh should not be used (only the first time for building the branches -structure of the repository-)

After cloning the repository, add the master branch into the \`public\` folder (subtree):
``` bash
rm -rf public
git worktree prune
git worktree add -B master public origin/master
``` 

To publish the site into the detached master branch, run deploy.sh