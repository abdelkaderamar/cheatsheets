Cmake_Minimum_Required(VERSION 2.8)
  
Project ( CHEATSHEETS )

Set(CMAKE_MODULE_PATH "${CHEATSHEETS_SOURCE_DIR}/../cmake")

Include (${CMAKE_MODULE_PATH}/UseLATEX.cmake)

set(ENV{TEXINPUTS} ".:${CHEATSHEETS_SOURCE_DIR}/../sty::")

# CPP
Add_Latex_Document(cpp/c++17-lang_cs-colourful.tex MANGLE_TARGET_NAMES DEFAULT_PDF)
Add_Latex_Document(cpp/c++17-lang_cs-colourful-updated.tex MANGLE_TARGET_NAMES DEFAULT_PDF)
Add_Latex_Document(cpp/c++17-lang_cs-yaml.tex MANGLE_TARGET_NAMES DEFAULT_PDF)

# MISC
Add_Latex_Document(misc/yaml_cs-colourful.tex MANGLE_TARGET_NAMES DEFAULT_PDF)
Add_Latex_Document(misc/yaml_cs-colourful-updated.tex MANGLE_TARGET_NAMES DEFAULT_PDF)
