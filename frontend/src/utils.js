/**
 * Turns a function into a debounced function.
 * The function will only be called after a defined timeout, but this timeout will be reset with
 * each additional function call.
 * For instance with keyboard input, a debounced input handler will only be called when the user
 * stops typing for the defined timeout period.
 * @param {function} fn - function to be debounced
 * @param {number} time - timeout value in milliseconds
 * @returns {Function} debounced function
 */
export const debounce = (fn, time) => {
  let timeout;
  return function (...args) {
    console.log('arguments:');
    console.log(args);
    const functionCall = () => fn.apply(this, args);
    clearTimeout(timeout);
    timeout = setTimeout(functionCall, time);
  };
};
