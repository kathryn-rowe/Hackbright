# Hackbright Academy

Collection of Skills Assessments, Homework, and Lab Exercises from my Software Engineering Fellowship at Hackbright Academy.

### Setup/Installation

How to organize repos in GitHub

Make parent repository:

```sh
$ mkdir Hackbright
```
Initialize git

```sh
$ git init
```

Retrieve "move_git" file and customize sub-trees, repo names.
```sh
$ git subtree add --prefix=Skills_Assess_Lists https://github.com/kathryn-rowe/skills_assessment_lists.git master
```

Run "move_git"
```sh
$ bash move_git.sh
```

Ensure commits are commited under your name/email.
```sh
$ bash change_name.sh
```

Push to GitHub
```sh
$ git push -f
```



[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


