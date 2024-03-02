## Terraform Infra Setup

Clone the repository in your local machine.

```bash
git clone https://github.com/mahesh-c-pathak/gcs_pipeline.git && \
cd terraform
```

Spin up the Infra -

- Initiate terraform and download the required dependencies-

  ```bash
  terraform init
  ```

- View the Terraform plan

  You will be asked to enter two values, the name of the GCS bucket you want to create and your GCP Project ID. Use the same values throughout the project. 

  ```bash
  terraform plan
  ```

- Apply the infra. 

  ```bash
  terraform apply
  ```

- Once you are done with the project. Teardown the infra using-

  ```bash
  terraform destroy
  ```

**Note:** The infra was setup a tad generously, you might not actually be fully utilizing the compute power. Feel free to reduce the instance sizes and test.
