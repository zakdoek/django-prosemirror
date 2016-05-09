###
# Builds this apps source
###

SHELL = /bin/bash

NODE_MODULES ?= node_modules
NPM_BIN = $(shell npm bin)
DEBUG = 0
BUILD_DIR ?= .build
BUILD_CACHE_DIR ?= .build-cache
SOURCE_DIR ?= ./
SASS_STYLE ?= compressed
SASS_SOURCEMAP ?= none

# Default
all: build

# Release
build: package
	
# Development build
set_dev:
	@echo -e "\nActivating development modus\n"
	$(eval DEBUG = 1)
	$(eval SASS_STYLE = nested)
	$(eval SASS_SOURCEMAP = file)

# Build wheel
package:
	@python setup.py sdist bdist_wheel
