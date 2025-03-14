// monitoring_middleware.js
const morgan = require('morgan');
const client = require('prom-client');

// Collect default metrics
client.collectDefaultMetrics();

// Define a custom counter for HTTP requests
const requestCounter = new client.Counter({
  name: 'http_requests_total',
  help: 'Total number of HTTP requests',
  labelNames: ['method', 'route', 'status']
});

function prometheusMiddleware(req, res, next) {
  res.on('finish', () => {
    requestCounter.inc({
      method: req.method,
      route: req.originalUrl,
      status: res.statusCode
    });
  });
  next();
}

module.exports = prometheusMiddleware;
