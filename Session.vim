let SessionLoad = 1
let s:so_save = &g:so | let s:siso_save = &g:siso | setg so=0 siso=0 | setl so=-1 siso=-1
let v:this_session=expand("<sfile>:p")
silent only
silent tabonly
cd ~/Performance-optimization-python
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
let s:shortmess_save = &shortmess
if &shortmess =~ 'A'
  set shortmess=aoOA
else
  set shortmess=aoO
endif
badd +50 ~/DataEng/multi_processing_python/single_module.py
badd +37 ~/DataEng/hw/report.py
badd +1 ~/DataEng/multi_processing_python/README.md
badd +33 ~/DataEng/hw/direct_wordcount.py
badd +11 ~/.config/lvim/config.lua
badd +65 baseline.py
badd +10 ~/DataEng/multi_processing_python/main.py
badd +25 main.py
badd +1 ~/DataEng/multi_processing_python/test_sort_speed.py
badd +9 ~/DataEng/hw/multi_processing.py
badd +11 ~/DataEng/multi_processing_python/On_sorting_time.md
badd +2 ~/DataEng/multi_processing_python/test_with_as.py
badd +37 ~/DataEng/hw/multi_processing16g.py
badd +29 ~/DataEng/hw/single_process16g.py
badd +28 ~/DataEng/hw/multi_wordcount.py
argglobal
%argdel
tabnew +setlocal\ bufhidden=wipe
tabrewind
edit ~/DataEng/multi_processing_python/test_sort_speed.py
let s:save_splitbelow = &splitbelow
let s:save_splitright = &splitright
set splitbelow splitright
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd w
wincmd _ | wincmd |
split
wincmd _ | wincmd |
split
2wincmd k
wincmd w
wincmd w
let &splitbelow = s:save_splitbelow
let &splitright = s:save_splitright
wincmd t
let s:save_winminheight = &winminheight
let s:save_winminwidth = &winminwidth
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
exe 'vert 1resize ' . ((&columns * 87 + 86) / 173)
exe '2resize ' . ((&lines * 14 + 23) / 46)
exe 'vert 2resize ' . ((&columns * 85 + 86) / 173)
exe '3resize ' . ((&lines * 14 + 23) / 46)
exe 'vert 3resize ' . ((&columns * 85 + 86) / 173)
exe '4resize ' . ((&lines * 13 + 23) / 46)
exe 'vert 4resize ' . ((&columns * 85 + 86) / 173)
argglobal
balt ~/DataEng/multi_processing_python/main.py
setlocal fdm=manual
setlocal fde=
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let &fdl = &fdl
let s:l = 1 - ((0 * winheight(0) + 21) / 42)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 1
normal! 0
lcd ~/DataEng/multi_processing_python
wincmd w
argglobal
if bufexists(fnamemodify("~/DataEng/multi_processing_python/single_module.py", ":p")) | buffer ~/DataEng/multi_processing_python/single_module.py | else | edit ~/DataEng/multi_processing_python/single_module.py | endif
if &buftype ==# 'terminal'
  silent file ~/DataEng/multi_processing_python/single_module.py
endif
balt ~/DataEng/multi_processing_python/test_sort_speed.py
setlocal fdm=manual
setlocal fde=
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let &fdl = &fdl
let s:l = 1 - ((0 * winheight(0) + 6) / 13)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 1
normal! 0
lcd ~/DataEng/multi_processing_python
wincmd w
argglobal
if bufexists(fnamemodify("~/DataEng/hw/direct_wordcount.py", ":p")) | buffer ~/DataEng/hw/direct_wordcount.py | else | edit ~/DataEng/hw/direct_wordcount.py | endif
if &buftype ==# 'terminal'
  silent file ~/DataEng/hw/direct_wordcount.py
