# Item Auto Poster README

## Description:

This script automates the process of listing an item on OfferUp using Appium. It reads item details (title, choice, and price) from filenames in a specific directory, and then uses these details to post items on the OfferUp app running on an Android device or emulator.

## Requirements:

1. Python 3.x
2. Appium
3. Android SDK (for ADB commands)
4. `python-dotenv` library (for environmental variables)

## Environment Setup:

1. Create a `.env` file in your project directory with the following variables:
    - `TASKNAME`: Name of your task (if you're using scheduled tasks)
    - `DIRECTORY`: Path to the directory containing the images of the items to be listed
    - `ZIPCODE`: Your zip code
      
2. Ensure that you have created a task in the Windows Task Scheduler that opens the emulator with "Run with highest privileges" checked. This allows the script to open the emulator without having to go through the UAC prompt.

3. Ensure that your Android device (or emulator) is connected and detected by ADB. Run `adb devices` to confirm.

4. Ensure that Appium server is properly set up and is ready to listen to client requests.

## Steps Performed by the Script:

1. Enables and runs a scheduled task (based on the task name from `.env` file).
2. Starts the ADB server and initiates Appium.
3. Processes the filenames in the `DIRECTORY` to derive the title, choice, and price of items.
4. Opens the OfferUp app on the Android device.
5. Lists the item on OfferUp with the extracted details.
6. Deletes processed image files from the `DIRECTORY`.

## How to Run:

1. Ensure you've set up the environment correctly.
2. Run the script as an Administrator.
3. Watch as it automates the process on your Android device!

## Notes:

- It's important to run the script with proper privileges (Administrator) as some operations like enabling tasks may require them.
- Ensure that the OfferUp app is installed on the Android device and that it is in a ready state for the script to function correctly.
- Filenames should follow the format: `<Title>-<Choice>-<Price>.jpg` for the script to parse them correctly. To parse multi-word titles, <Title> should be written in camelCase 

## Potential Enhancements:

1. Implement error handling for scenarios where elements are not found on the app, or any other unexpected situations.
2. Implement logging for better tracking and debugging.
3. Integrate with cloud-based testing platforms to expand test coverage across multiple devices.

---

Remember to always review and test the script in a safe environment before deploying it in a production scenario. Automation scripts can lead to unintended actions if not set up correctly. Always be cautious and ensure that you have proper backups and recovery plans.
