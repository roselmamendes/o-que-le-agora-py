case "$1"
 in
 build-image) sudo docker build -t o-que-le-agora-py .;;
 run-container) sudo docker run --rm -p 5000:5000 -v PWD:/usr/src/app -it o-que-le-agora-py;;
 *)
            echo $"Usage: $0 {build-image|run-container}"
            exit 1
esac