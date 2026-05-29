def call(imageName, imageTag) {

    echo "Building Docker Image: ${imageName}:${imageTag}"

    sh "docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} ."
}
