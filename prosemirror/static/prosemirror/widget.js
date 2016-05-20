/**
 * Browser component
 */

import "babel-polyfill";

import { jQuery as $ } from "django";
import { ProseMirror } from "prosemirror/dist/edit";
import "prosemirror/dist/markdown";
import "prosemirror/dist/menu/menubar";
import "prosemirror/dist/menu/tooltipmenu";
import "prosemirror/dist/inputrules/autoinput";
import { Schema } from "prosemirror/dist/model";

import maxiSpec from "./maxi-spec";
import microSpec from "./micro-spec";


/**
 * Prosemirror Wrapper class
 */
class ProseMirrorWrapper {

    /**
     * Constructor
     */
    constructor(target) {
        const $target = $(target);
        const $element = $("<div></div>");

        $element.addClass("prosemirror-editor");
        $element.insertBefore(target);

        this.$target = $target;
        this.options = $target.data("prosemirror-options");

        // Initialize
        try {
            $target.addClass("hide");

            this.editor = new ProseMirror({
                schema: new Schema(this.schema),
                place: $element.get(0),
                docFormat: "markdown",
                doc: $target.val(),
                menuBar: this.showMenuBar ? { float: true } : false,
                tooltipMenu: true,
                autoInput: true
            });

            // Register textarea updater
            this.editor.on("change", this.handleChange.bind(this));
        } catch(_) {
            $element.remove();
            $target.removeClass("hide");
        }
    }

    /**
     * schema settings
     */
    get schema() {
        if (this.options.schema === "micro") {
            return microSpec(this.options.inline_code);
        }
        // Default
        return maxiSpec(this.options.rule, this.options.inline_code);
    }

    /**
     * Get menu type
     */
    get showMenuBar() {
        return this.options.type === "bar";
    }

    /**
     * handle editor updates
     */
    handleChange() {
        this.$target.val(this.editor.getContent("markdown"));
    }

}


/**
 * Initialize once
 */
const initProseMirror = (item) => {
    const $item = $(item);
    const id = $item.attr("id");

    if ($item.data("prosemirror-field-id") !== id &&
            (hasFeinCMS() && !id.includes("__prefix__"))) {
        $item.data("prosemirror-field-wrapper", new ProseMirrorWrapper(item));
        $item.data("prosemirror-field-id", id);
    }
};


/**
 * Initialize all
 */
const initProseMirrors =
    () => $(".prosemirror-box").each((_, i) => initProseMirror(i));


/**
 * Fein Cms active detector
 */
const hasFeinCMS = () => !!window.contentblock_init_handlers;


/**
 * Bind initializers
 */
$(document).ready(() => {
    if (hasFeinCMS()) {
        window.contentblock_init_handlers.push(() => initProseMirrors());
    }
    initProseMirrors();
});
