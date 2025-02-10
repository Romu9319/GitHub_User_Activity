# GitHub_User_Activity
A simple command line interface (CLI) that it will allow us to obtain the latest activity from a Github user as well as the most common.

# Roadmap project URL
[https://roadmap.sh/projects/task-tracker](https://roadmap.sh/projects/github-user-activity)

# Installation 
1. Clone the repository 
    https://github.com/Romu9319/GitHub_User_Activity.git
2. Install dependencies
    ```bash
      pip install -r requirements.txt
    ```   
4. Run the CLI
    ```bash
      python cli.py --help
    ```
    
# Available Commands
1. Shows the last 5 events made by the user
    ```bash
      python cli.py last-events [user]
    ```
    - user: Enter the github username (Required)
    - Example:
       ```bash
          python cli.py last-events 'exampleUser:)'
       ```
    
2. Shows the number of events by type
    ```bash
      python cli.py github-activity [user]
    ```
     - user: Enter the github username (Required)
    - Example:
       ```bash
          python cli.py github-activity 'exampleUser:)'
       ```

3. Filter by event type
    ```bash
      python cli.py filter [user] [event_type]
    ```
    - user: Enter the github username (Required)
    - evente_type: Enter the type of event to search 
    - Example:
       ```bash
          python cli.py filter 'exampleUser:)' 'PushEvent'
       ```
