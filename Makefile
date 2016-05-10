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

# Default
all: build

# Release
build: clean scss browserify package

# Development build
set_dev:
	@echo -e "\nActivating development modus\n"
	$(eval DEBUG = 1)

# Clean
clean:
	@rm -rf prosemirror/static/prosemirror/*.min.*

# Scss
scss:
	@mkdir -p $(BUILD_CACHE_DIR)
	@if [[ $(DEBUG) == 1 ]]; then \
		$(NPM_BIN)/node-sass \
			prosemirror/static/prosemirror/widget.scss \
			$(BUILD_CACHE_DIR)/widget.css \
			--output-style nested \
			--source-map $(BUILD_CACHE_DIR)/widget.css.map; \
		cat $(BUILD_CACHE_DIR)/widget.css | \
			$(NPM_BIN)/postcss \
			--map \
			--use autoprefixer > \
			prosemirror/static/prosemirror/widget.min.css; \
	else \
		$(NPM_BIN)/node-sass \
			prosemirror/static/prosemirror/widget.scss \
			$(BUILD_CACHE_DIR)/widget.css \
			--output-style compressed; \
		cat $(BUILD_CACHE_DIR)/widget.css | \
			$(NPM_BIN)/postcss --use autoprefixer > \
			prosemirror/static/prosemirror/widget.min.css; \
	fi

# Browserify
browserify:
	@if [[ $(DEBUG) == 1 ]]; then \
		$(NPM_BIN)/browserify -d \
			prosemirror/static/prosemirror/widget.js | \
			$(NPM_BIN)/exorcist prosemirror/static/prosemirror/widget.min.js.map > \
			prosemirror/static/prosemirror/widget.min.js; \
	else \
		$(NPM_BIN)/browserify -g uglifyify \
			prosemirror/static/prosemirror/widget.js | \
			$(NPM_BIN)/uglifyjs -cm > \
			prosemirror/static/prosemirror/widget.min.js; \
	fi

# Build wheel
package:
	@python setup.py sdist bdist_wheel
