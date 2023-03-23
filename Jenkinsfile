pipeline {
    agent any
    options {
        ansiColor('xterm')
    }
    
    stages {
        stage('Invoke ansible playbook') {
            steps {
                ansiblePlaybook(
                    playbook: 'testmod.yml',
                    inventory: 'inventory.yml',
                    credentialsId: 'ansible-connect',
                    colorized: true
                )
            }
        }
    }
}