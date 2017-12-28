
#!/usr/bin/env bash

# This script does the required work to set up your personal GitHub Pages
# repository for deployment using Hugo. Run this script only once -- when the
# setup has been done, run the `deploy.sh` script to deploy changes and update
# your website.

# Name of the branch containing the Hugo source files.
SOURCE=hugo

msg() {
    printf "\033[1;32m :: %s\n\033[0m" "$1"
}

msg "Adding the \`public\` folder to .gitignore"
echo "public" >> .gitignore

msg "Deleting the \`master\` branch"
git branch -D master
git push origin --delete master

msg "Creating an empty, orphaned \`master\` branch"
git checkout --orphan master
git reset --hard
git commit --allow-empty -m "Initial commit on master branch"
git push origin master
git checkout $SOURCE

msg "Adding the master branch into the \`public\` folder"
rm -rf public
git worktree add -B master public origin/master
