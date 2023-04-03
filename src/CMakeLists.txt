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
    "cpp/tex/c++17-lang_cs-yaml.tex"
    "cpp/tex/c++14-lang_cs-cheatsheet.tex"
    "cpp/tex/c++14-lang_cs-colourful-updated.tex"
    "cpp/tex/c++14-lang_cs-colourful.tex"
)
Foreach (CPP_FILE ${CPP_FILES})
    Add_Latex_Document(${CPP_FILE} MANGLE_TARGET_NAMES DEFAULT_PDF)
Endforeach(CPP_FILE)

# BASH
Set(BASH_FILES
     "bash/tex/bash_cs-cheatsheet.tex"
     "bash/tex/bash_cs-colourful.tex"
     "bash/tex/bash_cs-colourful-updated.tex"
    )
Foreach (BASH_FILE ${BASH_FILES})
    Add_Latex_Document(${BASH_FILE} MANGLE_TARGET_NAMES DEFAULT_PDF)
Endforeach(BASH_FILE)

# BOOK
Set(BOOK_FILES
     "book/tex/pragmatic_programmer_cs-cheatsheet.tex"
     "book/tex/pragmatic_programmer_cs-colourful.tex"
     "book/tex/pragmatic_programmer_cs-colourful-updated.tex"
    )
Foreach (BOOK_FILE ${BOOK_FILES})
    Add_Latex_Document(${BOOK_FILE} MANGLE_TARGET_NAMES DEFAULT_PDF)
Endforeach(BOOK_FILE)

# CSS
Set(CSS_FILES
     "css/tex/css_selector-cheatsheet.tex"
     "css/tex/css_selector-colourful.tex"
     "css/tex/css_selector-colourful-updated.tex"
    )
Foreach (CSS_FILE ${CSS_FILES})
    Add_Latex_Document(${CSS_FILE} MANGLE_TARGET_NAMES DEFAULT_PDF)
Endforeach(CSS_FILE)

# LINUX
Set(LINUX_FILES
     "linux/tex/linux_misc-cheatsheet.tex"
     "linux/tex/linux_misc-colourful.tex"
     "linux/tex/linux_misc-colourful-updated.tex"
     )
Foreach (LINUX_FILE ${LINUX_FILES})
    Add_Latex_Document(${LINUX_FILE} MANGLE_TARGET_NAMES DEFAULT_PDF)
Endforeach(LINUX_FILE)

# PYTHON
Set(PYTHON_FILES
     "python/tex/python-cheatsheet.tex"
     "python/tex/python-colourful.tex"
     "python/tex/python-colourful-updated.tex"
     "python/tex/python-libraries-cheatsheet.tex"
     "python/tex/python-libraries-colourful.tex"
     "python/tex/python-libraries-colourful-updated.tex"
     "python/tex/django-cheatsheet.tex"
     "python/tex/django-colourful.tex"
     "python/tex/django-colourful-updated.tex"
     "python/tex/python-pandas-cheatsheet.tex"
     "python/tex/python-pandas-colourful.tex"
     "python/tex/python-pandas-colourful-updated.tex"
     "python/tex/python-pip-cheatsheet.tex"
     "python/tex/python-pip-colourful.tex"
     "python/tex/python-pip-colourful-updated.tex"
     "python/tex/python-scraping-cheatsheet.tex"
     "python/tex/python-scraping-colourful.tex"
     "python/tex/python-scraping-colourful-updated.tex"
     )
Foreach (PYTHON_FILE ${PYTHON_FILES})
    Add_Latex_Document(${PYTHON_FILE} MANGLE_TARGET_NAMES DEFAULT_PDF)
Endforeach(PYTHON_FILE)

# TOOLS
Set(TOOLS_FILES
     "tools/tex/git-cheatsheet.tex"
     "tools/tex/git-colourful.tex"
     "tools/tex/git-colourful-updated.tex"
     "tools/tex/cmake-cheatsheet.tex"
     "tools/tex/cmake-colourful.tex"
     "tools/tex/cmake-colourful-updated.tex"
     )
Foreach (TOOLS_FILE ${TOOLS_FILES})
    Add_Latex_Document(${TOOLS_FILE} MANGLE_TARGET_NAMES DEFAULT_PDF)
Endforeach(TOOLS_FILE)

# MISC
Set(MISC_FILES 
    "misc/tex/yaml_cs-colourful.tex" 
    "misc/tex/yaml_cs-colourful-updated.tex"
)
Foreach (MISC_FILE ${MISC_FILES})
    Add_Latex_Document(${MISC_FILE} MANGLE_TARGET_NAMES DEFAULT_PDF)
Endforeach(MISC_FILE)
