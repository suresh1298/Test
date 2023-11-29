# Test
To complete given  Assessment we need to fallow this steps

1. Taken a sample csv file in our case that is orders.csv in in that we are adding these many columns
        * Order ID,Customer ID,Order Date,Product ID,Product Name,Product Price,Quantity
2. Then we are going to print what ever we required using csv file in our case we wer using
        * print(Order ID,Customer ID,Order Date,Product ID,Product Name,Product Price,Quantity)
3. writing test and analysis for our file withe name of test_orders_analysis.py
4. Dockerized services for the task and the test involves creating separate Docker containers for each.
        * Dockerfile.task
        * Dockerfile.test
5. We wer going to build the image with the help of docker file and using that image we will run as container
        * docker build -t your-task-service -f Dockerfile.task .
        * docker build -t your-test-service -f Dockerfile.test .
6. Running the container with these commands
        *docker run your-task-service
        *docker run your-test-service
   To automate entire process we wer going to use CI-CD tool which is Jenkins . this tool is used to reduce the manual intervension 
8. CI-CD Using Declerative pipline in jenkins we wer going to automate the task with the help of pipeline
