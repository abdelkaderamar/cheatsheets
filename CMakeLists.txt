Cmake_Minimum_Required(VERSION 2.8)

Project ( CHEATSHEETS )

Set(CMAKE_MODULE_PATH "$ENV{HOME}/share/cmake")

Include (${CMAKE_MODULE_PATH}/UseLATEX.cmake)

Add_Latex_Document(cpp/c++14_cheatsheet.tex MANGLE_TARGET_NAMES DEFAULT_PDF)
