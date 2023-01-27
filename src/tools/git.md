main_title: GIT Cheatsheet
lang: shell

#-------------------------------------------------------------------------
#- section: Working With Repositories
#-------------------------------------------------------------------------
#- subsection: Basic commands
#-------------------------------------------------------------------------
title: Local repository status
git status
#-------------------------------------------------------------------------
title: Stage a file/dir to commit list
git add <file or dir>
#-------------------------------------------------------------------------
title: Commit (with text editor)
git commit
#-------------------------------------------------------------------------
title: Commit (with commit message)
git commit -m "message"
#-------------------------------------------------------------------------
title: Send committed modification to remote repository (master branch) 
git push origin master
#-------------------------------------------------------------------------
title: Verbose mode
git command --verbose
# or 
git command -v
#-------------------------------------------------------------------------
title: Dry run
git command --dry-run
#-------------------------------------------------------------------------
title: Unstage a file
git rm --cached <file>
#-------------------------------------------------------------------------
#- section: REPOSITORY STATUS
#- subsection: Repository status
#-------------------------------------------------------------------------
title: Unpublished commits
git log origin/master..HEAD
#-------------------------------------------------------------------------
title: Display diff of unpublished commits
git diff origin/master
#-------------------------------------------------------------------------
title: Display diff of unpublished commits 
git diff origin/master..HEAD
#-------------------------------------------------------------------------
title: Remote repository information
git remote show origin
#-------------------------------------------------------------------------
#- subsection: Branch
#-------------------------------------------------------------------------
title: Create a branch
git branch <branch name>
#-------------------------------------------------------------------------
title: Switch to a branch
git checkout <branch name>
#-------------------------------------------------------------------------
Create and switch to a branch
git checkout <branch name>
#-------------------------------------------------------------------------
Delete a branch
git branch -d <branch name>
#-------------------------------------------------------------------------
title: List the local and current (starred) branches 
git branch
#-------------------------------------------------------------------------
title: Get the current branch
git rev-parse --abbrev-ref HEAD
#-------------------------------------------------------------------------
title: List remote branches
git branches -r
#-------------------------------------------------------------------------
title: List local and remotes branches
git branches -a
#-------------------------------------------------------------------------
title: Create a branch
git checkout -b [name_of_your_new_branch]
#-------------------------------------------------------------------------
title: Change working branch
git checkout [name_of_your_new_branch]
#-------------------------------------------------------------------------
title: Push the branch
git push origin [name_of_your_new_branch]
#-------------------------------------------------------------------------
title: See all branches
git branch
#-------------------------------------------------------------------------
title: Delete a branch on your local filesystem
git branch -d [name_of_your_new_branch]
#-------------------------------------------------------------------------
title: Force the deletion of local branch on your filesystem
git branch -D [name_of_your_new_branch]
#-------------------------------------------------------------------------
title: Delete the branch on github
git push origin :[name_of_your_new_branch]
#-------------------------------------------------------------------------

#- section: Working With Files

#-subsection: Commit
#-------------------------------------------------------------------------
title:Modify a commit message
git commit --amend
#-------------------------------------------------------------------------
Undo commit
git commit -m "message"
git reset HEAD~
#<< edit files as necessary >>
git add <...>
git commit -c ORIG_HEAD
#-------------------------------------------------------------------------
title: Revert one or more (n) commit and keep modifs
git reset --soft HEAD~n
#-------------------------------------------------------------------------
title: Revert one or more (n) commit and undo modifs
git reset --hard HEAD~n
#-------------------------------------------------------------------------
title: Revert one or more commits (by hashes)
git revert a867b4af 25eee4ca 0766c053
#-------------------------------------------------------------------------
title: Revert the last two commits
git revert HEAD~2..HEAD
#-------------------------------------------------------------------------
title: Revert range of commits (by hashes interval)
git revert a867b4af..0766c053
#-------------------------------------------------------------------------
title: Unstage a file
git restore --staged <added file
#-------------------------------------------------------------------------
#- subsection: Logs
#-------------------------------------------------------------------------
title:Show commit logs
git log [ -n <number>]
#-------------------------------------------------------------------------
title:Show commit diff
git diff <commit hash>~   <commit hash>
# or 
 git show <commit hash>
#-------------------------------------------------------------------------
#- section: Useful Tips
#-------------------------------------------------------------------------
#- subsection: Mirroring
#-------------------------------------------------------------------------
title: Push to multiple Git repositories
git remote add github \
      git@github.com:aamar/my-project.git 
git remote add bb \ 
      git@bitbucket.org:aamar/my-project.git 
git remote set-url ---add ---push origin \
      git@github.com:aamar/my-project.git
git remote set-url ---add ---push origin \
      git@bitbucket.org:aamar/my-project.git
#-------------------------------------------------------------------------
#- section: Github
#- subsection: Access
#-------------------------------------------------------------------------
title: Change repo URL from https to ssh (replace user by the real username)
git remote set-url origin git+ssh://git@github.com/user/reponame.git

