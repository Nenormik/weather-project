pipeline {
    agent any 
    stages {
        stage('Build') {
            steps {
                script {
                    sh('''#!/bin/bash
                    ls -la
                    systemctl status docker
                    docker build -t envybranch:latest .
                    docker images
                    docker run -it envybranch:latest''')
                }
            }
        }
    }
}
