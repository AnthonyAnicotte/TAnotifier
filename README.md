# TAnotifier

TAnotifier is my first personnal project programmed in Python. It's a script that connects to your Outlook mailbox and fetch the last mail from Marvin, the Epitech's corrector robot.
If a new TA has arrived, the script will send you a notification containing your project result (success percentage).

## Installation

This scripted has been originally developed to be hosted on a Raspberry Pi 4, and triggered by a Crontab Task.
You just have to clone the project configure the Crontab manager, 
and fill out the `TAconfig.py` (Epitech's student part) plus the `outlook/config.py` (Outlook connection mode).

## Usage
Once the script loaded on your server, download the [Wirepusher application](https://play.google.com/store/apps/details?id=com.mrivan.wirepusher&hl=en) and retrieve your token. <br>
Rename the `TAconfig.py.sample` to `TAconfig.py` and configure it as explained. Do the same thing for the `outlook/config.py.sample`
Don't forget to setup the Wirepusher Application to your convenience.

## Contributing
The Outlook library used to connect and perform actions on the Outlook mailbox is entirely made by *Rolly Maulana Awangga* (https://github.com/awangga/outlook). However, I made some changes to adapt his project to mine. <br/>
The Wirepusher [web]app (http://wirepusher.com/) is used to send notifications through API requests.

## Coming Soon
System to allow your course mates to receive notifications by giving you their token after downloading the Wirepusher application. <br>
Note that they will be notified even if they are not subscribed to the project. Be sure that you have the projects in common.

## License
This project is free-to-use. No licence applied. Feel free to fork/clone it and work on it.