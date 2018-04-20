Title: Linux tips
Date: 2018-04-21 00:47
Modified: 2018-04-21 00:47
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

## Diff command
```bash
diff [OPTIONS] FILE FILE
```
|Options                     |Ignore options       |
| -------------------------- | ------------------- |
|`-q` reports only different |`-B` blank line      |
|`-s` report identical       |`-b` whitespaces     |
|`-y` side by side           |`-Z` trailing spaces |
|`-N` absent as empty        |`-E` tab expansion   |
|                            |`-w` all whitespaces |


## Useful commands
```bash
du -h DIR # size of all subdirs in DIR
du -sh DIR # size of directory
du -sch DIR/* # size of everything in DIR
```
`-c` show cumulative  
`-s` show summarized size  
`-h` human readable
```bash
tar -tf FILE # list files in FILE archive
tar -tvf FILE # long list
tar -zxvf FILE # uncompress and extract for .tar.gz
tar -xvf FILE # extract for .tar
tar -cxvf FILE # compress and zip to tar.gz
```
`-t` list  
`-f FILE` use file FILE  
`-x` extract  
`-z` use gzip  
`-c` create new archive  
`-v` verbose
