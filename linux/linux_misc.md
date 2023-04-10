main_title: Linux Monitoring Cheatsheet
lang: bash

#---------------------------------------------------
title: Current boot logs
journalctl -b
#---------------------------------------------------
title: Reinstall a package
sudo apt --reinstall install texlive-latex-extra
#---------------------------------------------------
title: List package content
dpkg -L texlive-latex-extra
#---------------------------------------------------
title: Split a text file with (n) lines for each generated file
split  -d -l400 --additional-suffix=.txt company_list.txt "company_list-"
#---------------------------------------------------
title: Display music file tags
mp3info track.mp3    # support only id3v1
id3info track.mp3    
metaflac --list track.flac
#---------------------------------------------------

