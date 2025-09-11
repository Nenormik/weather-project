pipeline {
    agent any 
    stages {
        stage('Build') {
            steps {
                script {
                    sh('''#!/bin/bash
                    ls -la
                    systemctl status docker
                    docker ps
                    docker build -t nenormik/dockrepo:latest .
                    docker images
                    echo "london" | docker run -i nenormik/dockrepo:latest
                    docker tag nenormik/dockrepo:latest nenormik/dockrepo:latest
                    docker push nenormik/dockrepo:latest
                    docker ps
                    docker images
                    docker rmi -f $(docker images -a -q)
                    docker images
                    docker ps''')
                }
            }
        }
    }
}
