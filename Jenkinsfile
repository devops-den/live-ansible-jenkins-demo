pipeline {
    agent any
    
    stages {
        stage('Invoke ansible playbook') {
            steps {
                ansiblePlaybook(
                    playbook: 'testmod.yml',
                    inventory: 'inventory.yml',
                    credentialsId: 'ansible-connect'
                )
            }
        }
    }
}