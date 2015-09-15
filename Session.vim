let SessionLoad = 1
if &cp | set nocp | endif
let s:so_save = &so | let s:siso_save = &siso | set so=0 siso=0
let v:this_session=expand("<sfile>:p")
silent only
exe "cd " . escape(expand("<sfile>:p:h"), ' ')
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
badd +1 evolacc/__main__.py
badd +1 evolacc/simulation/simulation.py
badd +1 evolacc/action/action.py
badd +1 evolacc/unit/unit.py
badd +1 evolacc/unit/component/component.py
badd +1 evolacc/observer/observable.py
badd +1 evolacc/observer/observer.py
badd +2 evolacc/placing/placing.py
badd +1 evolacc/action/basic_actions.py
badd +1 evolacc/unit/component/genome.py
badd +1 evolacc/staticgenome/staticgenome.py
badd +20 unittests.py
badd +1 evolacc/factory/unitfactory.py
badd +1 evolacc/config/config.py
badd +1 evolacc/evolacc/evolacc.py
badd +1 evolacc/config/conflog.py
badd +1 evolacc/alterator/alterator.py
badd +1 evolacc/userdata/globals/alterators/genetic_algorithm.py
argglobal
silent! argdel *
argadd ~/Programmation/Projets/EvolAcc/EvolAcc/evolacc/__main__.py
set stal=2
edit evolacc/evolacc/evolacc.py
set splitbelow splitright
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd w
set nosplitbelow
set nosplitright
wincmd t
set winheight=1 winwidth=1
exe 'vert 1resize ' . ((&columns * 94 + 95) / 191)
exe 'vert 2resize ' . ((&columns * 96 + 95) / 191)
argglobal
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let s:l = 59 - ((37 * winheight(0) + 24) / 48)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
59
normal! 09|
lcd ~/Programmation/Projets/EvolAcc/EvolAcc
wincmd w
argglobal
edit ~/Programmation/Projets/EvolAcc/EvolAcc/evolacc/__main__.py
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let s:l = 53 - ((41 * winheight(0) + 24) / 48)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
53
normal! 022|
lcd ~/Programmation/Projets/EvolAcc/EvolAcc
wincmd w
exe 'vert 1resize ' . ((&columns * 94 + 95) / 191)
exe 'vert 2resize ' . ((&columns * 96 + 95) / 191)
tabedit ~/Programmation/Projets/EvolAcc/EvolAcc/evolacc/config/config.py
set splitbelow splitright
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd w
wincmd _ | wincmd |
split
1wincmd k
wincmd w
set nosplitbelow
set nosplitright
wincmd t
set winheight=1 winwidth=1
exe 'vert 1resize ' . ((&columns * 94 + 95) / 191)
exe '2resize ' . ((&lines * 24 + 25) / 51)
exe 'vert 2resize ' . ((&columns * 96 + 95) / 191)
exe '3resize ' . ((&lines * 23 + 25) / 51)
exe 'vert 3resize ' . ((&columns * 96 + 95) / 191)
argglobal
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let s:l = 129 - ((23 * winheight(0) + 24) / 48)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
129
normal! 022|
lcd ~/Programmation/Projets/EvolAcc/EvolAcc
wincmd w
argglobal
edit ~/Programmation/Projets/EvolAcc/EvolAcc/evolacc/config/conflog.py
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let s:l = 2 - ((1 * winheight(0) + 12) / 24)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
2
normal! 0
lcd ~/Programmation/Projets/EvolAcc/EvolAcc
wincmd w
argglobal
edit ~/Programmation/Projets/EvolAcc/EvolAcc/unittests.py
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let s:l = 19 - ((11 * winheight(0) + 11) / 23)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
19
normal! 05|
lcd ~/Programmation/Projets/EvolAcc/EvolAcc
wincmd w
exe 'vert 1resize ' . ((&columns * 94 + 95) / 191)
exe '2resize ' . ((&lines * 24 + 25) / 51)
exe 'vert 2resize ' . ((&columns * 96 + 95) / 191)
exe '3resize ' . ((&lines * 23 + 25) / 51)
exe 'vert 3resize ' . ((&columns * 96 + 95) / 191)
tabedit ~/Programmation/Projets/EvolAcc/EvolAcc/evolacc/simulation/simulation.py
set splitbelow splitright
set nosplitbelow
set nosplitright
wincmd t
set winheight=1 winwidth=1
argglobal
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let s:l = 58 - ((28 * winheight(0) + 24) / 48)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
58
normal! 029|
lcd ~/Programmation/Projets/EvolAcc/EvolAcc
tabedit ~/Programmation/Projets/EvolAcc/EvolAcc/evolacc/placing/placing.py
set splitbelow splitright
set nosplitbelow
set nosplitright
wincmd t
set winheight=1 winwidth=1
argglobal
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let s:l = 95 - ((17 * winheight(0) + 24) / 48)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
95
normal! 0
lcd ~/Programmation/Projets/EvolAcc/EvolAcc
tabedit ~/Programmation/Projets/EvolAcc/EvolAcc/evolacc/action/basic_actions.py
set splitbelow splitright
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd w
set nosplitbelow
set nosplitright
wincmd t
set winheight=1 winwidth=1
exe 'vert 1resize ' . ((&columns * 94 + 95) / 191)
exe 'vert 2resize ' . ((&columns * 96 + 95) / 191)
argglobal
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let s:l = 115 - ((39 * winheight(0) + 24) / 48)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
115
normal! 018|
lcd ~/Programmation/Projets/EvolAcc/EvolAcc
wincmd w
argglobal
edit ~/Programmation/Projets/EvolAcc/EvolAcc/evolacc/action/action.py
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let s:l = 28 - ((23 * winheight(0) + 24) / 48)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
28
normal! 019|
lcd ~/Programmation/Projets/EvolAcc/EvolAcc
wincmd w
exe 'vert 1resize ' . ((&columns * 94 + 95) / 191)
exe 'vert 2resize ' . ((&columns * 96 + 95) / 191)
tabedit ~/Programmation/Projets/EvolAcc/EvolAcc/evolacc/alterator/alterator.py
set splitbelow splitright
set nosplitbelow
set nosplitright
wincmd t
set winheight=1 winwidth=1
argglobal
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let s:l = 48 - ((29 * winheight(0) + 24) / 48)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
48
normal! 0
lcd ~/Programmation/Projets/EvolAcc/EvolAcc
tabedit ~/Programmation/Projets/EvolAcc/EvolAcc/evolacc/unit/unit.py
set splitbelow splitright
set nosplitbelow
set nosplitright
wincmd t
set winheight=1 winwidth=1
argglobal
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let s:l = 35 - ((28 * winheight(0) + 24) / 48)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
35
normal! 015|
lcd ~/Programmation/Projets/EvolAcc/EvolAcc
tabedit ~/Programmation/Projets/EvolAcc/EvolAcc/evolacc/factory/unitfactory.py
set splitbelow splitright
set nosplitbelow
set nosplitright
wincmd t
set winheight=1 winwidth=1
argglobal
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let s:l = 1 - ((0 * winheight(0) + 24) / 48)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
1
normal! 0
lcd ~/Programmation/Projets/EvolAcc/EvolAcc
tabedit ~/Programmation/Projets/EvolAcc/EvolAcc/evolacc/unit/component/component.py
set splitbelow splitright
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd w
set nosplitbelow
set nosplitright
wincmd t
set winheight=1 winwidth=1
exe 'vert 1resize ' . ((&columns * 94 + 95) / 191)
exe 'vert 2resize ' . ((&columns * 96 + 95) / 191)
argglobal
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let s:l = 1 - ((0 * winheight(0) + 24) / 48)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
1
normal! 03|
lcd ~/Programmation/Projets/EvolAcc/EvolAcc
wincmd w
argglobal
edit ~/Programmation/Projets/EvolAcc/EvolAcc/evolacc/unit/component/genome.py
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let s:l = 10 - ((8 * winheight(0) + 24) / 48)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
10
normal! 027|
lcd ~/Programmation/Projets/EvolAcc/EvolAcc
wincmd w
exe 'vert 1resize ' . ((&columns * 94 + 95) / 191)
exe 'vert 2resize ' . ((&columns * 96 + 95) / 191)
tabedit ~/Programmation/Projets/EvolAcc/EvolAcc/evolacc/staticgenome/staticgenome.py
set splitbelow splitright
set nosplitbelow
set nosplitright
wincmd t
set winheight=1 winwidth=1
argglobal
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let s:l = 1 - ((0 * winheight(0) + 24) / 48)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
1
normal! 03|
lcd ~/Programmation/Projets/EvolAcc/EvolAcc
tabedit ~/Programmation/Projets/EvolAcc/EvolAcc/evolacc/observer/observer.py
set splitbelow splitright
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd w
set nosplitbelow
set nosplitright
wincmd t
set winheight=1 winwidth=1
exe 'vert 1resize ' . ((&columns * 94 + 95) / 191)
exe 'vert 2resize ' . ((&columns * 96 + 95) / 191)
argglobal
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let s:l = 1 - ((0 * winheight(0) + 24) / 48)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
1
normal! 0
lcd ~/Programmation/Projets/EvolAcc/EvolAcc
wincmd w
argglobal
edit ~/Programmation/Projets/EvolAcc/EvolAcc/evolacc/observer/observable.py
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let s:l = 36 - ((30 * winheight(0) + 24) / 48)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
36
normal! 039|
lcd ~/Programmation/Projets/EvolAcc/EvolAcc
wincmd w
exe 'vert 1resize ' . ((&columns * 94 + 95) / 191)
exe 'vert 2resize ' . ((&columns * 96 + 95) / 191)
tabedit ~/Programmation/Projets/EvolAcc/EvolAcc/evolacc/userdata/globals/alterators/genetic_algorithm.py
set splitbelow splitright
set nosplitbelow
set nosplitright
wincmd t
set winheight=1 winwidth=1
argglobal
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let s:l = 46 - ((25 * winheight(0) + 24) / 48)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
46
normal! 039|
lcd ~/Programmation/Projets/EvolAcc/EvolAcc
tabnext 4
set stal=1
if exists('s:wipebuf')
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20 shortmess=filnxtToO
let s:sx = expand("<sfile>:p:r")."x.vim"
if file_readable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &so = s:so_save | let &siso = s:siso_save
let g:this_session = v:this_session
let g:this_obsession = v:this_session
let g:this_obsession_status = 2
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
