Cmake_Minimum_Required(VERSION 2.8)
  
Project ( CHEATSHEETS )

Set(CMAKE_MODULE_PATH "${CHEATSHEETS_SOURCE_DIR}/../cmake")

Include (${CMAKE_MODULE_PATH}/UseLATEX.cmake)

set(ENV{TEXINPUTS} ".:${CHEATSHEETS_SOURCE_DIR}/../sty::")

# CPP
Set(CPP_FILES "cpp/c++17-lang_cs-colourful.tex" 
    "cpp/c++17-lang_cs-colourful-updated.tex" 
    "cpp/c++17-lang_cs-yaml.tex")
Foreach (CPP_FILE ${CPP_FILES})
    Add_Latex_Document(${CPP_FILE} MANGLE_TARGET_NAMES DEFAULT_PDF)
Endforeach(CPP_FILE)

# Add_Latex_Document(cpp/c++17-lang_cs-colourful.tex MANGLE_TARGET_NAMES DEFAULT_PDF)
# Add_Latex_Document(cpp/c++17-lang_cs-colourful-updated.tex MANGLE_TARGET_NAMES DEFAULT_PDF)
# Add_Latex_Document(cpp/c++17-lang_cs-yaml.tex MANGLE_TARGET_NAMES DEFAULT_PDF)

# MISC
Set(MISC_FILES "misc/yaml_cs-colourful.tex" "misc/yaml_cs-colourful-updated.tex")
Foreach (MISC_FILE ${MISC_FILES})
    Add_Latex_Document(${MISC_FILE} MANGLE_TARGET_NAMES DEFAULT_PDF)
Endforeach(MISC_FILE)
