# Instagram Follow List Scripts
Scripts to run on HTML files of followers and those you are following; it returns the usernames of those you follow who aren't following back.  Purpose is to help keep your following more organized and centralized. 

### How to Use
1. Get the data first. 
> Sign into your Instagram account >> Accounts Center >> Your Information and permissions >> Download your information >> Download or transfer information >> Click what info you want to download (followers and following is sufficient)


2. While downloading information from your Instagram, clone this repository to your local machine.

3. Instagram download should provide a followers.html and following.html file in a zip folder. Get these file paths and paste into the respective file path variables (`followers_file` and `following_file`) in the `igFollowers.py` file. 

4. Set up a virtual environment: 
```
python3 -m venv myenv
```
Activate the environment by running:
- on **macOS/Linux** 
    ```
    source myen/bin/activate
    ```
- on **Windows**
    ```
    myenv\Scripts\activate
    ``` 

Install necessary libraries:
```
pip install beautifulsoup4 lxml
```

5. We are ready to run the program now! Navigate to the directory containing the `igFollowers.py` file and run the command:
```
python3 igFollowers.py
``` 