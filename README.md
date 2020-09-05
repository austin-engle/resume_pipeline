# resume_pipeline

This codebase will deploy my resume to an s3 bucket hosted by Cloudfront. The website will have a visitor counter which will communicate with a DynamoDB Database to keep track of the visitor number. All of this will be deployed via a webhook and automated.

## TODO
- Set up Route53 to point to CloudFront


## Completed

- Create Infrastructure
    - DynamoDB
    - S3 Bucket
    - CloudFront
    - Lambda
        - Read the current number, increment it by 1, write new number to dynamo, return number to webpage
        - No tests included as there is no input to lambda, all the code relies on itself. Running the code proves the tests. 
    - IAM Policies for everything
    - API Gateway

- Create Website (HTML, CSS, Javascript)
    - HTML & CSS Resume
    - Javscript Counter
        - Should call API Gateway to get

## Deployment Steps

- zip lambda code (if any changes were made)
- Deploy frontend-infrastructure
- upload all code to s3 bucket
- deploy backend infrastructure
- Profit

## Bugs
- There is a bug deploying the API Gateway. The lambda arn that is passed to it doesn't set correctly. If I go in an manually remove then add it again the API starts working. 
