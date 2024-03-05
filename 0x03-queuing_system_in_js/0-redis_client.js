import { createClient } from 'redis';

/**
 * Establish a connection to the reds
 * server on localhost port 6379. Logs
 * the current connection status.
 */
const connectToRedisServer = () => {
  const client = createClient();

  client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));
  client.on('connect', () => console.log('Redis client connected to the server'));
};

connectToRedisServer();
