GOPATH := ${PWD}
export GOPATH

build: vet
	go build -v isubata

vet:
	go vet -v ./src/isubata/...
