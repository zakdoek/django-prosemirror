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
SASS_SOURCEMAP ?= 0

# Default
all: build

# Release
build: scss package
	
# Development build
set_dev:
	@echo -e "\nActivating development modus\n"
	$(eval DEBUG = 1)
	$(eval SASS_STYLE = nested)
	$(eval SASS_SOURCEMAP = prosemirror/static/prosemirror/widget.min.css.map)

# Scss
scss:
	@$(NPM_BIN)/node-sass \
		--output-style $(SASS_STYLE) \
		--source-map $(SASS_SOURCEMAP) \
		prosemirror/static/prosemirror/widget.scss \
		prosemirror/static/prosemirror/widget.min.css

# Browserify
browserify:

# Build wheel
package:
	@python setup.py sdist bdist_wheel
