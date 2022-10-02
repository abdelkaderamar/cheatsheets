main_title: CMAKE Cheatsheet
lang: cmake

#------------------------------------------------------------------------------
#- section: THE BASICS
title: Project definition
project ( <NAME> )

#------------------------------------------------------------------------------

title: cmake version requirement
cmake_minimum_required( VERSION 2.8.7 )

#------------------------------------------------------------------------------

title: Add a subdirectory to cmake
add_Subdirectory(src)

#------------------------------------------------------------------------------
#- section: EXECUTABLES AND LIBRARIES
#------------------------------------------------------------------------------

title: Add library target
Add_Library ( data ${DATA_SOURCES} )

#-----------------------------------------------------------------------------

title: Add dependency libraries (for libray or an executable)
Target_Link_Libraries (test_generator
	util data fix fixml)

#-----------------------------------------------------------------------------

title: Add executable target
add_executable(${CPP_EXE} ${CPP_FILE})

#-----------------------------------------------------------------------------

title: Add an executable target for each cpp file
foreach ( CPP ${SAMPLES_SRCS} ) 
   get_filename_component(EXE ${CPP} NAME_WE ) 
   add_executable ( ${EXE} ${FILE} )
endforeach( CPP_FILE )

#-----------------------------------------------------------------------------
#- section FILES
#------------------------------------------------------------------------------

title: Get files by their names using wildcard (here all cpp files)
File ( GLOB <VAR_NAME> *.cpp )

#-----------------------------------------------------------------------------

title: Get filename without extension
get_filename_component(FNAME ${CPP} NAME_WE)

#-----------------------------------------------------------------------------

title: Get name without directory
get_filename_component(FNAME ${CPP} NAME)

#-----------------------------------------------------------------------------

title: Get file extension (longest)
get_filename_component(FEXT ${CPP} EXT)

#-----------------------------------------------------------------------------

title: Get file absolute path
get\_filename\_component(FPATH \$\{CPP\} ABSOLUTE)

#-----------------------------------------------------------------------------

title: Get file absolute path with symlinks resolved
get\_filename\_component(FPATH \$\{CPP\} REALPATH)

#-----------------------------------------------------------------------------

title: Get file directory
get_filename_component(FDIR ${CPP} DIRECTORY)

#-----------------------------------------------------------------------------
#- section: C++
#-----------------------------------------------------------------------------

title: Define C++ standard requirement of the compiler (here c++14)
set(CMAKE_CXX_STANDARD 14)
        set(CMAKE_CXX_STANDARD_REQUIRED ON)

#-----------------------------------------------------------------------------

title: Add compilation flag
add_definitions ( "-std=c++11" )

#-----------------------------------------------------------------------------

title: Add include directory
Include_Directories(${Xerces_INCLUDE_DIRS})

#-----------------------------------------------------------------------------

title: Add link directories
link_directories(<dir1> <dir2> ...)

#-----------------------------------------------------------------------------

title: Add warnings flags
if(CMAKE_COMPILER_IS_GNUCC OR CMAKE_COMPILER_IS_GNUCXX)
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wno-long-long -pedantic")
endif()
#-----------------------------------------------------------------------------
#- section: Tests
#-----------------------------------------------------------------------------
#- section: Packaging and Installation
#-----------------------------------------------------------------------------
