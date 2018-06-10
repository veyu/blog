Title: pacman cheatsheet
Date: 2018-06-10 23:47
Modified: 2018-08-04 17:37
Category: cheatsheets
Tags: Arch, pacman, package manager, cheatsheet
Authors: veyu
Summary: Helpfull pacman commands

## pacman
### General
Full system upgrade
```bash
pacman -Syu
```
List all orphans (packages not required by anything)
```bash
pacman -Qdt
```
List all packages installed explicitly and not being dependency  
Basically all packages installed by user
```bash
pacman -Qet
```

### Packages
Search for package (pattern is Extended RegEx)
```bash
pacman -Ss <pattern>
```
Search for installed package
```bash
pacman -Qs <pattern>
```
Install package/packages/group
```bash
pacman -S [repo/]<pkg1> [ [repo/]<pkg2> ... ]
```
Remove package
```bash
pacman -R <package>
```
Remove package with all dependencies (not required by anything else)
```bash
pacman -Rs <package>
```
View dependency tree of package
```bash
pactree <package>
```

### Files
Sync files database
```bash
pacman -Fy
```
Check to which package FILE belongs
```bash
pacman -Qo <filepath>
```
Check which package contains FILE
```bash
pacman -Fs <file>
pacman -Fsx <file> # file is regexp
```
List files installed by package
```bash
pacman -Ql <package>
```
