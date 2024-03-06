const kue = require('kue');

const queue = kue.createQueue();
const sendNotification = (phoneNumber, message, done) => {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  done();
};

queue.process('push_notification_code', (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, done);
});
