# Intro to GitHub

## I want to create a new repository
Manually go onto your profile, click the + button at the top right, and click either import or create new repository. We generally have been adding the MIT license to our public repositories (cupcakes and coding).

## I want to clone a repository and/or update
Cloning means:
- `git clone <https://github.com/username/example.git>`: you can find url on the repository you want to clone's home page. Click the green button that says "Clone or download" to do this
- `git pull origin master`: updates your local clone copy and deleting all the changes you made but didn't commit. perform this command while in your local clone folder. `git fetch origin`: is less aggressive and will update your file with updates remote changes, without deleting the ones you've made

## I want to make changes to a repository locally, and push them to my origin/master repository

- `git status`: will tell you if there are files/ file changes in your working directory that have not been committed to your repository
- `git add .`: start adding changes to the repository. You can add specific files but replacing . with the file. to undo this, `git reset` will undo changes
- `git status`: will tell you if changes have been staged - currently a git add does not make permanent changes
- `git commit -m "any message"`: commit these changes to your repository
- `git push`: commit to remote repository

example workflow:
```
➜  Kistler_Utilities git:(master) git status
On branch master
Your branch is up-to-date with 'origin/master'.
Untracked files:
  (use "git add <file>..." to include in what will be committed)

	how_tos/

nothing added to commit but untracked files present (use "git add" to track)
➜  Kistler_Utilities git:(master) ✗ git add .
➜  Kistler_Utilities git:(master) ✗ git status
On branch master
Your branch is up-to-date with 'origin/master'.
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	new file:   how_tos/JupyterNotebook_onAWS.md
	new file:   how_tos/RStudio_onAWS.md
	new file:   how_tos/Reflow_basic.md

➜  Kistler_Utilities git:(master) ✗ git commit -m "new files"
[master 229d4f2] new files
 3 files changed, 179 insertions(+)
 create mode 100644 how_tos/JupyterNotebook_onAWS.md
 create mode 100644 how_tos/RStudio_onAWS.md
 create mode 100644 how_tos/Reflow_basic.md
➜  Kistler_Utilities git:(master) git status
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)
nothing to commit, working tree clean
➜  Kistler_Utilities git:(master) git push
Counting objects: 6, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (6/6), done.
Writing objects: 100% (6/6), 3.51 KiB | 3.51 MiB/s, done.
Total 6 (delta 0), reused 0 (delta 0)
To https://github.com/kalanir/Kistler_Utilities.git
   9e7c37b..229d4f2  master -> master
➜  Kistler_Utilities git:(master) git status
On branch master
Your branch is up-to-date with 'origin/master'.
nothing to commit, working tree clean

```


## I want to make a branch off of a repository, and make changes, and push that branch
- `git checkout -b <branch name>`: creates a new branch and switches to that branch. you should be able to see a change in the path you are working in.
- `git status`: see if there are files to commit that are not on the branch
- `git add .` or `git add <file name>`: to start adding changes to branch
- `git commit -m "message"`: to commit changes to branch
- `git push origin <branch name>`: pushes branch to repository. Go online to decide whether to merge new branch to master if you have the permission to.
- `git checkout <branch name`: allows you to switch between branches

example:
```
➜  fakerepo git:(master) touch kalani.txt
➜  fakerepo git:(master) ✗ git status
On branch master
Your branch is up-to-date with 'origin/master'.
Untracked files:
  (use "git add <file>..." to include in what will be committed)

	kalani.txt

nothing added to commit but untracked files present (use "git add" to track)
➜  fakerepo git:(master) ✗ git checkout -b 20181025_branch
Switched to a new branch '20181025_branch'
➜  fakerepo git:(20181025_branch) ✗ git branch
* 20181025_branch
  master
➜  fakerepo git:(20181025_branch) ✗ git status
On branch 20181025_branch
Untracked files:
  (use "git add <file>..." to include in what will be committed)

	kalani.txt

nothing added to commit but untracked files present (use "git add" to track)
➜  fakerepo git:(20181025_branch) ✗ git add kalani.txt
➜  fakerepo git:(20181025_branch) ✗ git status
On branch 20181025_branch
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	new file:   kalani.txt

➜  fakerepo git:(20181025_branch) ✗ git commit -m "branch practice"
[20181025_branch e119344] branch practice
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 kalani.txt
➜  fakerepo git:(20181025_branch) git push origin 20181025_branch
Counting objects: 3, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 273 bytes | 273.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
remote:
remote: Create a pull request for '20181025_branch' on GitHub by visiting:
remote:      https://github.com/kalanir/fakerepo/pull/new/20181025_branch
remote:
To https://github.com/kalanir/fakerepo.git
 * [new branch]      20181025_branch -> 20181025_branch
➜  fakerepo git:(20181025_branch) git checkout master
Switched to branch 'master'
Your branch is up-to-date with 'origin/master'.
➜  fakerepo git:(master) git checkout 20181025_branch
Switched to branch '20181025_branch'
```
## I want to merge my branch to origin/master
- Go online and you will see a merge request
- command line methods to do this, will post later
