/**
 * Maximum spec definition
 */

import {
    SchemaSpec,
    Doc,
    BlockQuote,
    OrderedList,
    BulletList,
    ListItem,
    Paragraph,
    Heading,
    HorizontalRule,
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
    blockquote: BlockQuote,
    ordered_list: OrderedList,
    bullet_list: BulletList,
    list_item: ListItem,

    paragraph: Paragraph,
    heading: Heading,

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
 * Specgen
 */
const getSpec = (rule=false, code=false) => {
    const nodesCopy = Object.assign({}, nodes);
    const marksCopy = Object.assign({}, marks);
    if (rule) {
        Object.assign(nodesCopy, {
            horizontal_rule: HorizontalRule
        });
    }

    if (code) {
        Object.assign(marksCopy, { code: CodeMark });
    }

    return new SchemaSpec(nodesCopy, marksCopy);
};


/**
 * Export the maxi spec
 */
export default getSpec;
