docker run --name lamia_s3  ^
            -p 8055:8055 ^
            -p 4563-4599:4563-4599 ^
            -e SERVICES=s3,es ^
            -e DATA_DIR=/media  ^
            -e PORT_WEB_UI=8055 ^
            -e LAMBDA_EXECUTOR=docker ^
            -e HOST_TMP_FOLDER=C:\localstacktmp ^
            -e TMPDIR=/tmp/ ^
            -e user=root ^
            --mount source=C:\media,target=/media,type=bind,consistency=delegated ^
            --mount source=C:\localstacktmp,target=/tmp,type=bind,consistency=delegated ^
            localstack/localstack:latest