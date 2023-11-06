---

# Barcode & QR Code Generators API Using FastAPI

This guide provides a walkthrough on how to set up and deploy a Barcode and QR Code Generators API using FastAPI.
# Getting Started with the Python Script

### Step 1: Install Requirements

To run this project, you need to install the necessary dependencies which are listed in the `requirements.txt` file.

#### How to install requirements:

Open your terminal and run the following command to install the dependencies:

```bash
pip install -r requirements.txt
```

### Step 2: Run APIs Locally

To run the API server on your local machine, execute the following command:

```bash
uvicorn app.main:app --reload
```

---

# Testing the API

1. Run your FastAPI application.
2. Open your web browser.
3. Navigate to **http://localhost/docs** if you're running the application locally, or to the appropriate URL if it's hosted on a remote server. 

4. The Swagger UI will be displayed with all the operational endpoints.



5. **Explore the endpoints**: When you open the Swagger UI, you'll see a list of all the available endpoints, including the paths for barcode and QR code generation.

6. **Try out an endpoint**:
   - Click on the endpoint you want to test. For example, click on `GET` under `/BarcodeCode128/{text}` or `/QrCode/{text}`.
   - Click the "Try it out" button.
   - Enter the `text` you want to encode into the barcode or QR code in the respective field.
   - Click the "Execute" button.

7. **View the response**: Swagger UI will display the server's response. For the barcode and QR code endpoints, you should see a successful response with the generated image. You can click on the "Download" button to save the image.


## Deployment with Docker

Docker simplifies deployment by containerizing your application and its environment. Below are the steps to deploy your API using Docker.

### Step 1: Build a Docker Image

A Docker image can be created with the included Dockerfile. To build the image, run:

```bash
docker build -t myimage .
```



### Step 2: Run a Docker Container

After building the image, you can run it as a container. To start the container, use:

```bash
docker run -d --name mycontainer -p 80:80 myimage
```


## Making future changes with the python script
### generate requirements.txt

```bash
pip install pipreqs
pipreqs [path to your directory :3]
```





