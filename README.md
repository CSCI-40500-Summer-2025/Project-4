# Project 4

## Project Vision

For event organizers or management teams who need to find a common date for an event for any number of people, the SORT Event Resource (SORTER), is a web based availability tool for groups that provides **simple** tools to invitees, and **significantly more robust** options for organizers, unlike other services such as WhenAvailable or DatePoll. Our product provides weighting **and** comparison in order to prioritize participants based on the meaningfulness of their contribution  while providing an obfuscated front end that is more friendly to attendees.

## Architecture

### Most Important Qualities of Our Software

1. Software compatibility.
    - Users need to be able to use our product regardless of what platform they are on AND whether they have internet access or not. 
2. Product lifetime.
    - Users who purchase our product instead of our subscription should have full functionality at the time of purchase without expiring features or limited compatability.
    - Users who use our subscription service should be given options that are both worth paying for, and beat our competitors for functionality.
3. Software reuse.
    - We want our base product to remain the same, a simple uncluttered tool for organizing events. Once we add features, we want to ensure that users have an improved experience over the base, not feeling like they are using an entirely new product.
    - If users want the product to include additional functions related to its scope, instead of changing the original product, we will create a platform or line instead of forcing all users to change how they use the original product

### Architecture Layers

- User interface
  - Web and mobile browsers focused on ease of use and similar experience.
  - Desktop application for standalone handling.
- UI Management
  - Multiple UI formats based on needs (Simple/Intermediate/Advanced)
  - Optional add-on modules based on needs (Additional fields w or w/o weights)
- Configuration Services
  - Security configuration (Share/Hide data and/or results from participants)
  - Setup service (Recommended use based on events)
- Application Services
  - Graphical reporting
  - Email/messaging for responses
- Integrated Resources
  - "How To" modules for event planning (Size, budget, venues, etc.)
- SVhared Infrastructure Services
  - Optional User Storage
  - Optional Search (For similar event templates)
  - Optional Logging/Monitoring (For RSVP changes)

### Required Technologies

- Database
  - No database required for portable base product. Data stored as .csv, maintained by user
  - Relational SQL database for similar structure and ease of conversion 
- Platform/Delivery
  - Desktop application, portable
  - Web interface
- Server
  - Initial deployment may use in-house servers due to application's low bandwidth requirements.
  - Increased user base/traffic may move to cloud services for ease of maintenance
- Open-source/Licensing
  - No issues at this time.
- Development Tools
  - No limited to architectural choices at this time.



## Prototype Use

You are organizing a small event. We have provided hypothetical RSVP data for a small number of people.
This tool is also ready for use with your own RSVP data taken directly from a Google Form.

1. Imagine you know everyone and they have different value to **YOUR** event.
2. You will be asked to rate their value to **YOUR** event on a scale of 0-10:
   - **0** meaning no value (e.g., asking your ballet teacher to help fix your transmission)
   - **5** is the default value (if no value is entered, this will remain unchanged)
   - **10** being invaluable (e.g., asking your TA or Professor to lead a study group)

## Prototype Files for Windows Executable

From the "windows_portable" folder, download all 3 files.
"main.exe" "data.csv" "run.bat"

Make sure they are in the same folder, and run "run.bat"
If you are providing your own data from google, follow the directions below.

## Prototype Files for Python

1. From the "scripts" directory, download all .py files AND data.csv
2. Run main.py

## Prototype Directions for Realistic Use

1. **Create a Google Form** using the following template:
   - A short answer field for **name or email**
   - A "Multiple Choice Grid":
     - **Rows**: Available dates
     - **Columns**: "Yes" or "No" (_case-sensitive!_)
   - Example: [Google Form Template](https://docs.google.com/forms/d/e/1FAIpQLSe7uA8irq7unqNzl2SWCOUatV7FOAupqzVya9cqleOLAMsHkQ/viewform)
2. **After responses are collected**:
   - Go to the form responses tab and click "Link to Sheets"
   - Choose "Create a new spreadsheet" with any name
   - In the spreadsheet, go to File → Download → Comma Separated Values (.csv)
   - Rename this file `data.csv` and place it in the same folder as the project files INSTEAD of the data.csv provided in the repo
3. **Run the program** and follow the directions.

# Prototyping

We have created an event organizer that allows prioritizing contributors vs observers. We will be using existing web software, Google Forms, to collect data, and then allowing an event organizer to prioritize the attendance of participants and creators vs observers or learners.

The organizer will create a Google Form to collect Yes/No responses from their invitees on dates that they choose. After responses are collected, the organizer will feed the data through our prototype and assign weights as needed to essential personnel. The organizer will then be given a very brief report on the best dates for the event.

## Frontend Prototype

A proof of concept web prototype that shows how a simple UI can provide improved functionality.

Instructions for demo:
1. Open the `index.html` file in any browser (e.g., Chrome, Safari).
2. The first half of the UI shows simplified organizer input with fields:
   - Organizer Name
   - Event title
   - Dates: Enter one date per line in any forma
3. Click Submit. The simplified invitee UI then shows
   - Each invite will enter their name and choose yes/no for each date in a dropdown box
4. Click Submit to enter the next invitee information.

Notes:
- This version does **not include** date weights or output saving.
