/**
 * Publish a message to a given channel.
 *
 */
import { createClient } from 'redis';

const client = createClient();

// Log any errors connecting to server.
client.on('error', (err) => { console.log(`Redis client not connected to the server: ${err}`); });
// Log successful connection to server.
client.on('connect', () => { console.log('Redis client connected to the server'); });

/**
 * Publish the given message to the
 * channel named `holberton school channel`.
 *
 * @params {string} - The message to publish.
 * @params {int} - The time in miliseconds
 * to take to publish the message.
 *
 */
const publishMessage = (msg, time) => {
  setTimeout(() => {
    console.log(`About to send ${msg}`);
    client.publish('holberton school channel', msg);
  }, time);
};

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
