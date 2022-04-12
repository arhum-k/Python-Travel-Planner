# Python-Travel-Planner



Inputs:
- User's email
- Airport they are traveling to
- Arrival date
- Departure date
- 3 activies they would like to do on their trip
- Selecting which locations they would like to visit

Output:
- The user is emailed an itinerary of their trip, including their destination, weather of the city, dates, and locations they should visit based on their interests (images attatched)

Once I gathered the user's inputs, I used a json file with all global airport data to determine of the inputted airport is a valid entry. To give the user options of places to visit, I used a yelp API to return 3 locations based on their respective interest. To determine the weather, I called a weather API and used the date and location as parameters. Finally, I used a Sengrid API to email the user their final itinerary.

Console:

![Screen Shot 2022-04-12 at 2 58 34 PM](https://user-images.githubusercontent.com/72320993/163062067-0f5da814-03ab-4b3d-8871-4f6f3a58a060.png)

![Screen Shot 2022-04-12 at 2 58 45 PM](https://user-images.githubusercontent.com/72320993/163062065-1cc71113-dfa4-4a35-8147-4968867d0bdf.png)

![Screen Shot 2022-04-12 at 3 00 36 PM](https://user-images.githubusercontent.com/72320993/163062059-dcab4b07-fa32-42c7-928a-d42378a5c647.png)

![Screen Shot 2022-04-12 at 3 00 43 PM](https://user-images.githubusercontent.com/72320993/163062058-5b1209b6-b344-44a7-b249-d9ff2478ad86.png)







Sengrid Email:

![Screen Shot 2022-04-12 at 2 55 23 PM](https://user-images.githubusercontent.com/72320993/163061003-e7c6690a-8fea-4c0e-aeed-f5061ea73405.png)

![Screen Shot 2022-04-12 at 2 55 50 PM](https://user-images.githubusercontent.com/72320993/163060993-10441638-741a-4322-84db-49454d397a49.png)





