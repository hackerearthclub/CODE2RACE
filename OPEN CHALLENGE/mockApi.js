/**
 * This is a pure-node mock API server implementation
 * See below for options and api mock schema
 * By default server will respond with status 200 and json content-type
 */

const http = require('http');
const fs = require('fs');

const config = {
  port: 3000,
  path: './mockApi.json'
};

/**
 * Options handling
 * --port <port> to set port
 * last argument will be treated as mock path
 */
const args = process.argv.slice(2);
const filterArgs = list => {
  if (list.length === 0) {
    return;
  }
  const arg = list[0];
  if (list.length === 1) {
    config.path = arg;
    return;
  }
  if (arg.includes('--')) {
    config[arg.substr(2)] = list[1];
    list.splice(0, 2);
  } else {
    list.splice(0, 1);
  }
  filterArgs(list);
};

filterArgs(args);

/**
 * Api mock loading
 * Api mock follows the following schema
 * {
 *  "<METHOD> <path>": {
 *    "status": <code>,
 *    "headers": {
 *      <header name>: <header value>
 *    },
 *    "response": <response json>
 *  }
 * }
 *
 * Everything but response field is optional
 * See mockApi.json for example
 */
let mockApi = null;
try {
  fs.statSync(config.path);
  const apiData = fs.readFileSync(config.path, { encoding: 'utf-8' });
  mockApi = JSON.parse(apiData);
  console.log(`🧐  Loaded api from ${config.path}`);
} catch (e) {
  if (e.name === 'SyntaxError') {
    console.log(`⚠️  Could not parse ${config.path}`);
    process.exit(1);
  }
  if (e.message.includes('ENOENT')) {
    console.log(`⚠️  No api config found @ ${config.path}`);
    process.exit(1);
  }
}

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'application/json');

  const { method, url } = req;
  const data = mockApi[[method, url].join(' ')];

  console.log(`👉 ${method} ${url}`);

  if (data && data.response) {
    if (data.status) {
      res.statusCode = data.status;
    }
    if (data.headers) {
      Object.entries(data.headers).forEach(([h, v]) => res.setHeader(h, v));
    }
    res.end(JSON.stringify(data.response));
  } else {
    res.status = 404;
    console.log(`🤔 No response for ${method} ${url}`);
    res.end(JSON.stringify({}));
  }
});

server.listen(config.port, '127.0.0.1', () => {
  console.log('🚀 Started server');
  console.log(`🔗 http://localhost:${config.port}`);
});
