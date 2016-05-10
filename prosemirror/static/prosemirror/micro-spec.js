/**
 * Micro spec definition
 */

import {
    SchemaSpec,
    Doc,
    Paragraph,
    Text,
    HardBreak,
    EmMark,
    StrongMark,
    LinkMark,
    CodeMark
} from "prosemirror/dist/model";


/**
 * Define nodes
 */
const nodes = {
    doc: Doc,
    paragraph: Paragraph,
    text: Text,
    hard_break: HardBreak
};


/**
 * Define marks
 */
const marks = {
    em: EmMark,
    strong: StrongMark,
    link: LinkMark
};


/**
 * Spec generator
 */
const getSpec = (code=false) => {
    const marksCopy = Object.assign({}, marks);
    if (code) {
        Object.assign(marksCopy, { code: CodeMark });
    }
    return new SchemaSpec(nodes, marksCopy);
};


/**
 * Export schema spec
 */
export default getSpec;
