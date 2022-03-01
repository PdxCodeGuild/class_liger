# Submitting Your Work

## Pushing to GitHub

The first step to submitting your work is to push your code to GitHub. In your terminal navigate to your lab folder, make sure you are on your branch `git branch --show-current` and execute the following commands. If you are not on your branch, you can change branches with the `git checkout branch_name` command. Just replace branch_name with your name.

1. `git pull`
2. `git add lab_name.py` (replace lab_name with the name of your solution.)
3. `git commit -m "added lab_name solution"`
4. `git push`
5. You should be able to see your commit in GitHub under your branch.

## Creating a Pull Request

1. On github select the `Pull Requests` tab
   ![Pull Requests](https://i.ibb.co/qRVB9Hx/pull-requests.png)
2. Click on `New pull request`
   ![New Request](https://i.ibb.co/Bqd57rk/new-request.png)
3. Select your branch
   ![Select Branch](https://i.ibb.co/zVSJ8Nx/select-branch.png)
4. Click on `Create pull request`
   ![Create Request](https://i.ibb.co/xGL2sLG/create-request.png)
5. Leave a comment and click `Create pull request`
   ![Leave Comment](https://i.ibb.co/30j0mrL/leave-comment.png)
6. Thats it! The instructor can now go review your pull request. If it meets the requirements of the assignment your code will be merged in.

## Getting the latest code from github

If you would like to get any changes that have occurred on the main branch and merge them with your own, you can run the `git merge main` command in your terminal.
