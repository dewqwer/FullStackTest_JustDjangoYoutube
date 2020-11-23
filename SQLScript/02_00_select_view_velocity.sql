SELECT 
	"facultyName",
	"majorName",
	"typeDegree",  
	"requireMeanTime", 
	"timeStop"-"timeStart" AS differenceTime
	,speed
	
	FROM public.view_velocity
	order by "queueMajor";