#Psuedocode for Python/Java
	#start app and start script 
	x = Get(systemTime(JourneyStart()));
	# App sleeps when closed but stores x
	# App is re-opened by user
	# App gets n
	n = Get(systemTime(Finish(Journey Finish())))
	# Difference in time
	dif = Compare(x,n)
	if dif<=0:
		# Function to adjust alarm times 
		alarmDoctor(int dif)
	# Variable to cath this location
	a = getLocation(thisLocation())

	# Find local currency
	b = getLocalcurrency()

	# Get tripadvirsor spots for visit
	c = getTripAdvisor(a,b)

	# ==============
	# Should output:
	# ==============

	# String Name = location(name)
	# String Address = location(address)
	# String LatLong = location(lat)
	# tuple reviews = location(reviews)
	# String price = location(price)