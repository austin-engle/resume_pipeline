# resume_pipeline

This codebase will deploy my resume to an s3 bucket hosted by Cloudfront. The website will have a visitor counter which will communicate with a DynamoDB Database to keep track of the visitor number. All of this will be deployed via a webhook and automated. 


## TODO
- Create Website (HTML, CSS, Javascript)
      - HTML & CSS Resume
      - Javscript Counter
          - Should call API Gateway to get 
          
- Create Infrastructure
      - DynamoDB
      - S3 Bucket
      - API Gateway
      - Lambda
          - Read the current number, increment it by 1, write new number to dynamo, return number to webpage
          - Going to need to include tests for my lambda (Unit Tests?)
      - Cloudfront
      - IAM Policies for everything
      
- Create Pipeline for website
      - Pipeline should take website files and upload them to s3
      
- Create Pipeline for Lambda Functions (?) (If I have time)

- Set up Route53 to point to CloudFront
