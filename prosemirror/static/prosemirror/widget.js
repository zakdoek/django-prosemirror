/**
 * Browser component
 */

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
            $target.addClass("show");
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


$(document).ready(() => {
    $(".prosemirror-box").each((_, item) => new ProseMirrorWrapper(item));
});
