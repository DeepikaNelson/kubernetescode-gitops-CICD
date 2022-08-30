from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, This is CI CD Pipeline using Jenkins and GitOps (ArgoCD) to dockerize your code, and deploy the container into a Kubernetes cluster.'
    echo 'thank you'
