# Self Bot using discord.py-self


Keep your server consistently bumped without having to babysit your bump channel
---

## To Provide Obfuscation The Following Bump Times Are Provided

**all times must be converted to seconds**

_/youdo not need to use these times as you can just leave the default wait time of 2 hours set but there are provided for convience_

- 2 hours
- 2 hours & 5 mins
- 2 hours & 10 mins
- 2 hours & 15 mins


These times are set within a list of dictionaries in the following form:

7460 === 2 hours

**bump_times = [{'wait_time': 7460, 'in_use': True}, {'wait_time': 7800, 'in_use': False}]**

Within the file _helpers.py_ there is 3 methods: 
- one for selecting a time based on the **in_use** key's value 
- second method which resets all the **in_use** key's values to _False_  
- final method to choose a new time increment.

The dictionary to set to the current value for how long the bot should wait before executing the bump command is based off of choosing a random int between 0 and the length of the **bump_times** list.


### To run 
- first install **requirements.txt** using _python -m pip install -r requirements.txt_
- Change into the folders directory and run _python index.py_
- If you have a different bump prefix other than _!d bump_ you can change these values within config.py

---


### If you wish to not use these, a default **wait_time** variable has been set within _config.py_


