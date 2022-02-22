pipeline {
    agent any
        tools {
            maven "3.8.4"
                }
        stages {
        stage ('Python') {
            steps {
                bat 'S_with_json.py'
            }
        }

        stage ('Server'){
            steps {
                rtServer (
                    id: "Artifactory",
                    url: 'http://127.0.0.1:8081/artifactory',
                    username: 'admin',
                    password: 'Sriniv@s7',
                    bypassProxy: true,
                    timeout: 300
                        )

            }
        }
        stage ('Upload'){
            steps{
                rtUplode (
                 serverId:"Artifactory",
                  spec: '''{
                   "files": [
                      {
                      "pattern": ".zip",
                      "target": "logic-ops-lab-libs-snapshot-local"
                      }
                            ]
                           }''',
                        )
            }
        }
        stage ('Publish build info') {
            steps {
                rtPublishBuildInfo (
                    serverId: "Artifactory"
                )
            }
        }
    }
}
