## GCP Overview

### Initial Setup

1. Create an account with your Google email ID 
2. Setup your first [project](https://console.cloud.google.com/) if you haven't already
    * eg. "gcs-pipeline", and note down the "Project ID" (we'll use this later when deploying infra with TF)
3. Create an ssh key in your local system in the .ssh folder
   * https://cloud.google.com/compute/docs/connect/create-ssh-keys
   * ssh-keygen -t rsa -f ~/.ssh/KEY_FILENAME -C USERNAME -b 2048
5. Add the public key (.pub) to your VM instance
   * https://cloud.google.com/compute/docs/connect/add-ssh-keys#expandable-2
6. Create a config file in your `.ssh` folder

     ```bash
     touch ~/.ssh/config
     ```
7. Copy the following snippet and replace with name,External IP of your VM. Username and path to the ssh private key

    ```bash
    Host <your VM instances name>
        HostName <External IP Address>
        User <username>
        IdentityFile <path/to/home/.ssh/keyfile>
    ```
8. Once you are setup, you can simply SSH into the servers using the below commands in separate terminals. Do not forget to change the IP address of VM restarts.

    ```bash
    ssh <your VM instances name>
    ```
9. Access VM from VScode
    * Enable vs code extension remote-ssh 
    * In VS Code, select Remote-SSH: Connect to Host... from the Command Palette (F1, Ctrl+Shift+P)
    * You will have to forward ports from your VM to your local machine for you to be able to see Kafka, Airflow UI.
10. Clone the repository in your local machine. we will use the setup.sh to install Anaconda, Docker, docker-compose on VM
    ```bash
    git clone https://github.com/mahesh-c-pathak/gcs_pipeline.git
    cd gcs_pipeline/scripts
    chmod +x vm_setup.sh
    ./vm_setup.sh
    ```

3. Setup [service account & authentication](https://cloud.google.com/docs/authentication/getting-started) for this project
    * Grant `Viewer` role to begin with.
    * Add these roles in addition to *Viewer* : **Storage Admin** + **Storage Object Admin** + **BigQuery Admin**
    * Download service-account-keys (.json) for auth.
4. Download [SDK](https://cloud.google.com/sdk/docs/quickstart) for local setup
5. Set environment variable to point to your downloaded GCP keys:
   ```shell
   export GOOGLE_APPLICATION_CREDENTIALS="<path/to/your/service-account-authkeys>.json"
   
   # Refresh token/session, and verify authentication
   gcloud auth activate-service-account --key-file $GOOGLE_APPLICATION_CREDENTIALS
   ```
   

 
