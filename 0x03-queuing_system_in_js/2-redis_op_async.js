import { createClient, print } from 'redis';
const { promisify } = require('util');


let client = undefined;
/**
 * Establish a connection to the reds
 * server on localhost port 6379. Logs
 * the current connection status.
 *
 * @return The instance of the connection
 * to the server.
 */
const connectToRedisServer = () => {
  // Ensure only one instance to the server
  // is maintained.
  if (client) return (client);

  client = createClient();

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

/**
 * Fetch the value of the given key
 * from the redis server asynchronously.
 *
 * @param {string} - The key to
 * the item to fetch.
 *
 */
const displaySchoolValue = async (key) => {
  const get = promisify(connectToRedisServer().get).bind(connectToRedisServer());

  console.log(await get(key));
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
