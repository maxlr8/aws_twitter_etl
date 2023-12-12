# twitter_etl

Welcome to the End-To-End Data Engineering Project using Airflow and Python! This project focuses on extracting data from Twitter using the Twitter API, and transforming the data using Python.

<div align="center">
  <img src="./Screenshots/1_Project_Workflow.jpg" alt="workflow" width=647 height=364>
</div>

<br>

Once the data is transformed, it is deployed on Airflow and AWS EC2, and ultimately storing the final results on Amazon S3.

<div align="center">
  <img src="./Screenshots/35_downloaded_csv.jpg" alt="workflow" width=647 height=364>
</div>

<br>

## Getting Started

To use this project, follow these steps:

1. **Twitter API Key:**
    - Obtain your Twitter API keys by creating a Twitter Developer account.
    - Update the `Twitter_API_Creds.env` file with your Twitter API keys.

2. **AWS Credentials:**
    - Ensure you have AWS credentials with access to EC2 and S3 services.

3. **Clone the Repository:**
    ```bash
    git clone https://github.com/your-username/your-project.git
    cd your-project
    ```

4. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```


## Implementation

Follow the [ScreenShots](./ScreenShots/) for implementation.
