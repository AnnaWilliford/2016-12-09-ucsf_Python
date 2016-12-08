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


7. Remotes in GitHub (30 minutes)

8. Collaborating (25 minutes)

9. Conflicts (15 minutes)



