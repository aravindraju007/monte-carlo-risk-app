### Abstract— 
The evolution of cloud technologies has paved the way for a slew of new prospects and business models, enabling on-demand, pay-as-you-go access to a pool of scalable resources and services. In this report, two cloud-based programmes are investigated to see how various components of them effect accessibility, as well as prices, security, and storage. This report outlines a basic web application that involves a number of cloud services to identify and evaluate the risk of adopting specific trading signals in a trading strategy. Finally, a demo of the application is shown, with results varying by parameter, as well as the service's running cost and satisfaction with the criteria.  
Keywords—NIST,AWS,GCP,EC2) 

### I. INTRODUCTION 
The system discussed in this article implements a web application which enables a user to practically detect and evaluate the risk of loss and the associated confidence for a specific trading signal using two top cloud service providers – 
GCP and AWS. The method employs the Monte Carlo simulation approach to generate a wide set of random price values and calculates the potential losses at 95 percent and 99 percent confidence levels. 

NIST SP800-145(National Institute of standard and Technology).Cloud computing is a methodology for providing on-demand network access to a shared pool of programmable computing resources that can be quickly supplied and released with minimal administration effort and service provider contact. The NIST guidelines and evaluation infrastructures are well recognised, and they successfully demonstrate the advantages of cloud computing over traditional IT infrastructures. This definition aids businesses in determining how to best utilise cloud resources and the degree to which cloud features satisfy the needs. 
The cloud model includes five main characteristics, according to the NIST definition: on-demand services, broad network access, resource pooling, rapid expansion or flexibility, and measured service. 

The goal here is to calculate overall risk of loss at the 95th and 99th percentiles using a set of simulated costs based on historical data. To accomplish this, AWS Lambda or EC2 services are employed. The user is given access to a web application that is hosted by Google App Engine. 
To have a better understanding of how the system works, look into the developer and user perspectives: 

### A. Developer 
The developer wants to take advantage of the cloud's scalability, on-demand services and resources to create an optimal solution while maintaining adequate resource management. GCP and AWS are two independent suppliers used by the developer. The application is hosted on GCP, which allows the developer to easily deploy and test any modifications. GAE as a Platform as a Service minimizes difficulty by allowing developers to operate remotely without the requirement for a physical server and to take advantage of other benefits which including storage and multiple computational capability as needed. The developer's attention is exclusively on the configuration, core code and an optimal scalable solution while using PaaS, which is detached from the underlying hardware. The developer hopes to save time by using parallel execution. The developer plans to save time and money by parallelizing execution and returning average risk levels to the user based on their inputs. This application's major goal is to permit on-demand activities to be conducted using a pool of resources, allowing it to scale as needed.There are two parts to the system: 

1.	Front- End: 
Platform as a Service (PaaS) is used to design the front end system. The GAE is used to host the complete application. Any modifications to the web application can also be analysed here as well. 
2.	Back End: 
 Using AWS Lambda or EC2 the simulations are executed, and all the  risk values are supplied to the main Python function. After that, HTML is used to show them on the webpage. 
 
### B. User 
In terms of user’s point of view, the self-service cloudhosted web application allows the user to access it remotely via a web browser from any user machines . The user interface region (front-end) contains a set of input entry boxes for entering necessary input values and the user can generate the result by simply clicking the submit icon. The results will be shown on the webpage. There is also a button to choose between lambda and EC2. The end user also can generate quick results thanks to the parallel threading option. Additionally, previous results can be viewed in the audit page. 

### II. FINAL ARCHITECTURE 
 
 
### A. Major System Components 
This web application is implemented using GCP and AWS as cloud providers. The Monte Carlo simulation and hence the production of risk levels at the back end are performed using AWS Lambda or EC2 services. while The front end of the application is hosted on Google Cloud Platform. Front-end and back-end components are the two primary types of parts that make up a web application system. 

1)	Back End: 
  a)	Amazon API Gateway: 
  b)	AWS defines an API gateway for requests and configuring integration responses. The REST API is used to redirect HTTP queries to AWS 
    Lambda 

  c)	AWS Lambda:
    AWS Lambda leverages recent history's mean and standard deviation to build a considerably bigger collection of values with similar 
    properties. Risk is calculated at the 95th and 99th percentiles and then returned to the main python code, which will then be 
    transferred to the webpage, where the user sees it on the front end.. 
  d)	EC2, AWS: 
     Similar to Lambda  Amazon's EC2 service can also be used to calculate signal risk. The key benefits of EC2 are its quick startup 
     time and scalability of compute capacity. 
3)	Front End.  
   a)	(GAE) Google App Engine: 
     A Google App Engine application uses serverless technologies to host and develop large-scale online apps. GAE is used to host the 
     web application, which may be visited and tested. The application establishes a connection and executes the user's request via the 
     REST API. The Python Flask framework is used to implement the system. The user can enter required inputs and examine the results 
     after launching the application. 
 
When the application first launches, the user is prompted to choose between AWS Lambda and Amazon EC2. Both services in this system are essentially offering an answer to the exact problem statement, however they are extremely different when compared to one another. For example, EC2 has a very quick startup time, whereas Lambda takes a little longer. EC2 also offers scalable computing performance, even at a higher cost of operation. As a result, even since they both offer solutions to the exact problem, the user must decide which option is best for them. 
 
 
### B. System Component Interactions 
Google App Engine is used to host the web application., and when accessed, it opens and shows a web page with a user input form for the end users to fill out. The user must then enter appropriate input values and choose a type of trading signal (Buy / Sell) . The user needs to additionally select a preferred service from the available options from the dropdown. The main function reads the data after the user inputs all values and clicks Submit. The mean and standard deviation of each signal are estimated, and an HTTP request will be sent to call the Lambda function using the API. After that, the Lambda function conducts a simulation and delivers the risk values output to the main python code. The average of risk values are then generated and shown in the structure of a table using the data from the parallel runs. When using the EC2 service, the same results should be expected. One of the most significant differences with both Lambda and EC2 is that only the Lambda function executes only when called, but EC2 must be up at all times. 




<img width="232" alt="image" src="https://github.com/user-attachments/assets/3c985a74-6d18-486e-8a9b-a5bc70994c79" />
                            System components' interactions 










