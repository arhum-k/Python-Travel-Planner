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
-  Email Images:

![Sengrid Email 1](https://user-images.githubusercontent.com/72320993/163059453-ddad5dd7-633d-4343-aff6-8f25784feff8.png)
![Sendgrid Email 2](https://user-images.githubusercontent.com/72320993/163059462-8e8fe0b0-b241-4f4c-8012-9f3245d41752.png)


Once I gathered the user's inputs, I used a json file with all global airport data to determine of the inputted airport is a valid entry. To give the user options of places to visit, I used a yelp API to return 3 locations based on their respective interest. To determine the weather, I called a weather API and used the date and location as parameters.


