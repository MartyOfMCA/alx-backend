import { createClient, print } from 'redis';

let client;
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

const storeHashSet = () => {
  const obj = {
    Portland: 50,
    Seattle: 80,
    'New York': 20,
    Bogota: 20,
    Cali: 40,
    Paris: 2,
  };

  connectToRedisServer()
    // Silently ignore deprecated messages.
    // Deleting below lines would cause a
    // a prompt to be issued for every item
    // added to the set.
    .on('warning', () => {})
    .on('ready', function () {
      Object.entries(obj).forEach((entry) => {
        this.hset('HolbertonSchools', entry[0], entry[1], print);
      });
    });
};

storeHashSet();
