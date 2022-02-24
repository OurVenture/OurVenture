GODIR="ourventure-backend\RestApi"
GOMAIN="ourventure-backend\RestApi\main.go"

if [ -d "$GODIR"]; then

    echo 'GODIR exists! RestApi folder has been created'
    if [-f "$GOMAIN" ]; then
        cd RestApi && go run main.go
    fi

else
    echo 'No GODIR ${GODIR} found, please ensure the RestApi folder has been created!'
    exit 1
fi 