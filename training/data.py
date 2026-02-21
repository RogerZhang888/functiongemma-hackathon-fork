







TOOL_GET_WEATHER = {
    "name": "get_weather",
    "description": "Get current weather for a location",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {"type": "string", "description": "City name"}
        },
        "required": ["location"],
    },
}

TOOL_SET_ALARM = {
    "name": "set_alarm",
    "description": "Set an alarm for a given time",
    "parameters": {
        "type": "object",
        "properties": {
            "hour": {"type": "integer", "description": "Hour to set the alarm for"},
            "minute": {"type": "integer", "description": "Minute to set the alarm for"},
        },
        "required": ["hour", "minute"],
    },
}

TOOL_SEND_MESSAGE = {
    "name": "send_message",
    "description": "Send a message to a contact",
    "parameters": {
        "type": "object",
        "properties": {
            "recipient": {"type": "string", "description": "Name of the person to send the message to"},
            "message": {"type": "string", "description": "The message content to send"},
        },
        "required": ["recipient", "message"],
    },
}

TOOL_CREATE_REMINDER = {
    "name": "create_reminder",
    "description": "Create a reminder with a title and time",
    "parameters": {
        "type": "object",
        "properties": {
            "title": {"type": "string", "description": "Reminder title"},
            "time": {"type": "string", "description": "Time for the reminder (e.g. 3:00 PM)"},
        },
        "required": ["title", "time"],
    },
}

TOOL_SEARCH_CONTACTS = {
    "name": "search_contacts",
    "description": "Search for a contact by name",
    "parameters": {
        "type": "object",
        "properties": {
            "query": {"type": "string", "description": "Name to search for"},
        },
        "required": ["query"],
    },
}

TOOL_PLAY_MUSIC = {
    "name": "play_music",
    "description": "Play a song or playlist",
    "parameters": {
        "type": "object",
        "properties": {
            "song": {"type": "string", "description": "Song or playlist name"},
        },
        "required": ["song"],
    },
}

TOOL_SET_TIMER = {
    "name": "set_timer",
    "description": "Set a countdown timer",
    "parameters": {
        "type": "object",
        "properties": {
            "minutes": {"type": "integer", "description": "Number of minutes"},
        },
        "required": ["minutes"],
    },
}











