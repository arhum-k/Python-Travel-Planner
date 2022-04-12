# Python-Travel-Planner



Inputs:
- User's email
- Airport they are traveling to
- Arrival date
- Departure date
- 3 activies they would like to do on their trip
- Selecting which locations they would like to visit

Output:
- The user is emailed an itinerary of their trip, including their destination, weather of the city, dates, and locations they should visit based on their interests

Once I gathered the user's inputs, I used a json file with all global airport data to determine of the inputted airport is a valid entry. To give the user options of places to visit, I used a yelp API to return 3 locations based on their respective interest. To determine the weather, I called a weather API and used the date and location as parameters.
