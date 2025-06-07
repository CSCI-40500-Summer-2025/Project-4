# Project 4

## Project Vision

For event organizers or management teams who need to find a common date for an event for any number of people, the SORT Event Resource (SORTER), is a web based availability tool for groups that provides simple survey tools to invitees, and significantly more robust options for organizers, unlike other services such as WhenAvailable or DatePoll. Our produce provides weighting anr comparison tools in order to prioritize participants based on the meaningfulness of their participation or attendance as necessary while providing an obfuscated front end that is more friendly to attendees.

## Prototyping Directions for Demonstration

You are organizing a small event. We have provided hypothetical RSVP data for a small number of people.
1. Imagine you know everyone and they have different value to **YOUR** event.
2. You will be asked to rate their value to **YOUR** event on a scale of 0-10:
   - **0** meaning no value (e.g., asking your ballet teacher to help fix your transmission)
   - **5** is the default value (if no value is entered, this will remain unchanged)
   - **10** being invaluable (e.g., asking your TA or Professor to lead a study group)
3. Download project files, run the program, follow directions, and receive the report.

## Prototype Directions for Realistic Use

1. **Create a Google Form** using the following template:
   - A short answer field for **name or email**
   - A "Multiple Choice Grid":
     - **Rows**: Available dates
     - **Columns**: "Yes" or "No" (*case-sensitive!*)
   - Example: [Google Form Template](https://docs.google.com/forms/d/e/1FAIpQLSe7uA8irq7unqNzl2SWCOUatV7FOAupqzVya9cqleOLAMsHkQ/viewform)
2. **After responses are collected**:
   - Go to the form responses tab and click "Link to Sheets"
   - Choose "Create a new spreadsheet" with any name
   - In the spreadsheet, go to File → Download → Comma Separated Values (.csv)
   - Rename this file `data.csv` and place it in the same folder as the project files
3. **Run the program** and follow the directions.

# Prototyping

We have created an event organizer that allows prioritizing contributors vs observers. We will be using existing web software, Google Forms, to collect data, and then allowing an event organizer to prioritize the attendance of participants and creators vs observers or learners.

The organizer will create a Google Form to collect Yes/No responses from their invitees on dates that they choose. After responses are collected, the organizer will feed the data through our prototype and assign weights as needed to essential personnel. The organizer will then be given a very brief report on the best dates for the event.

