Cmake_Minimum_Required(VERSION 2.8)

Project ( CHEATSHEETS )

Set(CMAKE_MODULE_PATH "${CHEATSHEETS_SOURCE_DIR}/cmake")

Include (${CMAKE_MODULE_PATH}/UseLATEX.cmake)

set(ENV{TEXINPUTS} ".:${CHEATSHEETS_SOURCE_DIR}/sty::")

Add_Latex_Document(cpp/c++14_lang_cheatsheet.tex MANGLE_TARGET_NAMES DEFAULT_PDF)
Add_Latex_Document(cpp/c++17_lang_cheatsheet.tex MANGLE_TARGET_NAMES DEFAULT_PDF)
Add_Latex_Document(cpp/c++20_lang_cheatsheet.tex MANGLE_TARGET_NAMES DEFAULT_PDF)
#Add_Latex_Document(python/python_cheatsheet.tex MANGLE_TARGET_NAMES DEFAULT_PDF)
#Add_Latex_Document(tex/latex_cheatsheet.tex MANGLE_TARGET_NAMES DEFAULT_PDF)
#Add_Latex_Document(tools/git_cheatsheet.tex MANGLE_TARGET_NAMES DEFAULT_PDF)
#Add_Latex_Document(tools/cmake_cheatsheet.tex MANGLE_TARGET_NAMES DEFAULT_PDF)
#Add_Latex_Document(tools/makefile_cheatsheet.tex MANGLE_TARGET_NAMES DEFAULT_PDF)
#Add_Latex_Document(tools/mysql_cheatsheet.tex MANGLE_TARGET_NAMES DEFAULT_PDF)
#Add_Latex_Document(tools/linux_useful_commands.tex MANGLE_TARGET_NAMES DEFAULT_PDF)
#Add_Latex_Document(python/django_cheatsheet.tex MANGLE_TARGET_NAMES DEFAULT_PDF)
#Add_Latex_Document(bash/bash_cheatsheet.tex MANGLE_TARGET_NAMES DEFAULT_PDF)
