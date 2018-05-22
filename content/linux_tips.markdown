Title: Linux tips
Date: 2018-04-21 00:47
Modified: 2018-04-21 13:10
Category: cheatsheets
Tags: linux, cheatsheet, command line, terminal
Authors: veyu
Summary: Helpfull linux commands and some tips

## Command line movements
```
M = C-a      A-b  C-b                      C-e
     |        |    |                        |
     v        v    v#                       v
   $ command1 --with parameter --and --flags
     ^        ^     #                       ^
     |        |                             |
R = C-u      C-w                           C-k

```

`#` Initial cursor position
`M =` Remove
`R =` Move  
`C` Ctrl

## Linux terminal keyboard combinations
`C-p` Up arrow  
`C-h` Backspace  
`C-m` Enter  
`C-z` Suspend process  

## Useful commands

### diff
```bash
diff -rNu FILE1 FILE2 # recursive unified diff
```
|Options                     |Ignore options       |
| -------------------------- | ------------------- |
|`-q` reports only different |`-B` blank line      |
|`-s` report identical files |`-b` whitespaces     |
|`-y` side by side           |`-Z` trailing spaces |
|`-N` absent files as empty  |`-E` tab expansion   |
|`-r` recursively            |`-w` all whitespaces |
|`-u` unified diff           | |

### du
```bash
du -h DIR # size of all subdirs in DIR
du -sh DIR # size of directory
du -sch DIR/* # size of everything in DIR
```
`-c` show cumulative
`-s` show summarized size
`-h` human readable

### tar
```bash
tar -tf ARCHIVE # list files in ARCHIVE
tar -tvf ARCHIVE # long list
tar -zxvf ARCHIVE # uncompress and extract tar.gz ARCHIVE
tar -xvf ARCHIVE # extract tar ARCHIVE
tar -zcvf ARCHIVE FILES # compress and zip FILES to tar.gz ARCHIVE
```
`-t` list
`-f ARCHIVE` ARCHIVE name
`-x` extract
`-z` use gzip
`-c` create new archive
`-v` verbose

### awk
```bash
awk -F'/' '{print $0,$NF}'
```
`-F` separator
`$0` whole line `$1` first column `$NF` last column

### sed
```bash
sed -i 's/regexp/dest/' [FILE]
```
`-i` in place
`-E regexp` use extended regexp

### rsync
```bash
rsync -avhz SRC DEST
```
`-r` recursive
`-l` symlinks as symlinks
`-p` preserve permissions
`-t` preserve times
`-g` preserve group
`-o` preserve owner
`-D` preserve device files and special files
`-z` compress
`-h` human readable  
`-a => -rlptgoD`

