import { createClient, print } from 'redis';

/**
 * Establish a connection to the reds
 * server on localhost port 6379. Logs
 * the current connection status.
 *
 * @return The instance of the connection
 * to the server.
 */
const connectToRedisServer = () => {
  const client = createClient();

  client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));
  client.on('connect', () => console.log('Redis client connected to the server'));

  return (client);
};

/**
 * Add a new item to the redis server
 * with the given given and value.
 *
 * @param {string} - The key for the item
 * to be stored.
 * @param {string} - The value for the
 * item to be stored.
 */
const setNewSchool = (key, value) => {
  connectToRedisServer()
    .on('ready', function () {
      this.set(key, value, print);
  });
};

setNewSchool('HolbertonSanFrancisco', '100');