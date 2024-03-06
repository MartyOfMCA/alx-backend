/**
 * Subscribe to a channel and log every
 * message sent to the channel.
 *
 */

import { createClient } from 'redis';

const client = createClient();

// Report any errors connecting to server.
client.on('error', (err) => { console.log(`Redis client not connected to the server: ${err}`); });
// Report succesfuly connection to server.
client.on('connect', () => { console.log('Redis client connected to the server'); });


client.subscribe('holberton school channel');
// Log every message received on the
// subscribed channel.
client.on('message', (channel, msg) => {
 if (msg === 'KILL_SERVER') {
    console.log(msg);
    client.unsubscribe('holberton school channel');
 } else {
    console.log(`Channel ${channel} received message ${msg}`);
 }
});
