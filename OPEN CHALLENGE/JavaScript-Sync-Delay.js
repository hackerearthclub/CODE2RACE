/*
JavaScript Synchronous Delay.
Author: Praveen Kumar Purushothaman
More Info: https://blog.praveen.science/right-way-of-delaying-execution-synchronously-in-javascript-without-using-loops-or-timeouts/
*/

function delay(n) {
  n = n || 2000;
  return new Promise(done => {
    setTimeout(() => {
      done();
    }, n);
  });
}

/*
Usage
-----
Make sure you use async and await here. This can be added in the Chrome's Developer Console, after loading the above script to see the effect.

  console.log("Start");
  console.time("Promise");
  await delay(2000);
  console.log("End");
  console.timeEnd("Promise");
*/
