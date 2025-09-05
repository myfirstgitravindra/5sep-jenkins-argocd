pipeline {
    agent any
    stages {
        stage('git checkout') {
            steps {
               git branch: 'main', credentialsId: 'github-token', url: 'https://github.com/myfirstgitravindra/5sep-jenkins-argocd'
            }
        }
        stage('docker image build') {
            steps {
                 sh "docker build -t ravindra806/versionapp:${env.BUILD_NUMBER} ."
            }
        }
        stage('docker login and push') {
            steps {
             withCredentials([usernamePassword(credentialsId: 'docker-hub', passwordVariable: 'PWD', usernameVariable: 'USR')]) {
    sh "docker login -u ${USR} -p ${PWD}"
  sh "docker push ravindra806/versionapp:${env.BUILD_NUMBER}"
}
}
}
stage("Update Deployment and Push"){
    steps{
        withCredentials([gitUsernamePassword(credentialsId: 'github-token', gitToolName: 'Default')]) {
            sh """
            sed -i 's|image:.*|image: ravindra806/versionapp:${env.BUILD_NUMBER}|' ./K8s/deployment.yaml
            git config user.name "Jenkins Server"
            git config user.email "jenkins@automation.com"
            git add .
            git commit -m "Docker tag updated by jenkins [ci skip]"
            git push origin main
            """
        }
    }
}
}
}