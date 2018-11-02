const readline = require('readline');
const util = require('util');

const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});
const question = text => new Promise(resolve => rl.question(text, resolve));
const stop = exitText => {
		rl.close();
		console.log('Stopping:', exitText);
		process.exit(1);
	};
const operationList = {
		'+': { noun: 'Sum', oper: (a, b) => a + b },
		'-': { noun: 'Difference', oper: (a, b) => a - b },
		'*': { noun: 'Product', oper: (a, b) => a * b },
		'/': { noun: 'Quotient', oper: (a, b) => b === 0 ? undefined : a / b }
	};
Object.assign(operationList, Object.entries({
	'+': [ 'add', 'addition', 'sum' ],
	'-': [ 'sub', 'subtract', 'difference', 'diff' ],
	'*': [ 'mult', 'multiply', 'multiplication', 'product', 'x' ],
	'/': [ 'div', 'divide', 'division', 'quotient', '\\' ]
}).reduce((p, [ key, aliases ]) => {
		aliases.forEach(a => p[a] = operationList[key]);
		return p;
	}, {}));
const maxRetries = 3;
const getElements = (m, n) => async (name, array) => {
		console.log(`\nEnter the ${m * n} elements of ${name} ${m}x${n} matrix:`);
		for(let c = 0; c < m; c++) {
			let retries = maxRetries;
			for(let d = 0; d < n; d++) {
				array[c][d] = parseFloat(await question(`(${c}, ${d}): `));
				if(array[c][d] !== array[c][d]) {
					if(retries) {
						console.log(`Value could not be parsed as a valid number, try again. ${retries}/${maxRetries}`);
						d--;
						retries--;
					}
					else {
						return stop(`Value could not be parsed as a valid number.`);
					}
				}
				else {
					retries = maxRetries;
				}
			}
		}
	};

(async () => {
	const counts = await question('Enter the number of rows and columns of matrix\nType "86" for 8x6 matrices or "4" for 4x4.\n');
	let { 0: m, 1: n, length } = counts;
	if(length !== 2 && length !== 1) {
		return stop(length ? 'Too many arguments.' : 'Not enough arguments.');
	}
	else if(length === 1) {
		n = m;
	}
	m = parseInt(m);
	n = parseInt(n);
	if(m !== m || n !== n) {
		return stop('Values could not be parsed as valid integers.');
	}
	else if(!m || !n) {
		return stop('Values cannot be 0.');
	}
	let operation;
	for(let i = maxRetries; i >= 0; i--) {
		const operationInput = await question('Choose an operation: + - * /\n');
		operation = operationList[operationInput];
		if(operation) {
			break;
		}
		if(i) {
			console.log(`Not a valid operation, try again. ${i}/${maxRetries}`);
		}
	}
	if(!operation) {
		return stop('Could not pick a valid operation.');
	}
	const { noun, oper } = operation;
	const [
		first, second, sum
	] = Array(3).fill().map(_ => Array(m).fill().map(_ => Array(n).fill(0)));
	const getData = getElements(m, n);
	await getData('first', first);
	await getData('second', second);
	console.log('\nFirst matrix:');
	console.table(first);
	console.log('\nSecond matrix:');
	console.table(second);
	rl.close();
	console.log(`\n${noun} of entered matrices:`);
	for(let c = 0; c < m; c++) {
		for(let d = 0; d < n; d++) {
			sum[c][d] = oper(first[c][d], second[c][d]);
		}
	}
	console.table(sum);
})();
