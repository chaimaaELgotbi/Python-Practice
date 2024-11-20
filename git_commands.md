# Git Commands Used

## Branch Operations
- `git branch dev` - Create a new branch called `dev`.
- `git checkout dev` - Switch to the `dev` branch.
- `git push origin dev` - Push the `dev` branch to the remote repository.

## Pull Requests and Merging
- `git pull origin master` - Pull remote changes from `master` into the current branch.
- `git merge dev` - Merge the `dev` branch into the current branch.
- `git push origin master` - Push the changes to the `master` branch.

## File Management
- `git add log.txt` - Stage the `log.txt` file.
- `git commit -m "Save git log output to log.txt"` - Commit changes with a message.
- `git push origin master` - Push committed changes to the `master` branch.

## Deleting Branches
- `git branch -d %USERNAME-new_featur` - Delete the local branch `%USERNAME-new_featur`.
- `git push origin --delete %USERNAME-new_featur` - Delete the remote branch `%USERNAME-new_featur`.

## Reverting
- `git revert <commit-hash>` - Revert a specific commit.