main_list = [
    

  {"id": 1, "prompt": "How's the weather in Paris?", "num_available_tools": 1, "available_tools": [TOOL_GET_WEATHER], "route_label": 1},
  {"id": 2, "prompt": "What's the weather like in Tokyo?", "num_available_tools": 2, "available_tools": [TOOL_GET_WEATHER, TOOL_SET_ALARM], "route_label": 1},
  {"id": 3, "prompt": "Check the weather in Berlin.", "num_available_tools": 3, "available_tools": [TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 1},
  {"id": 4, "prompt": "Get the weather in Singapore.", "num_available_tools": 4, "available_tools": [TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 1},
  {"id": 5, "prompt": "How's the weather in Sydney?", "num_available_tools": 5, "available_tools": [TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 1},

  {"id": 6, "prompt": "Set an alarm for 7:00 AM.", "num_available_tools": 1, "available_tools": [TOOL_SET_ALARM], "route_label": 1},
  {"id": 7, "prompt": "Set an alarm for 6:30 PM.", "num_available_tools": 2, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER], "route_label": 1},
  {"id": 8, "prompt": "Set an alarm for 9:15 AM.", "num_available_tools": 3, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE], "route_label": 1},
  {"id": 9, "prompt": "Set an alarm for 8:45 PM.", "num_available_tools": 4, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 1},
  {"id": 10, "prompt": "Set an alarm for 10:10 AM.", "num_available_tools": 5, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 1},

  {"id": 11, "prompt": "Set a timer for 10 minutes.", "num_available_tools": 1, "available_tools": [TOOL_SET_TIMER], "route_label": 1},
  {"id": 12, "prompt": "Start a 25 minute timer.", "num_available_tools": 2, "available_tools": [TOOL_SET_TIMER, TOOL_GET_WEATHER], "route_label": 1},
  {"id": 13, "prompt": "Set a timer for 45 minutes.", "num_available_tools": 3, "available_tools": [TOOL_SET_TIMER, TOOL_GET_WEATHER, TOOL_SET_ALARM], "route_label": 1},
  {"id": 14, "prompt": "Start a 3 minute timer.", "num_available_tools": 4, "available_tools": [TOOL_SET_TIMER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 1},
  {"id": 15, "prompt": "Set a timer for 90 minutes.", "num_available_tools": 5, "available_tools": [TOOL_SET_TIMER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 1},

  {"id": 16, "prompt": "Text Bob saying 'See you soon'.", "num_available_tools": 2, "available_tools": [TOOL_SEND_MESSAGE, TOOL_GET_WEATHER], "route_label": 1},
  {"id": 17, "prompt": "Send a message to Alice saying 'Running late'.", "num_available_tools": 3, "available_tools": [TOOL_SEND_MESSAGE, TOOL_GET_WEATHER, TOOL_SET_ALARM], "route_label": 1},
  {"id": 18, "prompt": "Message Dave saying 'I'll be there at 3 PM'.", "num_available_tools": 4, "available_tools": [TOOL_SEND_MESSAGE, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_CREATE_REMINDER], "route_label": 1},
  {"id": 19, "prompt": "Send a message to Sarah saying 'Thanks for your help'.", "num_available_tools": 5, "available_tools": [TOOL_SEND_MESSAGE, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 1},
  {"id": 20, "prompt": "Text John saying 'Meeting at 3 PM'.", "num_available_tools": 3, "available_tools": [TOOL_SEND_MESSAGE, TOOL_GET_WEATHER, TOOL_SET_ALARM], "route_label": 1},

  {"id": 21, "prompt": "Create a reminder titled 'Doctor appointment' at 4:00 PM.", "num_available_tools": 1, "available_tools": [TOOL_CREATE_REMINDER], "route_label": 1},
  {"id": 22, "prompt": "Set a reminder titled 'Team meeting' at 10:30 AM.", "num_available_tools": 2, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER], "route_label": 1},
  {"id": 23, "prompt": "Create a reminder titled 'Buy groceries' at 6:00 PM.", "num_available_tools": 3, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM], "route_label": 1},
  {"id": 24, "prompt": "Set a reminder titled 'Submit report' at 2:00 PM.", "num_available_tools": 4, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 1},
  {"id": 25, "prompt": "Create a reminder titled 'Gym session' at 7:15 PM.", "num_available_tools": 5, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_SEARCH_CONTACTS], "route_label": 1},
  {"id": 26, "prompt": "Find Michael in my contacts.", "num_available_tools": 1, "available_tools": [TOOL_SEARCH_CONTACTS], "route_label": 1},
  {"id": 27, "prompt": "Search for Emily in my contacts.", "num_available_tools": 2, "available_tools": [TOOL_SEARCH_CONTACTS, TOOL_GET_WEATHER], "route_label": 1},
  {"id": 28, "prompt": "Look up Chris in my contacts.", "num_available_tools": 3, "available_tools": [TOOL_SEARCH_CONTACTS, TOOL_GET_WEATHER, TOOL_SET_ALARM], "route_label": 1},
  {"id": 29, "prompt": "Find Olivia in my contacts.", "num_available_tools": 4, "available_tools": [TOOL_SEARCH_CONTACTS, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 1},
  {"id": 30, "prompt": "Search for Daniel in my contacts.", "num_available_tools": 5, "available_tools": [TOOL_SEARCH_CONTACTS, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 1},

  {"id": 31, "prompt": "Play 'Shape of You'.", "num_available_tools": 1, "available_tools": [TOOL_PLAY_MUSIC], "route_label": 1},
  {"id": 32, "prompt": "Play the song 'Halo'.", "num_available_tools": 2, "available_tools": [TOOL_PLAY_MUSIC, TOOL_GET_WEATHER], "route_label": 1},
  {"id": 33, "prompt": "Play 'Lose Yourself'.", "num_available_tools": 3, "available_tools": [TOOL_PLAY_MUSIC, TOOL_GET_WEATHER, TOOL_SET_ALARM], "route_label": 1},
  {"id": 34, "prompt": "Play the playlist 'Top Hits 2024'.", "num_available_tools": 4, "available_tools": [TOOL_PLAY_MUSIC, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 1},
  {"id": 35, "prompt": "Play 'Viva La Vida'.", "num_available_tools": 5, "available_tools": [TOOL_PLAY_MUSIC, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 1},

  {"id": 36, "prompt": "Check the weather in Rome.", "num_available_tools": 4, "available_tools": [TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 1},
  {"id": 37, "prompt": "Set an alarm for 11:30 AM.", "num_available_tools": 4, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 1},
  {"id": 38, "prompt": "Set a timer for 20 minutes.", "num_available_tools": 3, "available_tools": [TOOL_SET_TIMER, TOOL_GET_WEATHER, TOOL_SET_ALARM], "route_label": 1},
  {"id": 39, "prompt": "Text Emma saying 'Arrived safely'.", "num_available_tools": 4, "available_tools": [TOOL_SEND_MESSAGE, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_CREATE_REMINDER], "route_label": 1},
  {"id": 40, "prompt": "Create a reminder titled 'Call Mom' at 8:00 PM.", "num_available_tools": 5, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_SEARCH_CONTACTS], "route_label": 1},

  {"id": 41, "prompt": "Get the weather in Madrid.", "num_available_tools": 5, "available_tools": [TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 1},
  {"id": 42, "prompt": "Set an alarm for 4:20 PM.", "num_available_tools": 4, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 1},
  {"id": 43, "prompt": "Start a 60 minute timer.", "num_available_tools": 5, "available_tools": [TOOL_SET_TIMER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 1},
  {"id": 44, "prompt": "Search for Sophia in my contacts.", "num_available_tools": 4, "available_tools": [TOOL_SEARCH_CONTACTS, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 1},
  {"id": 45, "prompt": "Send a message to Mark saying 'On my way'.", "num_available_tools": 5, "available_tools": [TOOL_SEND_MESSAGE, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 1},

  {"id": 46, "prompt": "Play the song 'Believer'.", "num_available_tools": 4, "available_tools": [TOOL_PLAY_MUSIC, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 1},
  {"id": 47, "prompt": "Set a timer for 7 minutes.", "num_available_tools": 5, "available_tools": [TOOL_SET_TIMER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 1},
  {"id": 48, "prompt": "Check the weather in Lisbon.", "num_available_tools": 3, "available_tools": [TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 1},
  {"id": 49, "prompt": "Set an alarm for 3:05 PM.", "num_available_tools": 4, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 1},
  {"id": 50, "prompt": "Create a reminder titled 'Dinner reservation' at 6:45 PM.", "num_available_tools": 5, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_SEARCH_CONTACTS], "route_label": 1},
  {"id": 51, "prompt": "How's the weather in London?", "num_available_tools": 2, "available_tools": [TOOL_GET_WEATHER, TOOL_SET_ALARM], "route_label": 1},
  {"id": 52, "prompt": "Check the weather in Toronto.", "num_available_tools": 3, "available_tools": [TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 1},
  {"id": 53, "prompt": "Get the weather in Seoul.", "num_available_tools": 4, "available_tools": [TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 1},
  {"id": 54, "prompt": "What's the weather like in Dubai?", "num_available_tools": 5, "available_tools": [TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 1},
  {"id": 55, "prompt": "How's the weather in Bangkok?", "num_available_tools": 3, "available_tools": [TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 1},
  
  {"id": 56, "prompt": "Set an alarm for 6:00 AM.", "num_available_tools": 2, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER], "route_label": 1},
  {"id": 57, "prompt": "Set an alarm for 12:30 PM.", "num_available_tools": 3, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE], "route_label": 1},
  {"id": 58, "prompt": "Set an alarm for 1:45 PM.", "num_available_tools": 4, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 1},
  {"id": 59, "prompt": "Set an alarm for 5:55 AM.", "num_available_tools": 5, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 1},
  {"id": 60, "prompt": "Set an alarm for 9:00 PM.", "num_available_tools": 3, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE], "route_label": 1},
  
  {"id": 61, "prompt": "Start a 15 minute timer.", "num_available_tools": 2, "available_tools": [TOOL_SET_TIMER, TOOL_GET_WEATHER], "route_label": 1},
  {"id": 62, "prompt": "Set a timer for 30 minutes.", "num_available_tools": 3, "available_tools": [TOOL_SET_TIMER, TOOL_GET_WEATHER, TOOL_SET_ALARM], "route_label": 1},
  {"id": 63, "prompt": "Start a 5 minute timer.", "num_available_tools": 4, "available_tools": [TOOL_SET_TIMER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 1},
  {"id": 64, "prompt": "Set a timer for 120 minutes.", "num_available_tools": 5, "available_tools": [TOOL_SET_TIMER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 1},
  {"id": 65, "prompt": "Start a 40 minute timer.", "num_available_tools": 3, "available_tools": [TOOL_SET_TIMER, TOOL_GET_WEATHER, TOOL_SET_ALARM], "route_label": 1},
  
  {"id": 66, "prompt": "Text Kevin saying 'See you at noon'.", "num_available_tools": 2, "available_tools": [TOOL_SEND_MESSAGE, TOOL_GET_WEATHER], "route_label": 1},
  {"id": 67, "prompt": "Send a message to Laura saying 'I'll be there soon'.", "num_available_tools": 3, "available_tools": [TOOL_SEND_MESSAGE, TOOL_GET_WEATHER, TOOL_SET_ALARM], "route_label": 1},
  {"id": 68, "prompt": "Message Tom saying 'Good luck!'.", "num_available_tools": 4, "available_tools": [TOOL_SEND_MESSAGE, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_CREATE_REMINDER], "route_label": 1},
  {"id": 69, "prompt": "Send a message to Nina saying 'Meeting confirmed'.", "num_available_tools": 5, "available_tools": [TOOL_SEND_MESSAGE, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 1},
  {"id": 70, "prompt": "Text Ethan saying 'Call me later'.", "num_available_tools": 3, "available_tools": [TOOL_SEND_MESSAGE, TOOL_GET_WEATHER, TOOL_SET_ALARM], "route_label": 1},
  {"id": 71, "prompt": "Create a reminder titled 'Project deadline' at 11:00 AM.", "num_available_tools": 2, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER], "route_label": 1},
  {"id": 72, "prompt": "Set a reminder titled 'Parent-teacher meeting' at 3:30 PM.", "num_available_tools": 3, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM], "route_label": 1},
  {"id": 73, "prompt": "Create a reminder titled 'Dentist appointment' at 8:00 AM.", "num_available_tools": 4, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 1},
  {"id": 74, "prompt": "Set a reminder titled 'Car service' at 1:00 PM.", "num_available_tools": 5, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_SEARCH_CONTACTS], "route_label": 1},
  {"id": 75, "prompt": "Create a reminder titled 'Pick up package' at 6:00 PM.", "num_available_tools": 3, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM], "route_label": 1},
  {"id": 76, "prompt": "Find Rachel in my contacts.", "num_available_tools": 2, "available_tools": [TOOL_SEARCH_CONTACTS, TOOL_GET_WEATHER], "route_label": 1},
  {"id": 77, "prompt": "Search for Lucas in my contacts.", "num_available_tools": 3, "available_tools": [TOOL_SEARCH_CONTACTS, TOOL_GET_WEATHER, TOOL_SET_ALARM], "route_label": 1},
  {"id": 78, "prompt": "Look up Hannah in my contacts.", "num_available_tools": 4, "available_tools": [TOOL_SEARCH_CONTACTS, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 1},
  {"id": 79, "prompt": "Find Mason in my contacts.", "num_available_tools": 5, "available_tools": [TOOL_SEARCH_CONTACTS, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 1},
  {"id": 80, "prompt": "Search for Chloe in my contacts.", "num_available_tools": 3, "available_tools": [TOOL_SEARCH_CONTACTS, TOOL_GET_WEATHER, TOOL_SET_ALARM], "route_label": 1},

  {"id": 81, "prompt": "Play 'Counting Stars'.", "num_available_tools": 2, "available_tools": [TOOL_PLAY_MUSIC, TOOL_GET_WEATHER], "route_label": 1},
  {"id": 82, "prompt": "Play the song 'Thunder'.", "num_available_tools": 3, "available_tools": [TOOL_PLAY_MUSIC, TOOL_GET_WEATHER, TOOL_SET_ALARM], "route_label": 1},
  {"id": 83, "prompt": "Play 'Bad Guy'.", "num_available_tools": 4, "available_tools": [TOOL_PLAY_MUSIC, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 1},
  {"id": 84, "prompt": "Play the playlist 'Workout Mix'.", "num_available_tools": 5, "available_tools": [TOOL_PLAY_MUSIC, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 1},
  {"id": 85, "prompt": "Play 'Fix You'.", "num_available_tools": 3, "available_tools": [TOOL_PLAY_MUSIC, TOOL_GET_WEATHER, TOOL_SET_ALARM], "route_label": 1},

  {"id": 86, "prompt": "Check the weather in Oslo.", "num_available_tools": 4, "available_tools": [TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 1},
  {"id": 87, "prompt": "Set an alarm for 2:20 PM.", "num_available_tools": 3, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE], "route_label": 1},
  {"id": 88, "prompt": "Start a 50 minute timer.", "num_available_tools": 4, "available_tools": [TOOL_SET_TIMER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 1},
  {"id": 89, "prompt": "Text Zoe saying 'Dinner at 7'.", "num_available_tools": 5, "available_tools": [TOOL_SEND_MESSAGE, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 1},
  {"id": 90, "prompt": "Create a reminder titled 'Yoga class' at 5:30 PM.", "num_available_tools": 4, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 1},

  {"id": 91, "prompt": "Get the weather in Vienna.", "num_available_tools": 3, "available_tools": [TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 1},
  {"id": 92, "prompt": "Set an alarm for 3:30 PM.", "num_available_tools": 4, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 1},
  {"id": 93, "prompt": "Set a timer for 8 minutes.", "num_available_tools": 5, "available_tools": [TOOL_SET_TIMER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 1},
  {"id": 94, "prompt": "Search for Benjamin in my contacts.", "num_available_tools": 4, "available_tools": [TOOL_SEARCH_CONTACTS, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 1},
  {"id": 95, "prompt": "Send a message to Lily saying 'See you tomorrow'.", "num_available_tools": 5, "available_tools": [TOOL_SEND_MESSAGE, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 1},

  {"id": 96, "prompt": "Play 'Radioactive'.", "num_available_tools": 3, "available_tools": [TOOL_PLAY_MUSIC, TOOL_GET_WEATHER, TOOL_SET_ALARM], "route_label": 1},
  {"id": 97, "prompt": "Set an alarm for 7:25 AM.", "num_available_tools": 4, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 1},
  {"id": 98, "prompt": "Check the weather in Helsinki.", "num_available_tools": 5, "available_tools": [TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 1},
  {"id": 99, "prompt": "Create a reminder titled 'Water plants' at 9:00 AM.", "num_available_tools": 3, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM], "route_label": 1},
  {"id": 100, "prompt": "Set a timer for 12 minutes.", "num_available_tools": 4, "available_tools": [TOOL_SET_TIMER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 1},
  {"id": 101, "prompt": "How's the weather in Barcelona?", "num_available_tools": 3, "available_tools": [TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 1},
  {"id": 102, "prompt": "Set an alarm for 6:40 AM.", "num_available_tools": 4, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 1},
  {"id": 103, "prompt": "Start a 35 minute timer.", "num_available_tools": 5, "available_tools": [TOOL_SET_TIMER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 1},
  {"id": 104, "prompt": "Text Daniel saying 'Running 5 minutes late'.", "num_available_tools": 4, "available_tools": [TOOL_SEND_MESSAGE, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_CREATE_REMINDER], "route_label": 1},
  {"id": 105, "prompt": "Create a reminder titled 'Meeting notes' at 4:45 PM.", "num_available_tools": 5, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_SEARCH_CONTACTS], "route_label": 1},

  {"id": 106, "prompt": "Play 'Perfect'.", "num_available_tools": 3, "available_tools": [TOOL_PLAY_MUSIC, TOOL_GET_WEATHER, TOOL_SET_ALARM], "route_label": 1},
  {"id": 107, "prompt": "Search for Grace in my contacts.", "num_available_tools": 4, "available_tools": [TOOL_SEARCH_CONTACTS, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 1},
  {"id": 108, "prompt": "Set a timer for 6 minutes.", "num_available_tools": 5, "available_tools": [TOOL_SET_TIMER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 1},
  {"id": 109, "prompt": "Set an alarm for 8:35 PM.", "num_available_tools": 4, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 1},
  {"id": 110, "prompt": "Check the weather in Zurich.", "num_available_tools": 5, "available_tools": [TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 1},

  {"id": 111, "prompt": "Text Olivia saying 'I'm outside'.", "num_available_tools": 4, "available_tools": [TOOL_SEND_MESSAGE, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_CREATE_REMINDER], "route_label": 1},
  {"id": 112, "prompt": "Create a reminder titled 'Conference call' at 2:15 PM.", "num_available_tools": 5, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_SEARCH_CONTACTS], "route_label": 1},
  {"id": 113, "prompt": "Play the song 'Adventure of a Lifetime'.", "num_available_tools": 4, "available_tools": [TOOL_PLAY_MUSIC, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 1},
  {"id": 114, "prompt": "Set a timer for 18 minutes.", "num_available_tools": 5, "available_tools": [TOOL_SET_TIMER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 1},
  {"id": 115, "prompt": "Set an alarm for 5:05 AM.", "num_available_tools": 4, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 1},

  {"id": 116, "prompt": "Get the weather in Prague.", "num_available_tools": 3, "available_tools": [TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 1},
  {"id": 117, "prompt": "Search for Noah in my contacts.", "num_available_tools": 4, "available_tools": [TOOL_SEARCH_CONTACTS, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 1},
  {"id": 118, "prompt": "Text Ava saying 'Arrived'.", "num_available_tools": 5, "available_tools": [TOOL_SEND_MESSAGE, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 1},
  {"id": 119, "prompt": "Set a timer for 22 minutes.", "num_available_tools": 4, "available_tools": [TOOL_SET_TIMER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 1},
  {"id": 120, "prompt": "Create a reminder titled 'Pick up kids' at 3:00 PM.", "num_available_tools": 5, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_SEARCH_CONTACTS], "route_label": 1},

  {"id": 121, "prompt": "Play 'Someone Like You'.", "num_available_tools": 4, "available_tools": [TOOL_PLAY_MUSIC, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 1},
  {"id": 122, "prompt": "Set an alarm for 6:15 AM.", "num_available_tools": 5, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 1},
  {"id": 123, "prompt": "Check the weather in Amsterdam.", "num_available_tools": 4, "available_tools": [TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 1},
  {"id": 124, "prompt": "Search for Isabella in my contacts.", "num_available_tools": 5, "available_tools": [TOOL_SEARCH_CONTACTS, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 1},
  {"id": 125, "prompt": "Set a timer for 55 minutes.", "num_available_tools": 4, "available_tools": [TOOL_SET_TIMER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 1},
  {"id": 126, "prompt": "Text Mason saying 'Be there soon'.", "num_available_tools": 5, "available_tools": [TOOL_SEND_MESSAGE, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 1},
  {"id": 127, "prompt": "Create a reminder titled 'Lunch with Sam' at 12:00 PM.", "num_available_tools": 4, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 1},
  {"id": 128, "prompt": "Play 'Yellow'.", "num_available_tools": 5, "available_tools": [TOOL_PLAY_MUSIC, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 1},
  {"id": 129, "prompt": "Set an alarm for 4:45 AM.", "num_available_tools": 4, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 1},
  {"id": 130, "prompt": "Check the weather in Athens.", "num_available_tools": 5, "available_tools": [TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 1},

  {"id": 131, "prompt": "Search for Jacob in my contacts.", "num_available_tools": 4, "available_tools": [TOOL_SEARCH_CONTACTS, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 1},
  {"id": 132, "prompt": "Set a timer for 13 minutes.", "num_available_tools": 5, "available_tools": [TOOL_SET_TIMER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 1},
  {"id": 133, "prompt": "Text Mia saying 'Good night'.", "num_available_tools": 4, "available_tools": [TOOL_SEND_MESSAGE, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_CREATE_REMINDER], "route_label": 1},
  {"id": 134, "prompt": "Create a reminder titled 'Submit invoice' at 1:30 PM.", "num_available_tools": 5, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_SEARCH_CONTACTS], "route_label": 1},
  {"id": 135, "prompt": "Play the song 'Grenade'.", "num_available_tools": 4, "available_tools": [TOOL_PLAY_MUSIC, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 1},

  {"id": 136, "prompt": "Set an alarm for 7:05 PM.", "num_available_tools": 5, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 1},
  {"id": 137, "prompt": "Check the weather in Warsaw.", "num_available_tools": 4, "available_tools": [TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 1},
  {"id": 138, "prompt": "Search for Ella in my contacts.", "num_available_tools": 5, "available_tools": [TOOL_SEARCH_CONTACTS, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 1},
  {"id": 139, "prompt": "Set a timer for 27 minutes.", "num_available_tools": 4, "available_tools": [TOOL_SET_TIMER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 1},
  {"id": 140, "prompt": "Text Logan saying 'Thanks!'.", "num_available_tools": 5, "available_tools": [TOOL_SEND_MESSAGE, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 1},

  {"id": 141, "prompt": "Create a reminder titled 'Team sync' at 9:45 AM.", "num_available_tools": 4, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 1},
  {"id": 142, "prompt": "Play 'Demons'.", "num_available_tools": 5, "available_tools": [TOOL_PLAY_MUSIC, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 1},
  {"id": 143, "prompt": "Set an alarm for 8:25 AM.", "num_available_tools": 4, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 1},
  {"id": 144, "prompt": "Check the weather in Budapest.", "num_available_tools": 5, "available_tools": [TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 1},
  {"id": 145, "prompt": "Search for Harper in my contacts.", "num_available_tools": 4, "available_tools": [TOOL_SEARCH_CONTACTS, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 1},

  {"id": 146, "prompt": "Set a timer for 33 minutes.", "num_available_tools": 5, "available_tools": [TOOL_SET_TIMER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 1},
  {"id": 147, "prompt": "Text James saying 'See you at 5'.", "num_available_tools": 4, "available_tools": [TOOL_SEND_MESSAGE, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_CREATE_REMINDER], "route_label": 1},
  {"id": 148, "prompt": "Create a reminder titled 'Client call' at 11:15 AM.", "num_available_tools": 5, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_SEARCH_CONTACTS], "route_label": 1},
  {"id": 149, "prompt": "Play the playlist 'Chill Vibes'.", "num_available_tools": 4, "available_tools": [TOOL_PLAY_MUSIC, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 1},
  {"id": 150, "prompt": "Set an alarm for 10:55 PM.", "num_available_tools": 5, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 1},
  {"id": 151, "prompt": "Get the weather in Vancouver.", "num_available_tools": 2, "available_tools": [TOOL_GET_WEATHER, TOOL_SET_ALARM], "route_label": 1},
  {"id": 152, "prompt": "Check the weather in Kuala Lumpur.", "num_available_tools": 3, "available_tools": [TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 1},
  {"id": 153, "prompt": "What's the weather in Hong Kong?", "num_available_tools": 4, "available_tools": [TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 1},
  {"id": 154, "prompt": "How's the weather in Melbourne?", "num_available_tools": 5, "available_tools": [TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 1},
  {"id": 155, "prompt": "Get the weather in Manila.", "num_available_tools": 3, "available_tools": [TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 1},

  {"id": 156, "prompt": "Set an alarm for 5:30 AM.", "num_available_tools": 2, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER], "route_label": 1},
  {"id": 157, "prompt": "Set an alarm for 8:00 AM.", "num_available_tools": 3, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE], "route_label": 1},
  {"id": 158, "prompt": "Set an alarm for 2:10 PM.", "num_available_tools": 4, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 1},
  {"id": 159, "prompt": "Set an alarm for 9:40 PM.", "num_available_tools": 5, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 1},
  {"id": 160, "prompt": "Set an alarm for 12:05 PM.", "num_available_tools": 3, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE], "route_label": 1},

  {"id": 161, "prompt": "Set a timer for 14 minutes.", "num_available_tools": 2, "available_tools": [TOOL_SET_TIMER, TOOL_GET_WEATHER], "route_label": 1},
  {"id": 162, "prompt": "Start a 9 minute timer.", "num_available_tools": 3, "available_tools": [TOOL_SET_TIMER, TOOL_GET_WEATHER, TOOL_SET_ALARM], "route_label": 1},
  {"id": 163, "prompt": "Set a timer for 32 minutes.", "num_available_tools": 4, "available_tools": [TOOL_SET_TIMER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 1},
  {"id": 164, "prompt": "Start a 70 minute timer.", "num_available_tools": 5, "available_tools": [TOOL_SET_TIMER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 1},
  {"id": 165, "prompt": "Set a timer for 6 minutes.", "num_available_tools": 3, "available_tools": [TOOL_SET_TIMER, TOOL_GET_WEATHER, TOOL_SET_ALARM], "route_label": 1},

  {"id": 166, "prompt": "Text Ryan saying 'On my way'.", "num_available_tools": 2, "available_tools": [TOOL_SEND_MESSAGE, TOOL_GET_WEATHER], "route_label": 1},
  {"id": 167, "prompt": "Send a message to Priya saying 'See you at 6'.", "num_available_tools": 3, "available_tools": [TOOL_SEND_MESSAGE, TOOL_GET_WEATHER, TOOL_SET_ALARM], "route_label": 1},
  {"id": 168, "prompt": "Message Ben saying 'Please call me'.", "num_available_tools": 4, "available_tools": [TOOL_SEND_MESSAGE, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_CREATE_REMINDER], "route_label": 1},
  {"id": 169, "prompt": "Send a message to Chloe saying 'Thanks!'.", "num_available_tools": 5, "available_tools": [TOOL_SEND_MESSAGE, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 1},
  {"id": 170, "prompt": "Text Iris saying 'I’m here'.", "num_available_tools": 3, "available_tools": [TOOL_SEND_MESSAGE, TOOL_GET_WEATHER, TOOL_SET_ALARM], "route_label": 1},

  {"id": 171, "prompt": "Create a reminder titled 'Pay electricity bill' at 9:00 PM.", "num_available_tools": 2, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER], "route_label": 1},
  {"id": 172, "prompt": "Set a reminder titled 'Submit assignment' at 11:59 PM.", "num_available_tools": 3, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM], "route_label": 1},
  {"id": 173, "prompt": "Create a reminder titled 'Call the bank' at 2:30 PM.", "num_available_tools": 4, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 1},
  {"id": 174, "prompt": "Set a reminder titled 'Pick up groceries' at 6:15 PM.", "num_available_tools": 5, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_SEARCH_CONTACTS], "route_label": 1},
  {"id": 175, "prompt": "Create a reminder titled 'Water the plants' at 8:00 AM.", "num_available_tools": 3, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM], "route_label": 1},

  {"id": 176, "prompt": "Search for Ethan in my contacts.", "num_available_tools": 2, "available_tools": [TOOL_SEARCH_CONTACTS, TOOL_GET_WEATHER], "route_label": 1},
  {"id": 177, "prompt": "Find Amelia in my contacts.", "num_available_tools": 3, "available_tools": [TOOL_SEARCH_CONTACTS, TOOL_GET_WEATHER, TOOL_SET_ALARM], "route_label": 1},
  {"id": 178, "prompt": "Look up Lucas in my contacts.", "num_available_tools": 4, "available_tools": [TOOL_SEARCH_CONTACTS, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 1},
  {"id": 179, "prompt": "Search for Sofia in my contacts.", "num_available_tools": 5, "available_tools": [TOOL_SEARCH_CONTACTS, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 1},
  {"id": 180, "prompt": "Find Henry in my contacts.", "num_available_tools": 3, "available_tools": [TOOL_SEARCH_CONTACTS, TOOL_GET_WEATHER, TOOL_SET_ALARM], "route_label": 1},

  {"id": 181, "prompt": "Play 'Smells Like Teen Spirit'.", "num_available_tools": 2, "available_tools": [TOOL_PLAY_MUSIC, TOOL_GET_WEATHER], "route_label": 1},
  {"id": 182, "prompt": "Play the song 'Someone You Loved'.", "num_available_tools": 3, "available_tools": [TOOL_PLAY_MUSIC, TOOL_GET_WEATHER, TOOL_SET_ALARM], "route_label": 1},
  {"id": 183, "prompt": "Play 'Uptown Funk'.", "num_available_tools": 4, "available_tools": [TOOL_PLAY_MUSIC, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 1},
  {"id": 184, "prompt": "Play the playlist 'Focus Beats'.", "num_available_tools": 5, "available_tools": [TOOL_PLAY_MUSIC, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 1},
  {"id": 185, "prompt": "Play 'Take On Me'.", "num_available_tools": 3, "available_tools": [TOOL_PLAY_MUSIC, TOOL_GET_WEATHER, TOOL_SET_ALARM], "route_label": 1},

  {"id": 186, "prompt": "Check the weather in Reykjavik.", "num_available_tools": 4, "available_tools": [TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 1},
  {"id": 187, "prompt": "Set an alarm for 7:50 AM.", "num_available_tools": 3, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE], "route_label": 1},
  {"id": 188, "prompt": "Set a timer for 26 minutes.", "num_available_tools": 4, "available_tools": [TOOL_SET_TIMER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 1},
  {"id": 189, "prompt": "Text Maya saying 'I'll be there in 5'.", "num_available_tools": 5, "available_tools": [TOOL_SEND_MESSAGE, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 1},
  {"id": 190, "prompt": "Create a reminder titled 'Team standup' at 9:30 AM.", "num_available_tools": 4, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 1},

  {"id": 191, "prompt": "Get the weather in Brussels.", "num_available_tools": 3, "available_tools": [TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 1},
  {"id": 192, "prompt": "Set an alarm for 3:55 PM.", "num_available_tools": 4, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 1},
  {"id": 193, "prompt": "Start a 16 minute timer.", "num_available_tools": 5, "available_tools": [TOOL_SET_TIMER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 1},
  {"id": 194, "prompt": "Search for Jack in my contacts.", "num_available_tools": 4, "available_tools": [TOOL_SEARCH_CONTACTS, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 1},
  {"id": 195, "prompt": "Send a message to Nora saying 'See you soon'.", "num_available_tools": 5, "available_tools": [TOOL_SEND_MESSAGE, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 1},

  {"id": 196, "prompt": "Play the song 'Levitating'.", "num_available_tools": 4, "available_tools": [TOOL_PLAY_MUSIC, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 1},
  {"id": 197, "prompt": "Set an alarm for 6:05 AM.", "num_available_tools": 5, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 1},
  {"id": 198, "prompt": "Check the weather in Copenhagen.", "num_available_tools": 4, "available_tools": [TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 1},
  {"id": 199, "prompt": "Create a reminder titled 'Send invoice' at 1:10 PM.", "num_available_tools": 3, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM], "route_label": 1},
  {"id": 200, "prompt": "Set a timer for 11 minutes.", "num_available_tools": 4, "available_tools": [TOOL_SET_TIMER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 1},
  {"id": 201, "prompt": "Set an alarm for 7 AM and check the weather in London.", "num_available_tools": 4, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 0},
  {"id": 202, "prompt": "Send a message to Bob saying hi and play some music.", "num_available_tools": 5, "available_tools": [TOOL_SEND_MESSAGE, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 0},
  {"id": 203, "prompt": "Find Sarah in my contacts and text her 'Call me'.", "num_available_tools": 5, "available_tools": [TOOL_SEARCH_CONTACTS, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 0},
  {"id": 204, "prompt": "Remind me to call John tomorrow morning.", "num_available_tools": 4, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 0},
  {"id": 205, "prompt": "Set something so I don't forget my meeting next week.", "num_available_tools": 5, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_SEARCH_CONTACTS], "route_label": 0},

  {"id": 206, "prompt": "If it's raining in Paris, send a message to Mike saying I'll stay home.", "num_available_tools": 6, "available_tools": [TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 207, "prompt": "Wake me up early and start my workout playlist.", "num_available_tools": 6, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 208, "prompt": "Set a timer and play relaxing music.", "num_available_tools": 5, "available_tools": [TOOL_SET_TIMER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 0},
  {"id": 209, "prompt": "Message the first John in my contacts saying 'Meet at 7'.", "num_available_tools": 5, "available_tools": [TOOL_SEND_MESSAGE, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 0},
  {"id": 210, "prompt": "Set an alarm for nine.", "num_available_tools": 4, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 0},

  {"id": 211, "prompt": "Remind me in a bit to check the oven.", "num_available_tools": 4, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 0},
  {"id": 212, "prompt": "Play something chill.", "num_available_tools": 4, "available_tools": [TOOL_PLAY_MUSIC, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 0},
  {"id": 213, "prompt": "Text my boss that I'll be late.", "num_available_tools": 5, "available_tools": [TOOL_SEND_MESSAGE, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 0},
  {"id": 214, "prompt": "Set a reminder for later today.", "num_available_tools": 4, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 0},
  {"id": 215, "prompt": "Wake me up in 10.", "num_available_tools": 5, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 0},

  {"id": 216, "prompt": "Check the weather and set an alarm if it's cold.", "num_available_tools": 5, "available_tools": [TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 0},
  {"id": 217, "prompt": "Find Alex and tell him thanks.", "num_available_tools": 5, "available_tools": [TOOL_SEARCH_CONTACTS, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 0},
  {"id": 218, "prompt": "Remind me about the thing at 5.", "num_available_tools": 4, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 0},
  {"id": 219, "prompt": "Set an alarm sometime after lunch.", "num_available_tools": 4, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 0},
  {"id": 220, "prompt": "Play the usual playlist.", "num_available_tools": 4, "available_tools": [TOOL_PLAY_MUSIC, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 0},

  {"id": 221, "prompt": "Send a message and set a timer for 20 minutes.", "num_available_tools": 6, "available_tools": [TOOL_SEND_MESSAGE, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 222, "prompt": "Create a reminder and check the weather.", "num_available_tools": 6, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 223, "prompt": "Search for Emma then call her.", "num_available_tools": 5, "available_tools": [TOOL_SEARCH_CONTACTS, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 0},
  {"id": 224, "prompt": "Remind me to water plants and set a timer.", "num_available_tools": 6, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 225, "prompt": "Text John if it's sunny tomorrow.", "num_available_tools": 6, "available_tools": [TOOL_SEND_MESSAGE, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC], "route_label": 0},

  {"id": 226, "prompt": "Set a timer for dinner.", "num_available_tools": 4, "available_tools": [TOOL_SET_TIMER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 0},
  {"id": 227, "prompt": "Remind me in 20.", "num_available_tools": 4, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 0},
  {"id": 228, "prompt": "Wake me up before my meeting.", "num_available_tools": 5, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 0},
  {"id": 229, "prompt": "Tell Bob I'm outside.", "num_available_tools": 5, "available_tools": [TOOL_SEND_MESSAGE, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 0},
  {"id": 230, "prompt": "Play some music and check the weather.", "num_available_tools": 6, "available_tools": [TOOL_PLAY_MUSIC, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 0},

  {"id": 231, "prompt": "Remind me about the appointment next week.", "num_available_tools": 4, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 0},
  {"id": 232, "prompt": "Set an alarm around 8ish.", "num_available_tools": 4, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 0},
  {"id": 233, "prompt": "Find the newest contact and message them.", "num_available_tools": 6, "available_tools": [TOOL_SEARCH_CONTACTS, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 234, "prompt": "Play my workout stuff.", "num_available_tools": 4, "available_tools": [TOOL_PLAY_MUSIC, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 0},
  {"id": 235, "prompt": "Set something for 30 minutes from now.", "num_available_tools": 5, "available_tools": [TOOL_SET_TIMER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 0},

  {"id": 236, "prompt": "If it's hot, remind me to bring water.", "num_available_tools": 6, "available_tools": [TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 237, "prompt": "Text Anna and set an alarm.", "num_available_tools": 6, "available_tools": [TOOL_SEND_MESSAGE, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 238, "prompt": "Create a reminder for tomorrow.", "num_available_tools": 4, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 0},
  {"id": 239, "prompt": "Wake me up and tell me the weather.", "num_available_tools": 6, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 240, "prompt": "Send a message to whoever texted me last.", "num_available_tools": 6, "available_tools": [TOOL_SEND_MESSAGE, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC], "route_label": 0},

  {"id": 241, "prompt": "Set an alarm and remind me to call Mom.", "num_available_tools": 6, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 242, "prompt": "Play music if it's raining.", "num_available_tools": 6, "available_tools": [TOOL_PLAY_MUSIC, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 0},
  {"id": 243, "prompt": "Find John and check the weather in London.", "num_available_tools": 6, "available_tools": [TOOL_SEARCH_CONTACTS, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 244, "prompt": "Remind me at some point today.", "num_available_tools": 4, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 0},
  {"id": 245, "prompt": "Text Dave something funny.", "num_available_tools": 5, "available_tools": [TOOL_SEND_MESSAGE, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 0},

  {"id": 246, "prompt": "Set an alarm and a timer for 10 minutes.", "num_available_tools": 6, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 247, "prompt": "Create a reminder for when I get home.", "num_available_tools": 4, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 0},
  {"id": 248, "prompt": "Play whatever was playing yesterday.", "num_available_tools": 5, "available_tools": [TOOL_PLAY_MUSIC, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 0},
  {"id": 249, "prompt": "Message Chris and check the weather.", "num_available_tools": 6, "available_tools": [TOOL_SEND_MESSAGE, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 250, "prompt": "Set something up so I wake up before sunrise.", "num_available_tools": 5, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 0},

  {"id": 251, "prompt": "Set an alarm and send a message to John saying I'm awake.", "num_available_tools": 5, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 0},
  {"id": 252, "prompt": "Check the weather in Paris and remind me to bring an umbrella.", "num_available_tools": 6, "available_tools": [TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 253, "prompt": "Find Sarah and tell her I'll be late.", "num_available_tools": 5, "available_tools": [TOOL_SEARCH_CONTACTS, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 0},
  {"id": 254, "prompt": "Remind me sometime tomorrow to call Mike.", "num_available_tools": 4, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 0},
  {"id": 255, "prompt": "Wake me up early if it's sunny.", "num_available_tools": 6, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC], "route_label": 0},

  {"id": 256, "prompt": "Play music and set a 20 minute timer.", "num_available_tools": 6, "available_tools": [TOOL_PLAY_MUSIC, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 0},
  {"id": 257, "prompt": "Text Anna and check the weather in Tokyo.", "num_available_tools": 6, "available_tools": [TOOL_SEND_MESSAGE, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 258, "prompt": "Set something for later today.", "num_available_tools": 4, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 0},
  {"id": 259, "prompt": "Remind me about the meeting next Friday.", "num_available_tools": 4, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 0},
  {"id": 260, "prompt": "Tell Bob I'll be there soon.", "num_available_tools": 5, "available_tools": [TOOL_SEND_MESSAGE, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 0},
  {"id": 261, "prompt": "Set an alarm for around eight.", "num_available_tools": 4, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 0},
  {"id": 262, "prompt": "Play something upbeat for my workout.", "num_available_tools": 5, "available_tools": [TOOL_PLAY_MUSIC, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 0},
  {"id": 263, "prompt": "Find the latest contact and message them hello.", "num_available_tools": 6, "available_tools": [TOOL_SEARCH_CONTACTS, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 264, "prompt": "Remind me in a couple of hours to check the oven.", "num_available_tools": 5, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_SEARCH_CONTACTS], "route_label": 0},
  {"id": 265, "prompt": "Wake me up before sunrise.", "num_available_tools": 4, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 0},
  {"id": 266, "prompt": "Check the weather and play relaxing music.", "num_available_tools": 6, "available_tools": [TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 267, "prompt": "Set a timer and message John.", "num_available_tools": 6, "available_tools": [TOOL_SET_TIMER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 0},
  {"id": 268, "prompt": "Create a reminder and send a message.", "num_available_tools": 6, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 269, "prompt": "Search for Emily then tell her good luck.", "num_available_tools": 6, "available_tools": [TOOL_SEARCH_CONTACTS, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 270, "prompt": "Set something up so I remember my appointment.", "num_available_tools": 5, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_SEARCH_CONTACTS], "route_label": 0},

  {"id": 271, "prompt": "If it's raining tomorrow, remind me to bring boots.", "num_available_tools": 6, "available_tools": [TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 272, "prompt": "Play my favorite playlist and set an alarm.", "num_available_tools": 6, "available_tools": [TOOL_PLAY_MUSIC, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 0},
  {"id": 273, "prompt": "Tell Alex thanks and check the weather.", "num_available_tools": 6, "available_tools": [TOOL_SEND_MESSAGE, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 274, "prompt": "Set a timer for dinner and play some music.", "num_available_tools": 6, "available_tools": [TOOL_SET_TIMER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 0},
  {"id": 275, "prompt": "Remind me later to email Sarah.", "num_available_tools": 4, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 0},
  {"id": 276, "prompt": "Wake me up and tell me the temperature outside.", "num_available_tools": 6, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 277, "prompt": "Send a message to whoever called me last.", "num_available_tools": 6, "available_tools": [TOOL_SEND_MESSAGE, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 278, "prompt": "Set an alarm and a reminder for tomorrow.", "num_available_tools": 6, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 279, "prompt": "Check the weather if it's cloudy and text Mike.", "num_available_tools": 6, "available_tools": [TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 280, "prompt": "Play something similar to what I played yesterday.", "num_available_tools": 5, "available_tools": [TOOL_PLAY_MUSIC, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 0},

  {"id": 281, "prompt": "Remind me about my dentist appointment next month.", "num_available_tools": 4, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 0},
  {"id": 282, "prompt": "Set a timer for when the food is done.", "num_available_tools": 4, "available_tools": [TOOL_SET_TIMER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 0},
  {"id": 283, "prompt": "Tell Chris I'll call later and set an alarm.", "num_available_tools": 6, "available_tools": [TOOL_SEND_MESSAGE, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 284, "prompt": "Find John and check if it's sunny in London.", "num_available_tools": 6, "available_tools": [TOOL_SEARCH_CONTACTS, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 285, "prompt": "Play music for studying and remind me in 30.", "num_available_tools": 6, "available_tools": [TOOL_PLAY_MUSIC, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 0},
  {"id": 286, "prompt": "Wake me up at some point tomorrow.", "num_available_tools": 4, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 0},
  {"id": 287, "prompt": "Set something for when I get home.", "num_available_tools": 5, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_SEARCH_CONTACTS], "route_label": 0},
  {"id": 288, "prompt": "Text the group chat that I'm running late.", "num_available_tools": 5, "available_tools": [TOOL_SEND_MESSAGE, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 0},
  {"id": 289, "prompt": "Create a reminder for the usual time.", "num_available_tools": 4, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 0},
  {"id": 290, "prompt": "Check tomorrow's weather and set an alarm accordingly.", "num_available_tools": 6, "available_tools": [TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC], "route_label": 0},

  {"id": 291, "prompt": "Play relaxing music if it's raining.", "num_available_tools": 6, "available_tools": [TOOL_PLAY_MUSIC, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 0},
  {"id": 292, "prompt": "Set an alarm and text Anna good morning.", "num_available_tools": 6, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 293, "prompt": "Find my manager and tell him thanks.", "num_available_tools": 5, "available_tools": [TOOL_SEARCH_CONTACTS, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 0},
  {"id": 294, "prompt": "Remind me before lunch to take my meds.", "num_available_tools": 4, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 0},
  {"id": 295, "prompt": "Wake me up and start my playlist.", "num_available_tools": 6, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 296, "prompt": "Send a message and check the weather.", "num_available_tools": 6, "available_tools": [TOOL_SEND_MESSAGE, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 297, "prompt": "Set a timer and remind me to check it.", "num_available_tools": 6, "available_tools": [TOOL_SET_TIMER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 0},
  {"id": 298, "prompt": "Tell Bob it's cold in New York.", "num_available_tools": 5, "available_tools": [TOOL_SEND_MESSAGE, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 0},
  {"id": 299, "prompt": "Play some jazz and set a 10 minute timer.", "num_available_tools": 6, "available_tools": [TOOL_PLAY_MUSIC, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 0},
  {"id": 300, "prompt": "Remind me whenever you think it's appropriate.", "num_available_tools": 4, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 0},

  {"id": 301, "prompt": "Set an alarm if the weather is hot tomorrow.", "num_available_tools": 6, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 302, "prompt": "Check the weather and remind me to pack.", "num_available_tools": 6, "available_tools": [TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 303, "prompt": "Text John and search for Emma.", "num_available_tools": 6, "available_tools": [TOOL_SEND_MESSAGE, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 304, "prompt": "Set a reminder and an alarm for tomorrow morning.", "num_available_tools": 6, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 305, "prompt": "Play music that fits the weather.", "num_available_tools": 6, "available_tools": [TOOL_PLAY_MUSIC, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 0},

  {"id": 306, "prompt": "Remind me about that thing we talked about.", "num_available_tools": 4, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 0},
  {"id": 307, "prompt": "Wake me up when it's bright outside.", "num_available_tools": 4, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 0},
  {"id": 308, "prompt": "Send a message to the newest contact.", "num_available_tools": 5, "available_tools": [TOOL_SEND_MESSAGE, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 0},
  {"id": 309, "prompt": "Check the weather if I'm traveling tomorrow.", "num_available_tools": 6, "available_tools": [TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 310, "prompt": "Set a timer and text whoever is free.", "num_available_tools": 6, "available_tools": [TOOL_SET_TIMER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 0},

  {"id": 311, "prompt": "Play the same song as yesterday.", "num_available_tools": 5, "available_tools": [TOOL_PLAY_MUSIC, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 0},
  {"id": 312, "prompt": "Remind me about dinner next week.", "num_available_tools": 4, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 0},
  {"id": 313, "prompt": "Tell my boss I'm on the way.", "num_available_tools": 5, "available_tools": [TOOL_SEND_MESSAGE, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 0},
  {"id": 314, "prompt": "Set something up for after work.", "num_available_tools": 5, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_SEARCH_CONTACTS], "route_label": 0},
  {"id": 315, "prompt": "Wake me up and check tomorrow's weather.", "num_available_tools": 6, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC], "route_label": 0},

  {"id": 316, "prompt": "Send a message and set a reminder.", "num_available_tools": 6, "available_tools": [TOOL_SEND_MESSAGE, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 317, "prompt": "Find Anna and see what the weather is.", "num_available_tools": 6, "available_tools": [TOOL_SEARCH_CONTACTS, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 318, "prompt": "Play something fun and set a timer.", "num_available_tools": 6, "available_tools": [TOOL_PLAY_MUSIC, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 0},
  {"id": 319, "prompt": "Remind me before my usual time.", "num_available_tools": 4, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 0},
  {"id": 320, "prompt": "Set an alarm and check if it's raining.", "num_available_tools": 6, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC], "route_label": 0},

  {"id": 321, "prompt": "Check the weather and wake me up if it's cold.", "num_available_tools": 6, "available_tools": [TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 322, "prompt": "Text the last person I called.", "num_available_tools": 5, "available_tools": [TOOL_SEND_MESSAGE, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 0},
  {"id": 323, "prompt": "Set a timer for when it's ready.", "num_available_tools": 4, "available_tools": [TOOL_SET_TIMER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 0},
  {"id": 324, "prompt": "Play music and remind me to stretch.", "num_available_tools": 6, "available_tools": [TOOL_PLAY_MUSIC, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 0},
  {"id": 325, "prompt": "Find my coworker and send a message.", "num_available_tools": 6, "available_tools": [TOOL_SEARCH_CONTACTS, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_PLAY_MUSIC], "route_label": 0},

  {"id": 326, "prompt": "Set something for early tomorrow.", "num_available_tools": 4, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 0},
  {"id": 327, "prompt": "Wake me up and send a message.", "num_available_tools": 6, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 328, "prompt": "Remind me in a few hours.", "num_available_tools": 4, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 0},
  {"id": 329, "prompt": "Play the usual and check the weather.", "num_available_tools": 6, "available_tools": [TOOL_PLAY_MUSIC, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 0},
  {"id": 330, "prompt": "Text whoever is free tonight.", "num_available_tools": 5, "available_tools": [TOOL_SEND_MESSAGE, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 0},

  {"id": 331, "prompt": "Set an alarm and a timer.", "num_available_tools": 6, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 332, "prompt": "Check if it's sunny tomorrow and play music.", "num_available_tools": 6, "available_tools": [TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 333, "prompt": "Send a message and check the temperature.", "num_available_tools": 6, "available_tools": [TOOL_SEND_MESSAGE, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 334, "prompt": "Remind me whenever it's convenient.", "num_available_tools": 4, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 0},
  {"id": 335, "prompt": "Wake me up at the right time.", "num_available_tools": 4, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 0},

  {"id": 336, "prompt": "Set something so I don't oversleep.", "num_available_tools": 5, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 0},
  {"id": 337, "prompt": "Tell John it's sunny outside.", "num_available_tools": 5, "available_tools": [TOOL_SEND_MESSAGE, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 0},
  {"id": 338, "prompt": "Play something that matches my mood.", "num_available_tools": 5, "available_tools": [TOOL_PLAY_MUSIC, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER], "route_label": 0},
  {"id": 339, "prompt": "Remind me before it's too late.", "num_available_tools": 4, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 0},
  {"id": 340, "prompt": "Check tomorrow's weather and wake me up.", "num_available_tools": 6, "available_tools": [TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC], "route_label": 0},

  {"id": 341, "prompt": "Send a message and play music.", "num_available_tools": 6, "available_tools": [TOOL_SEND_MESSAGE, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 342, "prompt": "Set a timer and check the weather.", "num_available_tools": 6, "available_tools": [TOOL_SET_TIMER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 0},
  {"id": 343, "prompt": "Find Sarah and remind me to call her.", "num_available_tools": 6, "available_tools": [TOOL_SEARCH_CONTACTS, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 344, "prompt": "Play music if it's cold outside.", "num_available_tools": 6, "available_tools": [TOOL_PLAY_MUSIC, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 0},
  {"id": 345, "prompt": "Set something for next month.", "num_available_tools": 4, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 0},

  {"id": 346, "prompt": "Wake me up and tell Bob good morning.", "num_available_tools": 6, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 347, "prompt": "Remind me about the usual appointment.", "num_available_tools": 4, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE], "route_label": 0},
  {"id": 348, "prompt": "Check the weather and play the news.", "num_available_tools": 6, "available_tools": [TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 349, "prompt": "Text Anna and set something up.", "num_available_tools": 6, "available_tools": [TOOL_SEND_MESSAGE, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC], "route_label": 0},

  {"id": 350, "prompt": "Set an alarm for 7 AM, check the weather in London, and send a message to John saying good morning.", "num_available_tools": 6, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 351, "prompt": "Find Sarah in my contacts, send her a message saying I'm late, and start a 20 minute timer.", "num_available_tools": 6, "available_tools": [TOOL_SEARCH_CONTACTS, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 352, "prompt": "Check the weather in Paris, create a reminder titled 'Bring umbrella' at 8:00 AM, and text Mike about it.", "num_available_tools": 7, "available_tools": [TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC, TOOL_SET_TIMER], "route_label": 0},
  {"id": 353, "prompt": "Set a timer for 15 minutes, play my workout playlist, and send a message to Alex saying starting now.", "num_available_tools": 6, "available_tools": [TOOL_SET_TIMER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 0},
  {"id": 354, "prompt": "Search for Emma in my contacts, message her good luck, and set an alarm for 6:30 AM.", "num_available_tools": 6, "available_tools": [TOOL_SEARCH_CONTACTS, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 355, "prompt": "Check the weather in Tokyo, play some relaxing music, and set a reminder titled 'Meditate' at 9:00 PM.", "num_available_tools": 7, "available_tools": [TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC, TOOL_SET_TIMER], "route_label": 0},
  {"id": 356, "prompt": "Set an alarm for 8 AM, set a timer for 10 minutes, and send a message to Lisa saying wake up.", "num_available_tools": 6, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 357, "prompt": "Find John in my contacts, check the weather in New York, and remind me to call him at 5:00 PM.", "num_available_tools": 7, "available_tools": [TOOL_SEARCH_CONTACTS, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_PLAY_MUSIC, TOOL_SET_TIMER], "route_label": 0},
  {"id": 358, "prompt": "Play the playlist 'Focus', set a timer for 25 minutes, and create a reminder titled 'Review notes' at 6:00 PM.", "num_available_tools": 7, "available_tools": [TOOL_PLAY_MUSIC, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_SET_TIMER], "route_label": 0},
  {"id": 359, "prompt": "Set a reminder titled 'Gym' at 7:00 PM, check the weather in Singapore, and text Ryan about the plan.", "num_available_tools": 7, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC, TOOL_SET_TIMER], "route_label": 0},

  {"id": 360, "prompt": "Search for Olivia in my contacts, send her a message saying call me, and play her favorite song.", "num_available_tools": 7, "available_tools": [TOOL_SEARCH_CONTACTS, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_PLAY_MUSIC, TOOL_SET_TIMER], "route_label": 0},
  {"id": 361, "prompt": "Set an alarm for 6:45 AM, create a reminder titled 'Breakfast' at 7:30 AM, and start a 5 minute timer.", "num_available_tools": 6, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 362, "prompt": "Check the weather in Berlin, message Tom about it, and set a reminder titled 'Pack jacket' at 9:00 PM.", "num_available_tools": 7, "available_tools": [TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC, TOOL_SET_TIMER], "route_label": 0},
  {"id": 363, "prompt": "Find Chloe in my contacts, text her good morning, and set an alarm for 7:15 AM.", "num_available_tools": 6, "available_tools": [TOOL_SEARCH_CONTACTS, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 364, "prompt": "Play my workout playlist, set a 30 minute timer, and send a message to Mike saying starting workout.", "num_available_tools": 6, "available_tools": [TOOL_PLAY_MUSIC, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 0},
  {"id": 365, "prompt": "Set a timer for 12 minutes, check the weather in Madrid, and remind me to water plants at 8:00 PM.", "num_available_tools": 7, "available_tools": [TOOL_SET_TIMER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 366, "prompt": "Search for Daniel, send him a message saying meeting confirmed, and create a reminder titled 'Prepare slides' at 10:00 AM.", "num_available_tools": 7, "available_tools": [TOOL_SEARCH_CONTACTS, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_PLAY_MUSIC, TOOL_SET_TIMER], "route_label": 0},
  {"id": 367, "prompt": "Set an alarm for 9:00 AM, play the playlist 'Morning Vibes', and check the weather in Rome.", "num_available_tools": 6, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 368, "prompt": "Check the weather in Sydney, send a message to Anna about it, and set a timer for 40 minutes.", "num_available_tools": 6, "available_tools": [TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 369, "prompt": "Create a reminder titled 'Pay bills' at 8:00 PM, search for Sarah, and send her a message saying done.", "num_available_tools": 7, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC, TOOL_SET_TIMER], "route_label": 0},

  {"id": 370, "prompt": "Set a timer for 50 minutes, play the playlist 'Deep Focus', and text Chris saying studying now.", "num_available_tools": 6, "available_tools": [TOOL_SET_TIMER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 0},
  {"id": 371, "prompt": "Find Emma in my contacts, check the weather in Oslo, and set an alarm for 6:00 AM.", "num_available_tools": 7, "available_tools": [TOOL_SEARCH_CONTACTS, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_PLAY_MUSIC, TOOL_SET_TIMER], "route_label": 0},
  {"id": 372, "prompt": "Set an alarm for 5:30 AM, create a reminder titled 'Morning run' at 6:00 AM, and play the playlist 'Run Mix'.", "num_available_tools": 7, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC, TOOL_SET_TIMER], "route_label": 0},
  {"id": 373, "prompt": "Check the weather in Dubai, play relaxing music, and send a message to Mike saying it's hot.", "num_available_tools": 7, "available_tools": [TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC, TOOL_SET_TIMER], "route_label": 0},
  {"id": 374, "prompt": "Search for John in my contacts, send him a message saying see you, and set a 15 minute timer.", "num_available_tools": 6, "available_tools": [TOOL_SEARCH_CONTACTS, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 375, "prompt": "Set a reminder titled 'Team call' at 3:00 PM, check the weather in London, and play the playlist 'Focus'.", "num_available_tools": 7, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC, TOOL_SET_TIMER], "route_label": 0},
  {"id": 376, "prompt": "Play the playlist 'Evening Chill', set a timer for 20 minutes, and text Anna saying relaxing now.", "num_available_tools": 6, "available_tools": [TOOL_PLAY_MUSIC, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 0},
  {"id": 377, "prompt": "Set an alarm for 7:00 AM, check the weather in Barcelona, and send a message to Liam saying ready.", "num_available_tools": 6, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 378, "prompt": "Find Sophia in my contacts, message her good night, and set a reminder titled 'Call mom' at 9:00 AM.", "num_available_tools": 7, "available_tools": [TOOL_SEARCH_CONTACTS, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_PLAY_MUSIC, TOOL_SET_TIMER], "route_label": 0},
  {"id": 379, "prompt": "Check the weather in Amsterdam, create a reminder titled 'Bring coat' at 8:00 AM, and set a timer for 5 minutes.", "num_available_tools": 7, "available_tools": [TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC, TOOL_SET_TIMER], "route_label": 0},

  {"id": 380, "prompt": "Set a timer for 30 minutes, send a message to Mark saying meeting soon, and play the playlist 'Office Beats'.", "num_available_tools": 6, "available_tools": [TOOL_SET_TIMER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 0},
  {"id": 381, "prompt": "Search for Olivia, check the weather in Zurich, and set an alarm for 6:20 AM.", "num_available_tools": 7, "available_tools": [TOOL_SEARCH_CONTACTS, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_PLAY_MUSIC, TOOL_SET_TIMER], "route_label": 0},
  {"id": 382, "prompt": "Create a reminder titled 'Dinner' at 7:00 PM, play some music, and send a message to Chloe saying leaving now.", "num_available_tools": 7, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC, TOOL_SET_TIMER], "route_label": 0},
  {"id": 383, "prompt": "Set an alarm for 8:30 AM, set a timer for 10 minutes, and check the weather in Vienna.", "num_available_tools": 6, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 384, "prompt": "Find Daniel, message him good morning, and play the playlist 'Acoustic'.", "num_available_tools": 6, "available_tools": [TOOL_SEARCH_CONTACTS, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 385, "prompt": "Check the weather in Helsinki, set a reminder titled 'Pack gloves' at 9:00 PM, and send a message to Ryan.", "num_available_tools": 7, "available_tools": [TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC, TOOL_SET_TIMER], "route_label": 0},
  {"id": 386, "prompt": "Set a timer for 60 minutes, create a reminder titled 'Stretch' at 8:00 PM, and play relaxing music.", "num_available_tools": 7, "available_tools": [TOOL_SET_TIMER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 387, "prompt": "Search for Emma, send her a message saying on my way, and check the weather in Madrid.", "num_available_tools": 7, "available_tools": [TOOL_SEARCH_CONTACTS, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_PLAY_MUSIC, TOOL_SET_TIMER], "route_label": 0},
  {"id": 388, "prompt": "Set an alarm for 6:00 AM, play the playlist 'Morning Energy', and create a reminder titled 'Breakfast' at 7:00 AM.", "num_available_tools": 7, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC, TOOL_SET_TIMER], "route_label": 0},
  {"id": 389, "prompt": "Check the weather in Copenhagen, text Anna about it, and set a timer for 15 minutes.", "num_available_tools": 6, "available_tools": [TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC], "route_label": 0},

  {"id": 390, "prompt": "Find Lucas in my contacts, send him a message saying see you soon, and set a reminder titled 'Meeting' at 2:00 PM.", "num_available_tools": 7, "available_tools": [TOOL_SEARCH_CONTACTS, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_PLAY_MUSIC, TOOL_SET_TIMER], "route_label": 0},
  {"id": 391, "prompt": "Set a timer for 25 minutes, play the playlist 'Study', and check the weather in Oslo.", "num_available_tools": 6, "available_tools": [TOOL_SET_TIMER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS], "route_label": 0},
  {"id": 392, "prompt": "Create a reminder titled 'Doctor' at 10:00 AM, search for Sarah, and send her a message saying confirmed.", "num_available_tools": 7, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC, TOOL_SET_TIMER], "route_label": 0},
  {"id": 393, "prompt": "Set an alarm for 7:00 AM, check the weather in Prague, and play the playlist 'Wake Up'.", "num_available_tools": 6, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 394, "prompt": "Search for John, message him good luck, and set a timer for 10 minutes.", "num_available_tools": 6, "available_tools": [TOOL_SEARCH_CONTACTS, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 395, "prompt": "Check the weather in Budapest, create a reminder titled 'Bring scarf' at 8:00 PM, and play relaxing music.", "num_available_tools": 7, "available_tools": [TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC, TOOL_SET_TIMER], "route_label": 0},
  {"id": 396, "prompt": "Set a reminder titled 'Call boss' at 9:00 AM, set an alarm for 8:30 AM, and send a message to Mike.", "num_available_tools": 7, "available_tools": [TOOL_CREATE_REMINDER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC, TOOL_SET_TIMER], "route_label": 0},
  {"id": 397, "prompt": "Find Chloe in my contacts, check the weather in Rome, and play her favorite song.", "num_available_tools": 7, "available_tools": [TOOL_SEARCH_CONTACTS, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_PLAY_MUSIC, TOOL_SET_TIMER], "route_label": 0},
  {"id": 398, "prompt": "Set a timer for 45 minutes, send a message to Anna saying starting now, and check the weather in Paris.", "num_available_tools": 7, "available_tools": [TOOL_SET_TIMER, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC], "route_label": 0},
  {"id": 399, "prompt": "Play the playlist 'Chill Evening', set a reminder titled 'Tea break' at 6:00 PM, and search for Liam.", "num_available_tools": 7, "available_tools": [TOOL_PLAY_MUSIC, TOOL_GET_WEATHER, TOOL_SET_ALARM, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_SET_TIMER], "route_label": 0},

  {"id": 400, "prompt": "Set an alarm for 6:15 AM, check the weather in London, send a message to Sarah saying good morning, and start a 10 minute timer.", "num_available_tools": 7, "available_tools": [TOOL_SET_ALARM, TOOL_GET_WEATHER, TOOL_SEND_MESSAGE, TOOL_CREATE_REMINDER, TOOL_SEARCH_CONTACTS, TOOL_PLAY_MUSIC, TOOL_SET_TIMER], "route_label": 0}
]














