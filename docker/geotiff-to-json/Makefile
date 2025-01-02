build:
	docker build -t geotiff-to-json-image .

run: 
	docker run -t -d --name geotiff-to-json geotiff-to-json-image


stop:
	docker stop geotiff-to-json
	docker remove geotiff-to-json

transform-sh:
	docker exec -it geotiff-to-json mkdir -p /code/app/output
	docker exec -it geotiff-to-json chmod +x /code/app/transform.sh
	docker exec -it geotiff-to-json /code/app/transform.sh

transform-py:
	docker exec -it geotiff-to-json python /code/app/convert_coordinates.py

test-gadm:
	docker exec -it geotiff-to-json python /code/app/gadm_test.py

download:
	mkdir -p ~/geotiff-to-json
	docker cp geotiff-to-json:/code/app/output ~/geotiff-to-json/output_$$(date +%s)

build-and-run:
	make stop
	make build
	make run

build-download-and-run:
	make stop
	make build
	make run
	make transform-py
	make download

build-and-run-gadm:
	make stop
	make build
	make run
	make test-gadm