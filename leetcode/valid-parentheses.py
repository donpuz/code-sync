/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    // stack and then we push ( { [
    // pop and check ) } ]
    // if stack is empty at the end, return true
    // if any mismatch, return false

    const stack = [];
    const open = ['(', '{', '['];
    const close = [')', '}', ']'];
    for (const c of s) {
        if (open.includes(c)) {
            stack.push(c)
        }
        else if (close.includes(c)) {
            const openingBracket = stack.pop(c)
            if ((c === ')' && openingBracket !== '(') || (c === '}' && openingBracket !== '{') || (c === ']' && openingBracket !== '[')) {
                return false;
            }
        }
    }
    return stack.length === 0;
};