endif
balt ~/Performance-optimization-python/baseline.py
setlocal fdm=manual
setlocal fde=
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let &fdl = &fdl
let s:l = 7 - ((6 * winheight(0) + 6) / 13)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 7
normal! 02|
lcd ~/DataEng/hw
wincmd w
argglobal
if bufexists(fnamemodify("~/DataEng/multi_processing_python/single_module.py", ":p")) | buffer ~/DataEng/multi_processing_python/single_module.py | else | edit ~/DataEng/multi_processing_python/single_module.py | endif
if &buftype ==# 'terminal'
  silent file ~/DataEng/multi_processing_python/single_module.py
endif
balt ~/Performance-optimization-python/main.py
setlocal fdm=manual
setlocal fde=
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let &fdl = &fdl
let s:l = 28 - ((5 * winheight(0) + 6) / 12)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 28
normal! 0
lcd ~/DataEng/multi_processing_python
wincmd w
exe 'vert 1resize ' . ((&columns * 87 + 86) / 173)
exe '2resize ' . ((&lines * 14 + 23) / 46)
exe 'vert 2resize ' . ((&columns * 85 + 86) / 173)
exe '3resize ' . ((&lines * 14 + 23) / 46)
exe 'vert 3resize ' . ((&columns * 85 + 86) / 173)
exe '4resize ' . ((&lines * 13 + 23) / 46)
exe 'vert 4resize ' . ((&columns * 85 + 86) / 173)
tabnext
edit ~/.config/lvim/config.lua
let s:save_splitbelow = &splitbelow
let s:save_splitright = &splitright
set splitbelow splitright
wincmd _ | wincmd |
vsplit
wincmd _ | wincmd |
vsplit
2wincmd h
wincmd w
wincmd w
let &splitbelow = s:save_splitbelow
let &splitright = s:save_splitright
wincmd t
let s:save_winminheight = &winminheight
let s:save_winminwidth = &winminwidth
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
exe 'vert 1resize ' . ((&columns * 90 + 86) / 173)
exe 'vert 2resize ' . ((&columns * 21 + 86) / 173)
exe 'vert 3resize ' . ((&columns * 60 + 86) / 173)
argglobal
setlocal fdm=manual
setlocal fde=
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let &fdl = &fdl
let s:l = 1 - ((0 * winheight(0) + 21) / 42)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 1
normal! 0
lcd ~/DataEng/multi_processing_python
wincmd w
argglobal
if bufexists(fnamemodify("~/DataEng/hw/single_process16g.py", ":p")) | buffer ~/DataEng/hw/single_process16g.py | else | edit ~/DataEng/hw/single_process16g.py | endif
if &buftype ==# 'terminal'
  silent file ~/DataEng/hw/single_process16g.py
endif
balt ~/DataEng/hw/direct_wordcount.py
setlocal fdm=manual
setlocal fde=
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let &fdl = &fdl
let s:l = 29 - ((18 * winheight(0) + 21) / 42)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 29
normal! 06|
lcd ~/DataEng/hw
wincmd w
argglobal
if bufexists(fnamemodify("~/DataEng/hw/direct_wordcount.py", ":p")) | buffer ~/DataEng/hw/direct_wordcount.py | else | edit ~/DataEng/hw/direct_wordcount.py | endif
if &buftype ==# 'terminal'
  silent file ~/DataEng/hw/direct_wordcount.py
endif
balt ~/DataEng/hw/multi_wordcount.py
setlocal fdm=manual
setlocal fde=
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let &fdl = &fdl
let s:l = 33 - ((30 * winheight(0) + 21) / 42)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 33
normal! 021|
lcd ~/DataEng/hw
wincmd w
exe 'vert 1resize ' . ((&columns * 90 + 86) / 173)
exe 'vert 2resize ' . ((&columns * 21 + 86) / 173)
exe 'vert 3resize ' . ((&columns * 60 + 86) / 173)
tabnext 2
if exists('s:wipebuf') && len(win_findbuf(s:wipebuf)) == 0 && getbufvar(s:wipebuf, '&buftype') isnot# 'terminal'
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20
let &shortmess = s:shortmess_save
let &winminheight = s:save_winminheight
let &winminwidth = s:save_winminwidth
let s:sx = expand("<sfile>:p:r")."x.vim"
if filereadable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &g:so = s:so_save | let &g:siso = s:siso_save
set hlsearch
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
