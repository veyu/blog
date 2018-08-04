Title: lftp cheatsheet
Date: 2018-08-04 19:04
Modified: 2018-08-04 19:04
Category: cheatsheets
Tags: lftp, ftp, tools, linux, cheatsheet, command line, terminal
Authors: veyu
Summary: Quick go through basic functions of CLI FTP client


## Connect
```bash
open -u <user>,<pass> -p 21 <server>
```

```bash
set ssl:verify-certificate no
```
### close connection
```bash
close
```

## Basic operations
### Local operations
```bash
!<cmd>
```
### Upload file from current local directory to remote
```bash
put <filename>
```
### Upload whole directory to remote
```bash
mirror -R <dir>
```
### Download whole directory from remote
```bash
mirror <dir>
```
