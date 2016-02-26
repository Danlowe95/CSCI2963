##Lesson 1:
TUTORIAL.CXX
	// A simple program that computes the square root of a number
	#include <stdio.h>
	#include <stdlib.h>
	#include <math.h>
	#include "TutorialConfig.h"
	 
	int main (int argc, char *argv[])
	{
	  if (argc < 2)
	    {
	    fprintf(stdout,"%s Version %d.%d\n",
	            argv[0],
	            Tutorial_VERSION_MAJOR,
	            Tutorial_VERSION_MINOR);
	    fprintf(stdout,"Usage: %s number\n",argv[0]);
	    return 1;
	    }
	  double inputValue = atof(argv[1]);
	  double outputValue = sqrt(inputValue);
	  fprintf(stdout,"The square root of %g is %g\n",
	          inputValue, outputValue);
	  return 0;
	}

	CMAKELISTS
	cmake_minimum_required (VERSION 2.6)
	project (Tutorial)
	# The version number.
	set (Tutorial_VERSION_MAJOR 1)
	set (Tutorial_VERSION_MINOR 0)
	 
	# configure a header file to pass some of the CMake settings
	# to the source code
	configure_file (
	  "${PROJECT_SOURCE_DIR}/TutorialConfig.h.in"
	  "${PROJECT_BINARY_DIR}/TutorialConfig.h"
	  )
	 
	# add the binary tree to the search path for include files
	# so that we will find TutorialConfig.h
	include_directories("${PROJECT_BINARY_DIR}")
	 
	# add the executable
	add_executable(Tutorial tutorial.cxx)

#Lesson 2

	// A simple program that computes the square root of a number
	#include <stdio.h>
	#include <stdlib.h>
	#include <math.h>
	#include "TutorialConfig.h"
	#ifdef USE_MYMATH
	#include "MathFunctions.h"
	#endif
	 
	int main (int argc, char *argv[])
	{
	  if (argc < 2)
	    {
	    fprintf(stdout,"%s Version %d.%d\n", argv[0],
	            Tutorial_VERSION_MAJOR,
	            Tutorial_VERSION_MINOR);
	    fprintf(stdout,"Usage: %s number\n",argv[0]);
	    return 1;
	    }
	 
	  double inputValue = atof(argv[1]);
	 
	#ifdef USE_MYMATH
	  double outputValue = mysqrt(inputValue);
	#else
	  double outputValue = sqrt(inputValue);
	#endif
	 
	  fprintf(stdout,"The square root of %g is %g\n",
	          inputValue, outputValue);
	  return 0;
	}

	cmake_minimum_required (VERSION 2.6)
	project (Tutorial)
	# The version number.
	set (Tutorial_VERSION_MAJOR 1)
	set (Tutorial_VERSION_MINOR 0)
	 
	# configure a header file to pass some of the CMake settings
	# to the source code
	configure_file (
	  "${PROJECT_SOURCE_DIR}/TutorialConfig.h.in"
	  "${PROJECT_BINARY_DIR}/TutorialConfig.h"
	  )
	 
	# add the binary tree to the search path for include files
	# so that we will find TutorialConfig.h
	include_directories("${PROJECT_BINARY_DIR}")
	 
	 # should we use our own math functions?
	option (USE_MYMATH 
	        "Use tutorial provided math implementation" ON) 


	add_library(MathFunctions mysqrt.cxx)
	# should we use our own math functions?
	option (USE_MYMATH 
	        "Use tutorial provided math implementation" ON) 
	        
	# add the MathFunctions library?
	#
	if (USE_MYMATH)
	  include_directories ("${PROJECT_SOURCE_DIR}/MathFunctions")
	  add_subdirectory (MathFunctions)
	  set (EXTRA_LIBS ${EXTRA_LIBS} MathFunctions)
	endif (USE_MYMATH)
	 
	# add the executable
	add_executable (Tutorial tutorial.cxx)
	target_link_libraries (Tutorial  ${EXTRA_LIBS})

#Lesson 3

#Lesson 4

#Lesson 5