Title: Git cheatsheet
Date: 2018-04-16 18:47
Modified: 2018-04-16 18:47
Category: cheatsheets
Tags: git, cheatsheet
Authors: veyu
Summary: Helpfull git snipets and commands

#### Checkout on patchset from Gerrit:
```bash
git ls-remote | grep <change number>
git pull origin <ref>
git fetch origin <ref> && git checkout FETCH_HEAD
```

#### Copy file from specific commit to new file:
```bash
git show <ref>:main.cpp > old_main.cpp
git show HEAD^:main.cpp > old_main.cpp
```

#### Patch
Create patches to specified commit:
```bash
git format-patch <ref>
```
Output to `stdout` and redirect to custom file:
```bash
git format-patch <ref> --stdout > filename.patch
```
Apply patch
```bash
git am <patch file>
```

#### Tags
Get SHA from reference (works for both: tags and branches)  
`--verify` to output error in case of wrong ref name
```bash
git rev-parse --verify <ref>
```
Tags have their own SHA which is different then commit's SHA on which they
point.  
Use `^{}` to dereference tag's SHA to commit's SHA:
```bash
git rev-parse <ref>^{}
```
Show all tags pointing on specific commit pointed by tag
```bash
git tag --points-at $(git rev-parse <tag>^{})
```
Check if branch contains tag:
```bash
git branch -a --contains <tag>
```
Create annotated tag:
```bash
git tag -a <tag name> -m "<message>"
```
Create signed tag (requires GPG key configured in git):
```bash
git tag -s <tag> <commit> -m "<message>"
```
Push single tag to remote:
```bash
git push origin <tag name>
```
Delete tag from remote:
```bash
git push origin :<tag name>
```

#### Log
Show all commits changing specific file:
```bash
git log --follow <filename>
```
Show all commits changing line 155 from file:
```bash
git log --pretty=short -u -L 155,155:<filename>
```
Git blame for lines 150 to 160 in file:
```bash
git blame -L 150,160 -- <filename>
```
Find all commits where commit message contains given regexp:
```bash
git log --grep=<regexp>
```
Find all commits where changed lines contain given regexp:
```bash
git log -G<regexp>
```
Find all commits where "phrase" occurence count has changed:
```bash
git log -S<phrase>
```

#### General
Add file to unstaged without it's content:
```bash
git add -N <filename>
```
Add part of file to staged changes:
```bash
git add --patch <filename>
git add -p <filename>
```
Add all unstaged files to staged:
```bash
git add -u
```
In case of unpacker error:
```bash
git push --no-thin origin HEAD:refs/for/master
```
