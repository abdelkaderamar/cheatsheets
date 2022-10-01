main_title: Bash Cheatsheet
lang: bash
#-------------------------------------------------------------------------------
#- section: Strings
#-------------------------------------------------------------------------------
title: Remove newlines from string
${str//[$'\t\r\n ']} 
#-------------------------------------------------------------------------------
title: Replace some characters by another
mod=${orig//[xyz]/_}
#-------------------------------------------------------------------------------
title: Delete line containing a pattern
sed 's/pattern/d' file.txt

#-------------------------------------------------------------------------------