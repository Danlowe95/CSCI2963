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
