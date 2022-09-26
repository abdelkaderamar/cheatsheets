Cmake_Minimum_Required(VERSION 2.8)
  
Project ( CHEATSHEETS )

Set(CMAKE_MODULE_PATH "${CHEATSHEETS_SOURCE_DIR}/../cmake")

Include (${CMAKE_MODULE_PATH}/UseLATEX.cmake)

set(ENV{TEXINPUTS} ".:${CHEATSHEETS_SOURCE_DIR}/../sty::")

# CPP
Set(CPP_FILES 
    "cpp/tex/c++17-lang_cs-colourful.tex" 
    "cpp/tex/c++17-lang_cs-colourful-updated.tex" 
    "cpp/tex/c++17-lang_cs-cheatsheet.tex"
    "cpp/tex/c++17-lang_cs-yaml.tex")
Foreach (CPP_FILE ${CPP_FILES})
    Add_Latex_Document(${CPP_FILE} MANGLE_TARGET_NAMES DEFAULT_PDF)
Endforeach(CPP_FILE)

# MISC
Set(MISC_FILES 
    "misc/tex/yaml_cs-colourful.tex" 
    "misc/tex/yaml_cs-colourful-updated.tex"
)
Foreach (MISC_FILE ${MISC_FILES})
    Add_Latex_Document(${MISC_FILE} MANGLE_TARGET_NAMES DEFAULT_PDF)
Endforeach(MISC_FILE)
