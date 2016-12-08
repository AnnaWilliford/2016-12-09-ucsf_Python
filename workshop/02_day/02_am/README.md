# Introduction to Git

# Learning objectives

1. Automated version control (5 minutes)
    - Version control is like a structured, curated 'undo'. Better because...
        * You can control what constitutes a change
        * Can view and revert history without losing present work
        * Can have multiple histories simultaneously
    - Collaboration with version control -- allows many people to work in parallel
    - Caveats
        * Git is entirely orthagonal to Dropbox, etc.; they will not interfere with each other, and have somewhat different purposes
        * Git works best for text files, preferably ones that are not huge (i.e. not data files)
            - GitHub has a hard limit of 100MB on files, and a soft limit of 1GB on repositories.
            - [Further reading on GitHub](https://help.github.com/articles/what-is-my-disk-quota/)

2. Setting up Git (5 minutes)
    - Git commands are written as `get <verb> <parameters>`
    - Set up global configuration:
        * User name -- `git config --global user.name "Your name"`
        * User email -- `git config --global user.email "your@email.com"`
        * Colored output -- `git config --global color.ui "auto"`
        * Editor -- `git config --global core.editor "nano -w"`
    - Access help with `git <command> -h/--help`

3. Creating a repository (10 minutes)
    - Enter directory where python scripts are stored
    - Initialize repository -- `git init`
    - `ls -a` -- Everything git-related lives in the `.git` directory.
    - Print status -- `git status`
    - Caution against nesting repositories
        * _Can_ do it with submodules, but that's a very advanced topic

4. Tracking changes (20 minutes)
    - The three locations of Git:
        - Working directory -- files that are entirely local and have no backup. Anything in here that is not in Git is easily lost.
        - Staging area -- files that are ready to be added to Git, but have not been added yet
        - Repository -- snapshots of files that are within Git's system and therefore 'safe'. You have lots of powerful access to this.
    - Corresponding commands:
        - `git add` adds files that have been changed in the working directory to the staging area. 
        - `git commit` moves all files in the staging area to the repository
    - Add and commit (`commit -m 'your message'`) first file
    - `git status` -- should show there are still many "untracked" files, but the script we added isn't one of them
    - `git log` -- shows history of changes
        - Aside on paging (`less`) -- navigate with arrows, quit with `q`
    - Add some comments to the script
        - `git status` -- should show that the script has been changed
        - `git diff` -- shows exactly how you changed the file since the last commit
        - `git add` to add the change, and then `git diff` vs. `git diff --staged` to view the changes
        - `git status` to show what's staged
        - Commit the change
    - Add the remaining data files using wildcards (`git add human_chr*`) and confirm that's what we want (`git status`); then, commit
    - Options for viewing the log:
        - `--oneline`
        - `--graph`
        - `--decorate` -- show branches, HEAD, etc.
        - `--patch/-p` -- show differences
    - Review the three locations

**BREAK**

5. Exploring the history and undoing things (25 minutes)
    - Review the three locations
    - Referring to commits
        - By commit ID -- full is annoying, but minimum unambiguous head will work
        - By special name -- `HEAD`, `HEAD~1`, `HEAD~2`
    - `diff` against different commits (implied against working directory)
    - Create a change, then undo with `git checkout HEAD <file>` 
        - Note that the changes you just made are ***lost*** -- they ***cannot be recovered*** 
        - A particularly powerful and dangerous command is `git checkout -- .`, which will permanently undo all changes you've made since the last commit
        - `checkout` also affects the staged area -- changes that are staged are _not safe_
    - `checkout` an older change via `HEAD~n` or commit ID, then `git status` -- file will be staged
        - `checkout` the entire project at an earlier stage with just `git checkout <ID>` -- note the `detached HEAD state`
    - Un-stage files with `git reset <filename>` (blank indicates all).
        - The `reset` command is very powerful, but somewhat confusing. For a great explanation, see [Reset Demystified](https://git-scm.com/book/en/v2/Git-Tools-Reset-Demystified)

6. Ignoring things (5 minutes)
    - Add things to the `.gitignore` file
        - Specific files
        - Wildcards
        - Directories
    - Try `git add` on ignored files -- doesn't work! 
        - Can more safely do things like `git add .` (`.` refers to the current directory)
    - `.gitignore` file itself is tracked by git, like any other
        - If you want, you can ignore `.gitignore` itself -- this can be useful if you have computer-specific `.gitignore` files

**BREAK**

7. Remotes in GitHub (30 minutes)
    - Set up a GitHub account
    - Create a blank repository
    - `git remote add origin <URL>`
        - Test that it worked -- `git remote -v`
        - More robust test -- `git remote show origin`
        - `origin` is an arbitrary name for the remote -- you can call it whatever you want, but `origin` happens to be a very common name for your personal remote.
        - You can create multiple remotes -- we will touch on this in the next section ("Collaborating")
    - Upload changes to the repository -- `git push origin master`
        - `master` is the name of the `branch` you are on. Branches are a more advanced git feature that is covered in a different SWC lesson. All you need to know is that, unless you create any new branches, the default branch is always called `master`
    - Make a change online and commit it (via the GitHub web editor)
    - Download the changes with `git pull origin master`

8. Collaborating (35 minutes)
    - NOTE: I am diverging from the SWC materials here. Rather than using a shared repository, I would like to do the slightly more advanced but ultimately more robust and common approach of linking up multiple repositories (`fork/pull-request`)
    - Basic workflow
    - Pair up users
    - User 1:
        - Create a blank repository (Repo 1)
        - Clone (introduce `git clone`)
        - Adds some files
    - User 2:
        - Fork repository
        - Clone it
        - Make some changes
        - Push
        - Open a Pull Request
    - User 1:
        - Accept the pull request
        - Pull (to local)
        - Make some changes
        - Push
    - User 2:
        - Add User 1 as the `upstream` remote (or whatever, but `upstream` is common)
        - Pull upstream
        - Push to update origin 
    - Time-permitting, switch roles and repeat (Repo 2)

9. Conflicts (15 minutes)
    - User 1 and User 2 both modify the same files from Repo 1 and Repo 2
    - User 2 does a pull upstream
    - Inspect the conflicts
    - Resolve the conflicts by hand
        - Mention more advanced and automated ways to do this -- see [Advanced Merging](https://git-scm.com/book/en/v2/Git-Tools-Advanced-Merging)
