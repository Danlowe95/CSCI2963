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
forgot to take code sample
#Lesson 4
forgot to take code sample
#Lesson 5
	cmake_minimum_required (VERSION 2.6)
	project (Tutorial)
	include(CTest)
	 
	# The version number.
	set (Tutorial_VERSION_MAJOR 1)
	set (Tutorial_VERSION_MINOR 0)
	 
	# does this system provide the log and exp functions?
	include (${CMAKE_ROOT}/Modules/CheckFunctionExists.cmake)
	 
	check_function_exists (log HAVE_LOG)
	check_function_exists (exp HAVE_EXP)
	 
	# should we use our own math functions
	option(USE_MYMATH 
	  "Use tutorial provided math implementation" ON)
	 
	# configure a header file to pass some of the CMake settings
	# to the source code
	configure_file (
	  "${PROJECT_SOURCE_DIR}/TutorialConfig.h.in"
	  "${PROJECT_BINARY_DIR}/TutorialConfig.h"
	  )
	 
	# add the binary tree to the search path for include files
	# so that we will find TutorialConfig.h
	include_directories ("${PROJECT_BINARY_DIR}")
	 
	# add the MathFunctions library?
	if (USE_MYMATH)
	  include_directories ("${PROJECT_SOURCE_DIR}/MathFunctions")
	  add_subdirectory (MathFunctions)
	  set (EXTRA_LIBS ${EXTRA_LIBS} MathFunctions)
	endif (USE_MYMATH)
	 
	# add the executable
	add_executable (Tutorial tutorial.cxx)
	target_link_libraries (Tutorial  ${EXTRA_LIBS})
	 
	# add the install targets
	install (TARGETS Tutorial DESTINATION bin)
	install (FILES "${PROJECT_BINARY_DIR}/TutorialConfig.h"        
	         DESTINATION include)
	 
	# does the application run
	add_test (TutorialRuns Tutorial 25)
	 
	# does the usage message work?
	add_test (TutorialUsage Tutorial)
	set_tests_properties (TutorialUsage
	  PROPERTIES 
	  PASS_REGULAR_EXPRESSION "Usage:.*number"
	  )
	 
	 
	#define a macro to simplify adding tests
	macro (do_test arg result)
	  add_test (TutorialComp${arg} Tutorial ${arg})
	  set_tests_properties (TutorialComp${arg}
	    PROPERTIES PASS_REGULAR_EXPRESSION ${result}
	    )
	endmacro (do_test)
	 
	# do a bunch of result based tests
	do_test (4 "4 is 2")
	do_test (9 "9 is 3")
	do_test (5 "5 is 2.236")
	do_test (7 "7 is 2.645")
	do_test (25 "25 is 5")
	do_test (-25 "-25 is 0")
	do_test (0.0001 "0.0001 is 0.01")

	double mysqrt(double num){

		// if we have both log and exp then use them
	#if defined (HAVE_LOG) && defined (HAVE_EXP)
	  result = exp(log(x)*0.5);
	#else // otherwise use an iterative approach
		if(num >= 0) 
			{ 
			float x = num; 
			int i; 
			for(i = 0; i < 20; i ++) 
			{ 
			x = (((x * x) + num) / (2 * x)); 
			} 
			return x; 
			} 
			#endif
			return 0; 
			}

	# first we add the executable that generates the table
	add_executable(MakeTable MakeTable.cxx)
	# add the command to generate the source code
	add_custom_command (
	  OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/Table.h
	  DEPENDS MakeTable
	  COMMAND MakeTable ${CMAKE_CURRENT_BINARY_DIR}/Table.h
	  )
	# add the binary tree directory to the search path 
	# for include files
	include_directories( ${CMAKE_CURRENT_BINARY_DIR} )
	 
	# add the main library
	add_library(MathFunctions mysqrt.cxx ${CMAKE_CURRENT_BINARY_DIR}/Table.h)
	 
	install (TARGETS MathFunctions DESTINATION bin)
	install (FILES MathFunctions.h DESTINATION include)

DONE

Test project /home/danml/code/CSCI2963/lab5
    Start 1: TutorialRuns
1/9 Test #1: TutorialRuns .....................   Passed    0.00 sec
    Start 2: TutorialUsage
2/9 Test #2: TutorialUsage ....................   Passed    0.00 sec
    Start 3: TutorialComp4
3/9 Test #3: TutorialComp4 ....................   Passed    0.00 sec
    Start 4: TutorialComp9
4/9 Test #4: TutorialComp9 ....................   Passed    0.00 sec
    Start 5: TutorialComp5
5/9 Test #5: TutorialComp5 ....................   Passed    0.00 sec
    Start 6: TutorialComp7
6/9 Test #6: TutorialComp7 ....................   Passed    0.00 sec
    Start 7: TutorialComp25
7/9 Test #7: TutorialComp25 ...................   Passed    0.00 sec
    Start 8: TutorialComp-25
8/9 Test #8: TutorialComp-25 ..................   Passed    0.00 sec
    Start 9: TutorialComp0.0001
9/9 Test #9: TutorialComp0.0001 ...............   Passed    0.00 sec

100% tests passed, 0 tests failed out of 9

Total Test time (real) =   0.01 sec
