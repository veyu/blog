Title: Vim cheatsheet
Date: 2018-04-24 17:20
Modified: 2018-04-26 00:02
Category: cheatsheets
Tags: vim, cheatsheet
Authors: veyu
Summary: Vim commands and shortcuts


## CLI commands
```bash
vim -O FILE FILE... # open files in v-split
vim -p FILE FILE... # open files in tabs
vim FILE +10 # set cursor in 10 line; no number -> EOF
vimdiff FILE FILE # diff files
```

---

## Inside Vim
### Editing
#### History
`U` undo  
`C-r` redo  

#### Lines
`J` append next line to current one  

#### Sed
```vim
:%s/regex/str/gci
```
`///g` globally
`///c` confirmation required
`///i` case insensitive

### Folding
```vim
:set foldmethod=[manual|indent|syntax|expr|marker|diff]
:set fdm=manual " set to manual folding
```

#### Cursor location
Action | One fold | Recursively
---    | ---      | ---
create | ``zf``   |
open   | ``zo``   | ``ZO``
close  | ``zc``   | ``ZC``
toggle | ``za``   | ``ZA``
delete | ``zd``   |

#### File-wise
``zr`` open one level in bufferwise  
``zm`` close one level bufferwise  
``zR`` open all levels  
``zM`` close all levels  

### Navigation
#### Content specific
`%` jump to matching bracket  

#### File specific
`gg` beginning of file  
`G` EOF  
`9gg` jump to line no 9  

#### Marks
`mx` mark cursor location with **x** mark  
`'x` jump to line of **x** mark  
`` `x`` jump to **x** mark location  
``''`` jump to line of previous cursor location  
` `` ` jump to previous cursor location  

### Syntax
```vim
:set syntax=html
```

### Plugins
#### jedi-vim
`C-space` completion  
`\g` goto assignment of element under cursor  
`\d` goto definition of element under cursor  
`\n` show all usages of element under cursor in current file  
`\n` refactor element under cursor  
`K` show docs of element under cursor  
`:Pyimport os` open module *os*
